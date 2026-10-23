# sharepoint-training-hub

Planning and design for the **D365 Training Hub**, WiseTech Global's SharePoint site for Dynamics 365 procedure guides (PGs), quick reference guides (QRGs), recordings and templates.

| Path | What it is |
| --- | --- |
| [`docs/PLAN.md`](docs/PLAN.md) | The plan: outcomes, audiences, resource types, site map, homepage sections, content model, SharePoint build approach, governance, roadmap and open decisions |
| [`prototype/home.html`](prototype/home.html) | High-fidelity, interactive homepage prototype on the WiseTech Global Design System. Live preview: https://claude.ai/artifact/JaF5CzfGopBHiwbvLhaFMm (private; share it from the page's Share menu) |

## The prototype

`prototype/home.html` is a page fragment published as a Claude artifact, which adds the document wrapper. To open it locally, wrap it first:

```sh
{ printf '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>'; cat prototype/home.html; printf '</body></html>'; } > /tmp/d365-hub.html
```

Then open `/tmp/d365-hub.html` in a browser.

What works in it:

- Search from the hero or the suite bar, the popular-task chips, the format cards and the process-area tiles all filter the library explorer
- Library tabs, keyword filter, process-area filter, sort and "Show more"
- Role tabs in Learning paths
- FAQ accordion
- **Build notes** toggle (bottom-right): labels every section with the SharePoint web part that builds it (Native, PnP Modern Search or SPFx)

All names, document codes, dates and counts are sample content.
