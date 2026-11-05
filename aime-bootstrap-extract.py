"""Verify and unpack the reviewed AIME release; run from the repository root.

No external dependencies. All .github members are verified in the ZIP but skipped
on disk, allowing a temporary bootstrap workflow to remain until replaced in UI.
"""
import hashlib,json,os,re,stat,sys,tempfile,zipfile
from pathlib import Path,PurePosixPath

MAX_ARCHIVE_BYTES=20_000_000
ARCHIVE_PATTERN=re.compile(r'aime-upload-part-[0-9]{3}\.zip\Z')
EXPECTED_MANIFEST_SHA256='c47f5695ba7417ef403ff80ac709af146a85eb507a38c4655333e745e06ff7b8'

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def member_path(value):
    if not isinstance(value,str) or not value or '\\' in value or ':' in value or any(ord(c)<32 for c in value):
        raise ValueError('Invalid repository path: '+repr(value))
    p=PurePosixPath(value)
    if p.is_absolute() or str(p)!=value or any(c in {'','.', '..'} or c.casefold()=='.git' for c in p.parts):
        raise ValueError('Unsafe repository path: '+repr(value))
    return p

def inside(root,path):
    candidate=root.joinpath(*member_path(path).parts)
    if not candidate.resolve().is_relative_to(root):raise ValueError('Path escapes repository: '+path)
    cursor=candidate
    while cursor!=root:
        if cursor.is_symlink():raise ValueError('Symlink in destination path: '+str(cursor))
        cursor=cursor.parent
    return candidate

