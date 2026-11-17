"""Fill the community catalogue page from community/datasets/*.yml.

The review team approves datasets in the portal; each approval writes one
file to community/datasets/ in this repository. This hook turns them into
the list on docs/share/catalogue.md when the site is built.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARK = "<!-- community-catalogue -->"


def _load(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    body = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#"))
    try:
        return json.loads(body)  # the portal writes JSON, which is also YAML
    except ValueError:
        try:
            import yaml  # noqa: PLC0415 - only for hand-written entries
            return yaml.safe_load(text)
        except Exception:  # noqa: BLE001 - a broken file must not break the site
            return None


def _entries() -> list[dict]:
    items = []
    for path in sorted((ROOT / "community" / "datasets").glob("*.y*ml")):
        item = _load(path)
        if isinstance(item, dict) and item.get("title"):
            items.append(item)
    items.sort(key=lambda i: str(i.get("approved_at") or ""), reverse=True)
    return items


def _creators(item: dict) -> str:
    names = []
    for c in item.get("creators") or []:
        if isinstance(c, dict):
            names.append(" ".join(p for p in (c.get("first"), c.get("last"), c.get("name")) if p))
        elif c:
            names.append(str(c))
    return ", ".join(n for n in names if n)


def _card(item: dict) -> str:
    esc = html.escape
    title = esc(str(item.get("title")))
    meta = " · ".join(esc(str(x)) for x in (item.get("item_type"), item.get("licence"), (item.get("date_published") or "")[:10]) if x)
    by = _creators(item)
    lines = [f"### {title}", "", f"*{meta}*" if meta else "", ""]
    if by:
        lines += [f"**By** {esc(by)}" + (f", shared by {esc(str(item['contributor']))}" if item.get("contributor") else ""), ""]
    if item.get("abstract"):
        lines += [esc(str(item["abstract"]))[:600], ""]
    links = []
    if item.get("doi"):
        links.append(f"[DOI {esc(item['doi'])}](https://doi.org/{esc(item['doi'])})")
    if item.get("url"):
        links.append(f"[Original source]({esc(item['url'])})")
    for f in item.get("files") or []:
        if isinstance(f, dict) and f.get("url"):
            links.append(f"[{esc(str(f.get('name') or 'File'))}]({esc(f['url'])})")
    if links:
        lines += [" · ".join(links), ""]
    return "\n".join(lines)


def on_page_markdown(markdown: str, page, config, files) -> str:  # noqa: ARG001 - MkDocs hook signature
    if MARK not in markdown:
        return markdown
    items = _entries()
    if not items:
        body = "!!! info \"No community datasets yet\"\n    The first approved submissions will appear here."
    else:
        body = f"{len(items)} dataset{'s' if len(items) != 1 else ''} shared by the community and approved by the review team.\n\n" + "\n---\n\n".join(_card(i) for i in items)
    return markdown.replace(MARK, body)
