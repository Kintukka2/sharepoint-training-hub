# sharepoint-training-hub

Planning and design for the **Atlas Training Hub**, WiseTech Global's SharePoint site for Dynamics 365 procedure guides (PGs), quick reference guides (QRGs), recordings and templates.

Live preview of the homepage: https://claude.ai/artifact/JaF5CzfGopBHiwbvLhaFMm (private; share it from the page's Share menu)

| Path | What it is |
| --- | --- |
| [`sharepoint/atlas-training-hub.html`](sharepoint/atlas-training-hub.html) | **The file to upload.** The homepage as a SharePoint HTML page, with fonts embedded. Built from the source below |
| [`sharepoint/src/atlas-training-hub.html`](sharepoint/src/atlas-training-hub.html) | The page source to edit: styles, content data and the settings block |
| [`sharepoint/fonts/`](sharepoint/fonts) | DM Sans and DM Mono (WiseTech Global brand typefaces), Latin subset, WOFF2 |
| [`tools/build.py`](tools/build.py) | Embeds the fonts and writes the upload file |
| [`docs/PLAN.md`](docs/PLAN.md) | The plan: outcomes, audiences, resource types, site map, homepage sections, content model, SharePoint build approach, governance, roadmap and open decisions |
| [`prototype/home.html`](prototype/home.html) | The original concept prototype, with the Build notes overlay that maps each section to a SharePoint web part |

## Put the homepage on SharePoint

1. The **SETTINGS** block at the top of the script in `sharepoint/src/atlas-training-hub.html` already points at the WTG - Atlas site (`https://wisetechglobal.sharepoint.com/sites/Atlas`): the Atlas home page, the D365 User Support Hub, the FAQs page, the D365 Procedure Guides and D365 Templates folders, each guide's PDF, and the D365 support form (Microsoft Forms, opens in a new tab). Still to set:
   - `briefingSessions`, `recordings` and `quickReference`: their folder or page paths (they open the Training library until then)
   - `trainingEnvironment`: the D365 training environment URL (until then, "Put it into practice" opens the recordings)
2. Build the upload file:
   ```sh
   python3 tools/build.py
   ```
   For a quick change you can also edit the same SETTINGS block directly in `sharepoint/atlas-training-hub.html`.
3. In SharePoint, go to **Site Pages → Upload → Files**, choose `atlas-training-hub.html`, then open it and select **Publish**. (**+ New → HTML page → Upload an HTML file** works too, but opening that screen needs a Microsoft 365 Copilot license.)
4. Check on the first upload:
   - Fonts show as DM Sans and DM Mono
   - Links open the whole page, not just the frame. If they do nothing, set `linkTarget` to `"_blank"`
   - The support form opens. If SharePoint blocks it, a site owner adds `forms.cloud.microsoft` to **Site settings → HTML Field Security**
   - **Make homepage** is offered for the page in Site Pages
   - The page reads well in the SharePoint mobile app

The procedure guides, business areas and Business Process Owners live in the CONTENT block (`AREAS`, `PGS`, `PATHS`). Add a guide by adding a line to `PGS`; its PDF link is built from the number and title, matching the library's `<number>-<title> PG.pdf` file names. The learning paths are a proposed grouping of those guides by role.

## What SharePoint HTML pages allow

SharePoint renders the page in a sandboxed frame under its own header and navigation. Scripts must be inside the file, the page cannot fetch data or call APIs, browser storage is unavailable, forms cannot submit, and the HTML file can be up to 10 MB. Comments, likes, news promotion, scheduling, co-authoring and page templates are not available. Source: [Create, upload, edit, and publish HTML pages in SharePoint](https://support.microsoft.com/en-us/sharepoint/create-edit-publish-html-pages).

So the page holds no personal content (no greeting by name, resume card, progress or "action required"), and the guide list is data inside the file: update `PGS` when guides are added or renamed.
