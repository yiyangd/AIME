/* Evaluate this function in functions.exec with its tools object. Default mode is read-only. */
async function publishViaConnector({tools, mode = 'plan', maxBlobs = 40, root = 'D:/AIME', progress = () => {}}) {
  if (!['plan', 'upload', 'publish'].includes(mode)) throw Error('Unknown publisher mode');
  const repo = 'yiyangd/AIME';
  const manifestPath = `${root}/output/release/publication-manifest.json`;
  const statePath = `${root}/output/release/connector-state.json`;
  async function bridge(code) {
    const result = await tools.mcp__node_repl__js({code, title: 'Read the allowlisted AIME publication files'});
    if (result.isError) throw Error('Local publication bridge failed');
    return JSON.parse(result.content.filter(c => c.type === 'text').map(c => c.text).join('\n'));
  }
  const manifest = await bridge(`var publicationFs=await import('node:fs/promises');nodeRepl.write(await publicationFs.readFile(${JSON.stringify(manifestPath)},'utf8'));`);
  if (manifest.repository !== repo || manifest.branch !== 'main') throw Error('Unexpected publication destination');
  const files = manifest.files;
  for (const f of files) {
    if (!f.path || f.path.startsWith('/') || f.path.includes('\\') || f.path.split('/').includes('..')) throw Error('Unsafe public path');
    if (f.path.split('/').some(p => ['node_modules','.git','.aws','.codex','__pycache__'].includes(p))) throw Error('Private local directory entered publication manifest');
    const publicSourceMetadata = new Set(['sources/README-audit.md','sources/inventory.json','sources/fetch_manifest.json','sources/asset_manifest.json']);
    if (f.path.startsWith('sources/') && !publicSourceMetadata.has(f.path)) throw Error('Private source material entered publication manifest');
    if (/^(tmp\/|output\/release\/|web\/(dist|\.astro)\/)/.test(f.path)) throw Error('Private or generated input entered publication manifest');
  }
  let state = await bridge(`var publicationState;try{publicationState=JSON.parse(await publicationFs.readFile(${JSON.stringify(statePath)},'utf8'));}catch(e){if(e.code!=='ENOENT')throw e;publicationState={repository:${JSON.stringify(repo)},uploaded:[]};}nodeRepl.write(JSON.stringify(publicationState));`);
  if (state.repository !== repo) throw Error('Wrong cached repository');
  const uploaded = new Set(state.uploaded);
  const unique = [...new Map(files.map(f => [f.git_blob_sha1, f])).values()];
  const pending = unique.filter(f => !uploaded.has(f.git_blob_sha1));
  if (mode === 'plan') return {mode, final: manifest.final, files: files.length, uniqueBlobs: unique.length, pendingBlobs: pending.length, uniqueBytes: manifest.unique_blob_bytes, filesSha256: manifest.files_sha256, remoteWrites: false};
  if (!manifest.final || manifest.errors.length) throw Error('Run prepare_publication.py --final after final QA before uploading');
  async function save() {
    state.uploaded = [...uploaded];
    await bridge(`await publicationFs.writeFile(${JSON.stringify(statePath)},${JSON.stringify(JSON.stringify(state, null, 2))},'utf8');nodeRepl.write('true');`);
  }
  function structured(result) {
    if (result.isError) throw Error(JSON.stringify(result.structuredContent || result.content));
    return result.structuredContent || {};
  }
  function sha(result) {
    const value = structured(result);
    const found = value.sha || value.commit_sha || value.commit?.sha || value.tree_sha || value.blob_sha;
    if (!found || !/^[0-9a-f]{40}$/.test(found)) throw Error('Connector did not return a Git object SHA: ' + JSON.stringify(value));
    return found;
  }
  async function readFiles(selected) {
    return bridge(`var publicationCrypto=await import('node:crypto');var publicationSelection=${JSON.stringify(selected)};var publicationPayload=[];for(var publicationFile of publicationSelection){var publicationBuffer=await publicationFs.readFile(${JSON.stringify(root)}+'/'+publicationFile.path);if(publicationCrypto.createHash('sha256').update(publicationBuffer).digest('hex')!==publicationFile.sha256)throw Error('File changed after final QA: '+publicationFile.path);publicationPayload.push({path:publicationFile.path,sha:publicationFile.git_blob_sha1,data:publicationBuffer.toString('base64'),utf8:publicationFile.path==='README.md'?publicationBuffer.toString('utf8'):undefined});}nodeRepl.write(JSON.stringify(publicationPayload));`);
  }
  if (!state.parentSha) {
    const metadata = structured(await tools.mcp__codex_apps__github_get_repo({repository_full_name: repo}));
    if (!metadata.permissions?.push || !metadata.permissions?.admin) throw Error('Connected account lacks expected repository permissions');
    if (metadata.size !== 0) throw Error('Repository is no longer empty: inspect its head before initializing');
    const readme = files.find(f => f.path === 'README.md');
    if (!readme) throw Error('README missing from publication allowlist');
    const [payload] = await readFiles([readme]);
    state.parentSha = sha(await tools.mcp__codex_apps__github_create_file({repository_full_name:repo,path:'README.md',content:payload.utf8,message:'Initialize the reviewed AIME learning pack'}));
    uploaded.add(readme.git_blob_sha1);
    state.initializedByPublisher = true;
    await save();
  }
  if (!state.initializedByPublisher) throw Error('No verified initial publication state');
  if (mode === 'upload') {
    let completed = 0;
    const selected = unique.filter(f => !uploaded.has(f.git_blob_sha1)).slice(0,maxBlobs);
    for (let start=0; start<selected.length; start+=6) {
      const payload = await readFiles(selected.slice(start,start+6));
      const results = await Promise.allSettled(payload.map(async f => {
        const actual = sha(await tools.mcp__codex_apps__github_create_blob({repository_full_name:repo,encoding:'base64',content:f.data}));
        if (actual !== f.sha) throw Error('Uploaded Git blob identity differs for '+f.path);
        return actual;
      }));
      for (const result of results) if (result.status === 'fulfilled') {uploaded.add(result.value);completed++;}
      await save();
      const failed = results.find(r => r.status === 'rejected');
      if (failed) throw failed.reason;
      progress({uploadedThisCall:completed,remaining:unique.filter(f => !uploaded.has(f.git_blob_sha1)).length});
    }
    return {mode,uploadedThisCall:completed,remaining:unique.filter(f => !uploaded.has(f.git_blob_sha1)).length,parentSha:state.parentSha,branchUpdated:false};
  }
  if (unique.some(f => !uploaded.has(f.git_blob_sha1))) throw Error('Upload all manifest blobs before final publication');
  // Revalidate every local hash together before committing the final tree.
  const verified = await bridge(`var publicationCrypto=await import('node:crypto');var publicationManifest=JSON.parse(await publicationFs.readFile(${JSON.stringify(manifestPath)},'utf8'));if(publicationManifest.files_sha256!==${JSON.stringify(manifest.files_sha256)})throw Error('Manifest changed');for(var publicationFile of publicationManifest.files){var publicationBuffer=await publicationFs.readFile(${JSON.stringify(root)}+'/'+publicationFile.path);if(publicationCrypto.createHash('sha256').update(publicationBuffer).digest('hex')!==publicationFile.sha256)throw Error('Final file changed: '+publicationFile.path);}nodeRepl.write('true');`);
  if (!verified) throw Error('Final file validation failed');
  if (state.publishedFilesSha256 === manifest.files_sha256) return {mode,alreadyPublished:true,commit:state.publishedSha};
  const treeSha = sha(await tools.mcp__codex_apps__github_create_tree({repository_full_name:repo,tree_elements:files.map(f => ({path:f.path,mode:'100644',type:'blob',sha:f.git_blob_sha1}))}));
  const commitSha = sha(await tools.mcp__codex_apps__github_create_commit({repository_full_name:repo,tree_sha:treeSha,parent_sha:state.parentSha,message:'Publish reviewed bilingual AIME 2000–2026 pack\n\nPublic manifest: '+manifest.files_sha256}));
  state.pendingCommitSha = commitSha;await save();
  structured(await tools.mcp__codex_apps__github_update_ref({repository_full_name:repo,branch_name:'main',sha:commitSha,expected_sha:state.parentSha,force:false}));
  state.publishedSha=commitSha;state.publishedFilesSha256=manifest.files_sha256;state.parentSha=commitSha;delete state.pendingCommitSha;await save();
  return {mode,commit:commitSha,files:files.length,site:'https://yiyangd.github.io/AIME/',pagesMustUseActions:true};
}
