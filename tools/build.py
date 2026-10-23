"""Build the SharePoint HTML pages and their previews.

    python3 tools/build.py [--preview DIR]

For each page in sharepoint/src, embeds the WOFF2 fonts in sharepoint/fonts as base64 @font-face rules
and every src="images/..." or url("images/...") photo from sharepoint/images as a data URI (SharePoint
HTML pages run in a sandbox, so a page cannot rely on Google Fonts or on files next to it), then writes
sharepoint/<page>.html: the single file to upload to Site Pages.

With --preview, also writes a body-only copy of each page into DIR for the Claude artifact preview, which
supplies its own document wrapper.
"""
import argparse
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "sharepoint" / "src"
FONTS = ROOT / "sharepoint" / "fonts"
IMAGES = ROOT / "sharepoint" / "images"
OUT_DIR = ROOT / "sharepoint"
FONTS_MARKER = re.compile(r"^[ \t]*<!-- @fonts:.*?-->[ \t]*\n", re.M)
IMAGE_REF = re.compile(r'(src="|url\(")images/([\w.-]+)"')
IMAGE_TYPES = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp", ".svg": "image/svg+xml"}

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


def image_uri(match):
    file = IMAGES / match.group(2)
    if not file.is_file():
        raise SystemExit(f"missing image {file.relative_to(ROOT)}")
    data = base64.b64encode(file.read_bytes()).decode("ascii")
    return f'{match.group(1)}data:{IMAGE_TYPES[file.suffix.lower()]};base64,{data}"'


def build_page(src_path):
    src = src_path.read_text(encoding="utf-8")
    page, count = FONTS_MARKER.subn(lambda m: font_css(), src)
    if count != 1:
        raise SystemExit(f"expected one @fonts marker in {src_path}, found {count}")
    page = IMAGE_REF.sub(image_uri, page)
    out = OUT_DIR / src_path.name
    out.write_text(page, encoding="utf-8")
    return out, page


def build_preview(page, path):
    head = re.search(r"<head>(.*?)</head>", page, re.S).group(1)
    body = re.search(r"<body>(.*?)</body>", page, re.S).group(1)
    head = re.sub(r'<meta (charset|name="viewport")[^>]*>\n?', "", head)
    head = head.replace("</title>", '</title>\n<meta name="claude:viewport-fit-sides" content="cover">', 1)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(head.strip() + "\n" + body.strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", type=pathlib.Path, help="also write each page's artifact preview fragment into this folder")
    args = parser.parse_args()
    for src_path in sorted(SRC_DIR.glob("*.html")):
        out, page = build_page(src_path)
        print(f"wrote {out.relative_to(ROOT)} ({len(page.encode('utf-8')) / 1024:.0f} KB)")
        if args.preview:
            preview = args.preview / src_path.name
            build_preview(page, preview)
            print(f"wrote {preview}")
