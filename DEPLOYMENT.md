# Publishing the reviewed AIME pack

The public website is built from `web/` and deployed to <https://yiyangd.github.io/AIME/>. The workflow in `.github/workflows/pages.yml` installs the lockfile, checks Astro and mathematics, builds the site, verifies internal links, and uploads only `web/dist`.

The repository stores the authored canonical data, original diagrams, production scripts, independent review receipts and final public products. Source downloads and original evidence images/PDFs stay local. The public importer uses the final PDF page manifests, so run it after the final print build and verify its links before preparing a release. GitHub Actions builds the already imported reviewed website snapshot; it does not fetch or republish source contest text.

Prepare and inspect the publication manifest with:

```text
python scripts/prepare_publication.py
python scripts/check_publication_snapshot.py
python scripts/prepare_publication.py --final
```

The first command inventories an explicit allowlist. After all final products have been imported, the check wrapper runs Astro, math, build, local-link and PDF-link checks against unchanged inputs and records exact input/report hashes. The final command requires complete independent reviews, final public products and that current check receipt. None of these commands publishes. `output/release/publication-manifest.json` records SHA-256 and Git blob identities; local connector-upload state stays in the ignored release directory.

The user has repository administration and push rights, but the connected integration's actual file-write test returned 403 `Resource not accessible by integration`. A successful repository metadata read does not establish integration write permission. This workspace's unrelated cached Git identity also cannot push. The connector publisher in `scripts/publish_via_connector.js` is retained as a prepared alternative; it has not published this pack and requires working integration write access before use.

The working publication route uses the authenticated GitHub web UI. The reviewed allowlist is packaged into ZIP parts below 20 MB, with an archive index and path-safe extractor. A temporary `workflow_dispatch`-only restore workflow is created through the web editor at `.github/workflows/pages.yml`. Its repository-scoped workflow token verifies the archive/member hashes, expands readable public files, skips `.github` members, removes the temporary archives from the branch tip, and commits the restored pack. The archive remains recoverable in Git history.

After restoration, the web editor replaces that temporary file with the exact locally reviewed `.github/workflows/pages.yml`. Its push trigger builds and deploys the complete site. Keeping the temporary restore workflow outside the frozen local project prevents it from changing the reviewed website inputs. No new personal token or integration permission is used.

Before the first deployment, select **GitHub Actions** as the source under [Settings → Pages](https://github.com/yiyangd/AIME/settings/pages). The available connector has no Pages-settings endpoint. Use the authenticated repository UI for this setting; do not store a personal access token in the project. The ordinary workflow token can deploy to an enabled Pages site, but `configure-pages` cannot initially enable one with that token alone.

GitHub's current [custom-workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) specifies the Pages artifact and deployment permissions. The [configure-pages input definition](https://github.com/actions/configure-pages/blob/v5/action.yml) documents the separate token requirement for automatic first-time enablement.