def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def main():
    root=Path.cwd().resolve()
    if not (root/'.git').exists():raise ValueError('Run inside the checked-out repository root.')
    script=Path(__file__).resolve()
    if script!=root/'aime-bootstrap-extract.py':raise ValueError('Bootstrap extractor must be at the repository root.')
    manifest_path=inside(root,'publication-manifest.json');index_path=inside(root,'archive-index.json')
    index=load(index_path)
    if not re.fullmatch('[0-9a-f]{64}',EXPECTED_MANIFEST_SHA256):raise ValueError('Bootstrap has not been pinned to a final manifest.')
    if digest(manifest_path)!=EXPECTED_MANIFEST_SHA256 or index['publication_manifest_sha256']!=EXPECTED_MANIFEST_SHA256:raise ValueError('Publication manifest SHA256 differs from the pinned release.')
    manifest=load(manifest_path)
    if manifest.get('final') is not True or manifest.get('errors') or manifest.get('repository')!='yiyangd/AIME':
        raise ValueError('A final, error-free yiyangd/AIME publication manifest is required.')
    records=manifest['files'];expected={};casefold=set();by_hash={}
    for item in records:
        name=str(member_path(item['path']))
        if name in expected or name.casefold() in casefold:raise ValueError('Duplicate or case-colliding manifest member: '+name)
        if not isinstance(item['bytes'],int) or item['bytes']<0 or not re.fullmatch('[0-9a-f]{64}',item['sha256']):raise ValueError('Invalid member size or hash: '+name)
        expected[name]=item;casefold.add(name.casefold());inside(root,name);by_hash.setdefault(item['sha256'],[]).append(name)
    identity=json.dumps(records,sort_keys=True,separators=(',',':')).encode()
    if hashlib.sha256(identity).hexdigest()!=manifest['files_sha256']:raise ValueError('Manifest file-list identity mismatch.')
    if len(records)!=manifest['file_count'] or sum(x['bytes'] for x in records)!=manifest['total_bytes']:raise ValueError('Manifest totals mismatch.')
    if index.get('mode')!='deduplicated-content':raise ValueError('Expected deduplicated-content archive index.')
    payloads={}
    for item in index['payloads']:
        name=str(member_path(item['path']));h=item['sha256']
        if h in payloads or name not in expected or expected[name]['sha256']!=h or expected[name]['bytes']!=item['bytes'] or sorted(item['targets'])!=sorted(by_hash[h]):raise ValueError('Payload mapping differs from reviewed manifest: '+name)
        payloads[h]=item
    if set(payloads)!=set(by_hash):raise ValueError('Payload map does not cover every reviewed content hash.')
    seen=set();archives=[]
    # Validate every byte before changing any repository file.
    for archive in index['archives']:
        filename=archive['filename']
        if not ARCHIVE_PATTERN.fullmatch(filename):raise ValueError('Unexpected archive filename: '+filename)
        path=inside(root,filename)
        if path.stat().st_size!=archive['bytes'] or path.stat().st_size>MAX_ARCHIVE_BYTES or digest(path)!=archive['sha256']:
            raise ValueError('Archive size or SHA256 mismatch: '+filename)
        names=archive['files']
        if len(names)!=archive['file_count'] or len(set(names))!=len(names):raise ValueError('Archive index contains duplicate members.')
        with zipfile.ZipFile(path) as z:
            infos=z.infolist()
            if len(infos)!=len(names) or {i.filename for i in infos}!=set(names):raise ValueError('Archive members differ from index: '+filename)
            for info in infos:
                name=str(member_path(info.filename));mode=info.external_attr>>16
                if name not in expected:raise ValueError('Unknown ZIP member: '+name)
                content_hash=expected[name]['sha256']
                if content_hash in seen or payloads[content_hash]['path']!=name:raise ValueError('Duplicate or unexpected payload representative: '+name)
                if info.is_dir() or stat.S_ISLNK(mode) or stat.S_IFMT(mode) not in {0,stat.S_IFREG} or info.flag_bits&1:
                    raise ValueError('Nonregular or encrypted ZIP member: '+name)
                if info.compress_type not in {zipfile.ZIP_STORED,zipfile.ZIP_DEFLATED}:raise ValueError('Unsupported ZIP compression.')
                target=expected[name]
                if info.file_size!=target['bytes']:raise ValueError('Uncompressed member size differs: '+name)
                h=hashlib.sha256();size=0
                with z.open(info) as stream:
                    for block in iter(lambda:stream.read(1024*1024),b''):
                        size+=len(block)
                        if size>target['bytes']:raise ValueError('Member exceeds reviewed size: '+name)
                        h.update(block)
                if size!=target['bytes'] or h.hexdigest()!=target['sha256']:raise ValueError('Member SHA256 differs: '+name)
                seen.add(content_hash);inside(root,name)
        archives.append(path)
    if seen!=set(by_hash):raise ValueError('Archive union does not cover every reviewed payload.')
    if index['file_count']!=len(expected) or index['payload_count']!=len(by_hash):raise ValueError('Archive index total differs from manifest.')
    skipped=[];written=0
    for archive_path in archives:
        with zipfile.ZipFile(archive_path) as z:
            for info in z.infolist():
                for name in by_hash[expected[info.filename]['sha256']]:
                    if member_path(name).parts[0].casefold()=='.github':
                        target=inside(root,name)
                        skipped.append(dict(path=name,expected_sha256=expected[name]['sha256'],existing_sha256=digest(target) if target.is_file() else None))
                        continue
                    target=inside(root,name);target.parent.mkdir(parents=True,exist_ok=True);inside(root,name)
                    fd,tmp=tempfile.mkstemp(prefix='.aime-unpack-',dir=target.parent)
                    try:
                        with os.fdopen(fd,'wb') as out,z.open(info) as source:
                            for block in iter(lambda:source.read(1024*1024),b''):out.write(block)
                        temporary=Path(tmp)
                        if digest(temporary)!=expected[name]['sha256']:raise ValueError('Extraction hash mismatch: '+name)
                        inside(root,name);os.replace(temporary,target);written+=1
                    finally:
                        temporary=Path(tmp)
                        if temporary.exists():temporary.unlink()
    for name,item in expected.items():
        if member_path(name).parts[0].casefold()!='.github' and digest(inside(root,name))!=item['sha256']:
            raise ValueError('Post-extraction verification failed: '+name)
    # Exact reviewed bootstrap filenames only; no recursive removal is performed.
    for path in archives+[index_path,manifest_path,script]:
        if path.parent!=root or path.is_symlink() or not path.resolve().is_relative_to(root):raise ValueError('Unsafe bootstrap cleanup path: '+str(path))
        path.unlink()
    print(json.dumps(dict(status='passed',publication_manifest_sha256=EXPECTED_MANIFEST_SHA256,verified_payloads=len(by_hash),verified_files=len(expected),written_files=written,skipped_github=skipped,archives_removed=len(archives),bootstrap_removed=True,uploaded_manifest_removed=True),ensure_ascii=False,indent=2))

if __name__=='__main__':
    try:main()
    except Exception as error:
        print('AIME bootstrap verification failed: '+str(error),file=sys.stderr);raise SystemExit(1)
