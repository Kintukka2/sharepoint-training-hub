# Atlas Training Hub: plan

Draft 0.1 · 23 Oct 2026 · Homepage prototype: [`prototype/home.html`](../prototype/home.html) · [live preview](https://claude.ai/artifact/JaF5CzfGopBHiwbvLhaFMm)

The Atlas Training Hub is the one place a WiseTech Global employee goes to learn and carry out a Dynamics 365 process correctly. It holds four mandatory resource types (procedure guides, quick reference guides, recordings and templates), organized by process area and by role, and it tells people when a process changes.

This plan covers what the site contains, how it is organized, how each part is built in SharePoint, and how the content stays current. The homepage prototype shows the design. Everything in it (names, codes, dates, counts) is sample content until the current-state inventory replaces it.

---

## 1. Outcomes

| Outcome | How we measure it |
| --- | --- |
| People find the right resource for a task in under a minute | Search click-through rate; searches with no result (PnP Modern Search and Microsoft Search insights) |
| Fewer "how do I…" support requests | D365 support requests tagged *how-to*, before and after launch |
| Content is trustworthy | Share of resources reviewed inside their review window (target 95%) |
| New users are productive faster | Completion of D365 Fundamentals and of the role path within 30 days of access |
| Changes reach the people they affect | Change-notice views and acknowledgment rate for mandatory notices |

## 2. Audiences

| Audience | What they come for | What the hub gives them |
| --- | --- | --- |
| Everyday D365 users (AP, AR, GL, procurement, expenses) | The steps for the task in front of them, right now | Search, procedure guides, QRGs, templates |
| New starters | Access, the basics, then their role | *Get set up in four steps*, D365 Fundamentals, role learning paths |
| Approvers and managers | Approve correctly and on time | Approver path, workflow QRG, change notices |
| Process owners (SMEs) | Publish and maintain their area's content | Authoring standards, review reminders, suggestion queue |
| D365 Training team | Run sessions, track mandatory training, keep content current | Training calendar, mandatory list, analytics, change notices |

## 3. Resource types

The four mandatory types are first-class. Each has a code prefix, a color in the design and its own metadata.

| Type | Code | Color | What it is | File | Type-specific metadata |
| --- | --- | --- | --- | --- | --- |
| Procedure guide | `PG` | Sky `#A7CFF8` | Step-by-step instructions for one task, a screenshot per step, the exact D365 menu path | Word → PDF (phase 1), SharePoint page (pilot) | Menu path, step count, security role, prerequisites |
| Quick reference guide | `QRG` | Violet `#B7B3FF` | One or two pages: statuses, codes, shortcuts, calendars | PDF | Page count |
| Recording | `REC` | Peach `#FFBF98` | Narrated walkthrough or session recap, chaptered to match the PG steps | MP4 in the library (plays in Stream) | Duration, chapters, transcript |
| Template | `TPL` | Mint `#C6FFD1` | The current upload template for D365, with a column guide on its first sheet | .xlsx | Data entity, import method, tested-in-D365 date, paired PG |

Supporting types: **change notice** (news post), **learning path** (list), **training session** (event), **FAQ** and **glossary term** (lists).

**Guide numbers** follow the existing D365 Procedure Guides library on the WTG - Atlas site: each business area owns a number range, and the file is named `<number>-<title> PG.pdf`, for example `301-Vendor Invoices PG.pdf`. The number never changes when the title does, so links, search and conversations stay stable. QRGs, recordings and templates take the number of the procedure guide they support.

| Range | Business area | Business Process Owner |
| --- | --- | --- |
| 100s | Acquire to Retire (A2R) | Sarah Ge, Joe Turner |
| 200s | Order to Cash (O2C) | Christopher Clarke |
| 300–302 | Procure to Pay (P2P) | Ghada Boulos |
| 303–304 | Procurement | Wayne Louys, Ghada Boulos |
| 398–399 | RCTI | Christopher Clarke, Ghada Boulos |
| 400s | Record to Report (R2R) | Sarah Ge, Joe Turner |

Business areas and owners come from the library's Business Area and BPO columns (October 2026).

## 4. Site map

```
Atlas Training Hub (Site Pages on the WTG - Atlas site)
├── Home
├── Procedure guides            library view, grouped by process area
├── Quick reference guides      library view
├── Recordings                  video gallery, grouped by process area and series
├── Templates                   template catalogue + "how to use templates safely"
├── Learning paths              one page per role: AP, AR, GL, Requester, Approver
├── What's changed              change notices (news), newest first
├── Training sessions           events calendar, recordings of past sessions
└── Support
    ├── FAQ
    ├── D365 glossary
    ├── Get help                support request, community channel, office hours
    └── Suggest a guide         Microsoft Forms → Suggestions list
Hidden for contributors: Authoring standards · PG/QRG/template masters · Review dashboard
```

Navigation is a mega menu with four groups: **Learn** (the four types), **By process area** (12 links into the pre-filtered library), **Learning paths**, **Support**.

## 5. Homepage, section by section

| # | Section | Its job | SharePoint build | Phase |
| --- | --- | --- | --- | --- |
| 1 | Hero: greeting, search, popular tasks | Get people from "I need to…" to a result in one step | SPFx *Hub hero*; fallback: native Hero + Search box | 1 (fallback), 2 (SPFx) |
| 1b | Resume card | Return people to the exact step they left | SPFx, reads the viewer's last-opened PG | 2 |
| 2 | Four resource types | Make the mandatory formats unmissable | Native Quick links, Button layout, custom icons | 1 |
| 3 | Action required | Make mandatory items and deadlines visible above the fold; hidden when nothing is due | Native List web part on *Mandatory Training*, filtered to [Me]; later Viva Learning assignments | 1 |
| 4 | Process areas | Browse by the part of D365 people work in | Native Quick links, Grid; each link opens the library pre-filtered | 1 |
| 5 | Training library explorer | Filter every resource by type, area and keyword | PnP Modern Search: verticals (tabs), box, filters, results with a custom layout | 1 |
| 6 | Learning paths by role | Show the right order to learn a role | Phase 1: Highlighted content filtered by Role. Phase 2: SPFx path web part with personal progress | 1 → 2 |
| 7 | Live sessions | Fill office hours and refreshers | Native Events web part on *Training Sessions* | 1 |
| 8 | Templates band | Stop people reusing stale templates | Native section (Strong background) + Text + Highlighted content filtered to the Template content type | 1 |
| 9 | What's changed | Tell people when a process changes and what was updated | Native News web part filtered to the *Change notice* category | 1 |
| 10 | New to D365? | Give new starters a four-step start | Native Text + Quick links | 1 |
| 11 | FAQ and Still stuck? | Answer the top questions; route the rest | Native Collapsible sections; Quick links; Microsoft Forms web part | 1 |
| 12 | Footer | Ownership, contributor links | Native site footer (Extended) | 1 |

Open the prototype and switch on **Build notes** (bottom-right) to see these annotations on the page itself.

## 6. Content model

### Training Library (one document library, four content types)

One library with shared site columns gives one search index, one set of filters and one review process. Content types separate the four formats.

| Column | Type | Applies to | Notes |
| --- | --- | --- | --- |
| Title | Text | All | Task-first wording: "Process a vendor invoice" |
| Document code | Text, unique, indexed | All | `PG-AP-014` |
| Process area | Managed metadata (*D365 Process Areas*) | All | Drives filters and navigation |
| Roles | Managed metadata, multi (*D365 Roles*) | All | Drives learning paths and "for your role" views |
| Process owner | Person | All | Accountable SME |
| Status | Choice: Current · Under review · Retired | All | Retired items leave search results |
| Last reviewed | Date | All | Shown on every card |
| Next review due | Calculated: Last reviewed + 180 days | All | Feeds the review dashboard |
| Related resources | Lookup to this library, multi | All | Powers "With it" links |
| Keywords | Text, multi-line | All | Synonyms people search with ("bill", "supplier") |
| D365 menu path | Text | PG | `Accounts payable › Invoices › Pending vendor invoices` |
| Steps | Number | PG | |
| Security role | Text | PG | Who can see the menus in the guide |
| Pages | Number | QRG | |
| Duration | Text | Recording | `18:42` |
| Chapters | Text, multi-line | Recording | One line per chapter, matched to PG steps |
| Data entity | Text | Template | `Vendors V2` |
| Import method | Choice: Data management · Open in Excel · Journal import | Template | |
| Tested in D365 on | Date | Template | Shown on every template card |
| Paired guide | Lookup | Template | The PG that explains the import |

Versioning: major versions on, content approval on, version shown in the file name and on page 1 of every PG.

### Search schema for PnP Modern Search

Map the crawled properties to refinable managed properties (site-collection search schema):

| Managed property | Column |
| --- | --- |
| `RefinableString00` | Process area |
| `RefinableString01` | Resource type (content type) |
| `RefinableString02` | Roles |
| `RefinableString03` | Document code |
| `RefinableString04` | Status |
| `RefinableDate00` | Last reviewed |

### Supporting lists

| List | Key columns |
| --- | --- |
| Learning Paths | Role, Order, Resource (lookup), Estimated minutes |
| Mandatory Training | Title, Assigned to (person or group), Due date, Resource, Status |
| Training Sessions | Events list: date, time zone, Teams link, presenter, process area |
| Suggestions | Details, Related resource, Process area, Status, Owner, Response date |
| FAQ | Question, Answer, Category, Order |
| Glossary | Term, Definition, Process area |

## 7. SharePoint build approach

**Site.** Communication site (full-width sections, site footer, Extended header), associated with the relevant hub.

**Branding.** Org theme in SharePoint Brand Center from the WiseTech Global Design System: WiseTech Blue `#1D1765` as the theme primary, Cobalt `#371EE1` for actions, Midnight `#141E30` and Sky `#A7CFF8` for section backgrounds. DM Sans and DM Mono uploaded as a Brand Center font package. Section backgrounds use the theme's Neutral, Soft and Strong variants.

**Three build tiers**

| Tier | Covers | Needs |
| --- | --- | --- |
| Native web parts | Quick links, Highlighted content, News, Events, List, Text, Collapsible sections, Forms, footer | Site owner rights |
| PnP Modern Search (open-source SPFx) | Library explorer: tabs, filters, keyword box, custom result layout | App catalog deployment and the search schema mapping above |
| Custom SPFx | Hub hero with resume card, learning-path progress, "for your role" personalization | App catalog, a developer, Microsoft Graph permissions for user profile and activity |

Phase 1 ships with native web parts plus PnP Modern Search. It delivers everything on the homepage except the resume card and personal path progress, which arrive with SPFx in phase 2.

**Homepage as a SharePoint HTML page (chosen route).** SharePoint now accepts uploaded HTML pages in Site Pages (preview October 2026, general availability mid-November to late December 2026). The homepage ships that way: [`sharepoint/atlas-training-hub.html`](../sharepoint/atlas-training-hub.html) is one self-contained file with the brand fonts embedded, every link set from one settings block, and no outside scripts. SharePoint renders it in a sandboxed frame below its own header and navigation, which sets these limits:

| Limit | Effect on the homepage |
| --- | --- |
| No data calls or APIs, no browser storage | No personal content: the greeting by name, resume card, path progress and Action required are removed |
| Content lives in the file | The library list, learning paths, sessions and change notices are data inside the page; refresh them from the library export, or move sessions and change notices to native Events and News pages |
| Forms cannot submit | Search runs on Enter and the button; suggestions go to a Microsoft Forms link |
| No comments, likes, news promotion, scheduling or co-authoring | Feedback goes through the suggestion form |
| Uploaded HTML does not take the site theme | The page carries the WiseTech Global design itself |

PnP Modern Search and SPFx remain the route for a live, personalized library later (phase 2).

**Procedure guides as pages.** "Resume at step 3" and deep links to a single step work best when a PG is a SharePoint page with an anchor per step. Phase 1 keeps PGs as Word and PDF for a fast migration. Phase 2 pilots the ten most-viewed PGs as pages and compares completion and feedback.

## 8. Authoring standards

**Procedure guide anatomy**

1. Header block: code, title, version, process owner, last reviewed, who it is for, security role, D365 menu path
2. Before you start: prerequisites and the data you need
3. Numbered steps, one action each, a screenshot with the click target highlighted
4. Check it worked: what the result looks like in D365
5. If something goes wrong: the common errors and what to do
6. Related: the QRG, recording and template that go with it

**QRG.** One or two pages of tables and lists (statuses, codes, shortcuts, calendars). No step-by-step instructions; those live in the PG.

**Recording.** Under 15 minutes where possible, chapters that match PG steps, captions and a transcript, PG code said and shown in the first 10 seconds.

**Template.** First sheet is the column guide (field, required, allowed values, example). Version in the file name and in cell A1. Tested in the D365 training environment before each publish.

**File names.** `<code> <title> v<version>.<ext>`, for example `PG-AP-014 Process a vendor invoice v3.2.pdf`.

**Accessibility.** Alt text on every screenshot, real headings in Word, tagged PDFs, captions on every recording.

## 9. Governance

| Activity | Rule |
| --- | --- |
| Ownership | Each process area has a named process owner; the D365 Training team owns the site |
| Review cycle | PGs and QRGs every six months; templates whenever the data entity or process changes |
| D365 service updates | Each service update triggers a check of affected areas and a change notice where behavior changed |
| Publishing | Draft → SME review → Training review → Publish (content approval on the library) |
| Retirement | Status = Retired hides an item from the hub's search results (query filter on `RefinableString04`); the file moves to the archive library |
| Change notices | Every process change gets a news post tagged *Change notice* that links each updated resource; mandatory ones also create an Action required item |
| Suggestions | Logged in the Suggestions list, routed to the process owner, answered within five business days |
| Reporting | Monthly: top resources, searches with no result, overdue reviews, suggestion turnaround |

## 10. Roadmap

| Phase | Scope |
| --- | --- |
| 0 · Discover (2 weeks) | Inventory the current hub, confirm process areas and roles, test the prototype with 5 to 8 users across roles |
| 1 · Launch (4 to 6 weeks) | Site, theme, Training Library and lists, metadata, migration of current content, homepage on native web parts and PnP Modern Search, mega menu, change notices |
| 2 · Personalize (4 weeks) | SPFx hub hero with resume card, learning-path progress, "for your role" defaults, PG-as-page pilot |
| 3 · Extend | Viva Learning assignments for mandatory training, a SharePoint agent (Copilot) grounded on the Training Library that answers with citations to PGs, links into the hub from inside D365 |

## 11. What the current-state inventory needs to answer

Send these and the prototype's sample content gets replaced with the real thing:

- [x] Current pages: Atlas home, Atlas Training Hub, D365 User Support Hub (from screenshots, 23 Oct 2026)
- [ ] Every current page, its purpose and its owner
- [x] D365 Procedure Guides: 30 guides with business area and BPO (from screenshots; one Procurement and one R2R guide were not visible)
- [x] Links: D365 Templates folder, FAQs page, D365 User Support Hub, D365 support form
- [ ] Folder or page locations for Briefing Sessions, Training Recordings and QRGs
- [ ] An export of the current libraries: title, type, process area, owner, last modified, file type
- [ ] The current navigation
- [ ] Usage: most-viewed pages and documents, top search terms
- [ ] The list of templates with their data entities and import methods
- [ ] The D365 apps in scope (Finance and Operations only, or Customer Engagement as well) and the role list
- [ ] Known pain points and feedback from users
- [ ] Platform constraints: Brand Center access, app catalog deployment (SPFx, PnP Modern Search), search schema mapping

## 12. Decisions to make

| Decision | Recommendation |
| --- | --- |
| One library or one per type | One library with four content types |
| PG format | Word → PDF at launch; pilot PG-as-page for the top ten |
| Personalization (resume card, path progress) | Build in phase 2 once the library and metadata are stable |
| Mandatory training tracking | Mandatory Training list at launch; Viva Learning if licensed |
| Library explorer | PnP Modern Search |

## Appendix: design system usage

The prototype is built on the **WiseTech Global Design System** (organization default): DM Sans for all text, DM Mono for codes, metadata and eyebrows, one 10px radius, hairline borders and no shadows, Cobalt for actions and links, WiseTech Blue and Midnight for brand surfaces, and line icons in WiseTech Blue on secondary-color tiles.

Hub-specific choices:

- **Resource type colors** are fixed across the site: PG Sky, QRG Violet, Recording Peach, Template Mint. They appear on icon tiles, badges and link chips, so a type reads the same everywhere.
- **Codes and menu paths are set in DM Mono** because they are system strings people match against D365.
- **Icons to add to the verified set:** `file-text` (QRG), `video` (recording), `file-sheet` (template), `arrow-right`, `chevron-right`, `chevron-down`, `download`, `play`, `help`, `star`, `share`, `pencil`. The prototype draws them at 24px with a 1.5 stroke to match.
