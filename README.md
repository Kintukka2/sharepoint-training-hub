# sharepoint-training-hub

Planning and design for the **D365 Training Hub**, WiseTech Global's SharePoint site for Dynamics 365 procedure guides (PGs), quick reference guides (QRGs), recordings and templates.

Live preview of the homepage: https://claude.ai/artifact/JaF5CzfGopBHiwbvLhaFMm (private; share it from the page's Share menu)

| Path | What it is |
| --- | --- |
| [`sharepoint/d365-training-hub.html`](sharepoint/d365-training-hub.html) | **The file to upload.** The homepage as a SharePoint HTML page, with fonts embedded. Built from the source below |
| [`sharepoint/src/d365-training-hub.html`](sharepoint/src/d365-training-hub.html) | The page source to edit: styles, content data and the settings block |
| [`sharepoint/fonts/`](sharepoint/fonts) | DM Sans and DM Mono (WiseTech Global brand typefaces), Latin subset, WOFF2 |
| [`tools/build.py`](tools/build.py) | Embeds the fonts and writes the upload file |
| [`docs/PLAN.md`](docs/PLAN.md) | The plan: outcomes, audiences, resource types, site map, homepage sections, content model, SharePoint build approach, governance, roadmap and open decisions |
| [`prototype/home.html`](prototype/home.html) | The original concept prototype, with the Build notes overlay that maps each section to a SharePoint web part |

## Put the homepage on SharePoint

1. Open `sharepoint/src/d365-training-hub.html` and fill in the **SETTINGS** block at the top of the script:
   - `siteUrl`: the full URL of the training hub site
   - `sitePaths`: change any page or library path that differs on your site
   - `external`: the support portal, Teams channel, office hours booking page, Microsoft Forms suggestion form and training environment
2. Build the upload file:
   ```sh
   python3 tools/build.py
   ```
   For a quick change you can also edit the same SETTINGS block directly in `sharepoint/d365-training-hub.html`.
3. In SharePoint, go to **Site Pages → Upload → Files**, choose `d365-training-hub.html`, then open it and select **Publish**. (**+ New → HTML page → Upload an HTML file** works too, but opening that screen needs a Microsoft 365 Copilot license.)
4. Check on the first upload:
   - Fonts show as DM Sans and DM Mono
   - Links open the whole page, not just the frame. If they do nothing, set `linkTarget` to `"_blank"`
   - **Make homepage** is offered for the page in Site Pages
   - The page reads well in the SharePoint mobile app

Until a resource has a direct link (the optional 10th value in each `ROWS` entry), its buttons search the site for its document code. Links left empty in `external` point nowhere and are listed in the browser console.

## What SharePoint HTML pages allow

SharePoint renders the page in a sandboxed frame under its own header and navigation. Scripts must be inside the file, the page cannot fetch data or call APIs, browser storage is unavailable, forms cannot submit, and the HTML file can be up to 10 MB. Comments, likes, news promotion, scheduling, co-authoring and page templates are not available. Source: [Create, upload, edit, and publish HTML pages in SharePoint](https://support.microsoft.com/en-us/sharepoint/create-edit-publish-html-pages).

So the page holds no personal content (no greeting by name, resume card, progress or "action required"), and the library, learning paths, sessions and change notices are data inside the file until they are replaced with the real content.
