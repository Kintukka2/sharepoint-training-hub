# sharepoint-training-hub

Planning and design for the **D365 Training Hub**, WiseTech Global's SharePoint site for Dynamics 365 procedure guides (PGs), quick reference guides (QRGs), recordings and templates.

Live preview of the homepage: https://claude.ai/artifact/JaF5CzfGopBHiwbvLhaFMm (private; share it from the page's Share menu)

| Path | What it is |
| --- | --- |
| [`sharepoint/d365-training-hub.html`](sharepoint/d365-training-hub.html) | **The file to upload.** The homepage as a SharePoint HTML page, with fonts embedded. Built from the source below |
| [`sharepoint/src/d365-training-hub.html`](sharepoint/src/d365-training-hub.html) | The page source to edit: styles, content data and the settings block |
| [`sharepoint/fonts/`](sharepoint/fonts) | DM Sans and DM Mono (WiseTech Global brand typefaces), Latin subset, WOFF2 |
| [`sharepoint/training-hub.html`](sharepoint/training-hub.html) | **The Training Hub homepage to upload.** The Training Hub mockup with new quick links and a Project Timeline. Fonts and photos embedded. See [Training Hub homepage](#training-hub-homepage) |
| [`sharepoint/src/training-hub.html`](sharepoint/src/training-hub.html) | Its source: styles, content and the settings block |
| [`sharepoint/images/`](sharepoint/images) | Photos for the Training Hub homepage (from Unsplash, standing in for your own photography) |
| [`tools/build.py`](tools/build.py) | Embeds the fonts and photos and writes the upload files, one per page in `sharepoint/src` |
| [`docs/PLAN.md`](docs/PLAN.md) | The plan: outcomes, audiences, resource types, site map, homepage sections, content model, SharePoint build approach, governance, roadmap and open decisions |
| [`prototype/home.html`](prototype/home.html) | The original concept prototype, with the Build notes overlay that maps each section to a SharePoint web part |

## Put the homepage on SharePoint

1. The **SETTINGS** block at the top of the script in `sharepoint/src/d365-training-hub.html` already points at the WTG - Atlas site (`https://wisetechglobal.sharepoint.com/sites/Atlas`): the Atlas home page, the D365 User Support Hub, the D365 Procedure Guides library and each guide's PDF. Still to set:
   - `briefingSessions`, `recordings`, `quickReference` and `templates`: their folder or page paths (they open the Training library until then)
   - `trainingEnvironment`: the D365 training environment URL (until then, "Put it into practice" opens the recordings)
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

The procedure guides, business areas and Business Process Owners live in the CONTENT block (`AREAS`, `PGS`, `PATHS`). Add a guide by adding a line to `PGS`; its PDF link is built from the number and title, matching the library's `<number>-<title> PG.pdf` file names. The learning paths are a proposed grouping of those guides by role.

## Training Hub homepage

`sharepoint/training-hub.html` recreates the Training Hub mockup with two changes:

- **Quick links:** the hero tiles are Support, WiseTech Academy, Procedure Guides, Quick Reference Guides, Communications, D365 Templates, Success Stories and Recordings.
- **Project Timeline replaces Upcoming Training.** It shows a countdown to the next go-live, a roadmap of milestones, events and go-lives with a marker for today, and details for the milestone someone selects. Completed, Up next and Planned come from today's date.

Action Required, Resources for your role, My Training Bookmarks, Feedback and the footer follow the mockup. Live preview: https://claude.ai/artifact/LouimmFEdSB5QB1WApiEKy (private; share it from the page's Share menu)

To put it on SharePoint:

1. In `sharepoint/src/training-hub.html`, fill in the **SETTINGS** block at the top of the script: `siteUrl` (hero search), `linkTarget`, and `feedbackForm`.
2. Run `python3 tools/build.py`.
3. Upload `sharepoint/training-hub.html` to Site Pages and publish it, as in the steps above.

To change the content, search the source for these markers:

| Marker | What to change |
| --- | --- |
| `QUICK LINKS` | The `href` of each of the eight tiles |
| `TIMELINE` | One `<li>` per milestone, oldest first: `data-date` (YYYY-MM-DD), `data-kind` (`milestone`, `event` or `golive`), the title, and the hidden note shown in the detail row |
| `ACTION REQUIRED` | Each item's title, `data-due` date and link |
| `ROLE CARDS` | Four cards per role tab; the photos are set in the `th-card-img` styles |
| `BOOKMARKS` | The default bookmarks |

How the sandbox shapes this page:

- **Greeting:** reads "How can I help you today?" because the page can't tell who is viewing.
- **Action Required:** lists the same mandatory items for everyone. An item turns pink 7 days before it is due and shows Overdue after.
- **Bookmarks:** anything people add or remove lasts until they leave the page.
- **Feedback:** Submit opens the Microsoft Forms link in `feedbackForm` in a new tab. Use the form's pre-filled link with `FEEDBACK` as the answer, and the typed text carries across.

All milestones, dates and role-card text are sample content.

## What SharePoint HTML pages allow

SharePoint renders the page in a sandboxed frame under its own header and navigation. Scripts must be inside the file, the page cannot fetch data or call APIs, browser storage is unavailable, forms cannot submit, and the HTML file can be up to 10 MB. Comments, likes, news promotion, scheduling, co-authoring and page templates are not available. Source: [Create, upload, edit, and publish HTML pages in SharePoint](https://support.microsoft.com/en-us/sharepoint/create-edit-publish-html-pages).

So the page holds no personal content (no greeting by name, resume card, progress or "action required"), and the guide list is data inside the file: update `PGS` when guides are added or renamed.
