"""Build the SharePoint HTML page and its preview.

    python3 tools/build.py [--preview PATH]

Reads sharepoint/src/d365-training-hub.html, embeds the WOFF2 fonts in sharepoint/fonts as base64
@font-face rules (SharePoint HTML pages run in a sandbox, so the page cannot rely on Google Fonts),
and writes sharepoint/d365-training-hub.html: the single file to upload to Site Pages.

With --preview, also writes a body-only copy for the Claude artifact preview, which supplies its own
document wrapper.
"""
import argparse
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "sharepoint" / "src" / "d365-training-hub.html"
FONTS = ROOT / "sharepoint" / "fonts"
OUT = ROOT / "sharepoint" / "d365-training-hub.html"
FONTS_MARKER = re.compile(r"^[ \t]*<!-- @fonts:.*?-->[ \t]*\n", re.M)

FACES = [
    ("DM Sans", 400, "DMSans-Regular.woff2"),
    ("DM Sans", 500, "DMSans-Medium.woff2"),
    ("DM Sans", 700, "DMSans-Bold.woff2"),
    ("DM Mono", 400, "DMMono-Regular.woff2"),
    ("DM Mono", 500, "DMMono-Medium.woff2"),
]


def font_css():
    rules = []
    for family, weight, file in FACES:
        data = base64.b64encode((FONTS / file).read_bytes()).decode("ascii")
        rules.append(
            f'@font-face{{font-family:"{family}";font-style:normal;font-weight:{weight};font-display:swap;'
            f'src:url(data:font/woff2;base64,{data}) format("woff2")}}'
        )
    return "<style>\n/* DM Sans and DM Mono, WiseTech Global brand typefaces (SIL Open Font License 1.1), Latin subset */\n" + "\n".join(rules) + "\n</style>\n"


def build_page():
    src = SRC.read_text(encoding="utf-8")
    page, count = FONTS_MARKER.subn(lambda m: font_css(), src)
    if count != 1:
        raise SystemExit(f"expected one @fonts marker in {SRC}, found {count}")
    OUT.write_text(page, encoding="utf-8")
    return page


def build_preview(page, path):
    head = re.search(r"<head>(.*?)</head>", page, re.S).group(1)
    body = re.search(r"<body>(.*?)</body>", page, re.S).group(1)
    head = re.sub(r'<meta (charset|name="viewport")[^>]*>\n?', "", head)
    head = head.replace("</title>", '</title>\n<meta name="claude:viewport-fit-sides" content="cover">', 1)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(head.strip() + "\n" + body.strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", type=pathlib.Path, help="also write the artifact preview fragment here")
    args = parser.parse_args()
    page = build_page()
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page.encode('utf-8')) / 1024:.0f} KB)")
    if args.preview:
        build_preview(page, args.preview)
        print(f"wrote {args.preview}")
