# Training Hub homepage (SharePoint embed)

`training-hub.html` is the Training Hub homepage as a single HTML file, ready to drop into SharePoint. It recreates the Training Hub mockup with two changes:

- **Quick links** in the hero: Support, WiseTech Academy, Procedure Guides, Quick Reference Guides, Communications, D365 Templates, Success Stories, Recordings.
- **Project Timeline** replaces Upcoming Training. It has a countdown to the next go-live, a roadmap of milestones, events and go-lives with a "today" marker, and a detail row for the selected milestone.

Action Required, Resources for your role, My Training Bookmarks, Feedback and the footer follow the mockup.

Live preview: https://claude.ai/artifact/LouimmFEdSB5QB1WApiEKy (private; share it from the page's Share menu).

All dates, milestones, due dates and role-card text are sample content.

## Put it on SharePoint

### Option 1: Embed web part (no app deployment)

1. Upload `training-hub.html` and the `images` folder to the site's **Site Assets** library. Keep `images/` next to the HTML file.
2. Edit the page, add a **full-width section**, add an **Embed** web part and paste:

   ```html
   <iframe src="https://<tenant>.sharepoint.com/sites/<site>/SiteAssets/training-hub.html" width="100%" height="2200" style="border:0"></iframe>
   ```

3. If SharePoint downloads the file or shows "File not found" instead of rendering it, rename the file to `training-hub.aspx` and use that URL. How SharePoint serves HTML files from a library depends on the tenant's custom-script settings and the site type.

The page is about 2,200px tall at desktop width; set the iframe `height` to match. Links inside the frame open in the full SharePoint page.

### Option 2: Script-editor web part

Paste the whole file into a script-editor web part (for example the PnP Modern Script Editor sample, which an admin deploys to the app catalog). All CSS is scoped under `.th` and all script under `#th-root`, so nothing leaks into SharePoint's own chrome. Change the `images/...` paths to full Site Assets URLs.

SharePoint Online's Content Security Policy enforcement ([MC1193419](https://mc.merill.net/message/MC1193419)) blocks inline script in SPFx web parts. The page renders completely without script; the live parts listed below stay in their saved state.

### Option 3: Native web parts

For the long-term build, [`docs/PLAN.md`](../docs/PLAN.md) maps each homepage section to native web parts and PnP Modern Search.

## What the script does

| Part | Behavior |
| --- | --- |
| Greeting | Shows the viewer's first name from SharePoint ("How can I help you, Sabina?"). Elsewhere it reads "How can I help you today?" |
| Search | Opens the site's search results page for the query |
| Project Timeline | Works out Completed, Up next and Planned from today's date, places the today marker, counts down to the next go-live, and shows details for the selected milestone |
| Action Required | Turns an item pink inside 7 days of its due date and marks it Overdue after |
| Resources for your role | Role tabs, with arrow-key support |
| My Training Bookmarks | Add/ Remove opens an editor. Each person's bookmarks are saved in their browser |
| Feedback | Saves to a SharePoint list called **Training Hub Feedback** with a **Comments** column (Multiple lines of text). Create the list before going live |

## Edit the content

Open `training-hub.html` and search for these markers:

| Marker | What to change |
| --- | --- |
| `QUICK LINKS` | The `href` of each of the eight tiles |
| `TIMELINE` | One `<li>` per milestone, oldest first: `data-date` (YYYY-MM-DD), `data-kind` (`milestone`, `event` or `golive`), the title, and the hidden note shown in the detail row |
| `ACTION REQUIRED` | Each item's title, `data-due` date and link |
| `ROLE CARDS` | Four cards per role tab |
| `BOOKMARKS` | The default bookmarks |
| `SETTINGS` | Feedback list and column names, search URL, the due-soon window, and a `today` override for previewing another date |

Images: replace the files in `images/` (hero portrait 760 × 880, cards 640 × 440). The current photos come from Unsplash (free under the Unsplash License) and stand in for your own photography.
