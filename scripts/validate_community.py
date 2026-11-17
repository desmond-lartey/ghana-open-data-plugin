"""Check every file in community/datasets/ before it is merged.

Run by .github/workflows/validate.yml. Each file must parse (JSON or YAML),
carry the required fields with sensible values, and contain no e-mail
addresses (contributors' addresses are never published).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TYPES = {"dataset", "article", "report", "map", "survey", "imagery", "election", "other"}
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def load(path: Path):
    text = path.read_text(encoding="utf-8")
    body = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#"))
    try:
        return json.loads(body), text
    except ValueError:
        import yaml  # noqa: PLC0415
        return yaml.safe_load(text), text


def problems(path: Path) -> list[str]:
    try:
        item, text = load(path)
    except Exception as exc:  # noqa: BLE001
        return [f"does not parse: {exc}"]
    if not isinstance(item, dict):
        return ["is not an object"]
    out = []
    for key in ("id", "item_type", "title", "creators", "licence"):
        if not item.get(key):
            out.append(f"missing {key}")
    if item.get("item_type") and item["item_type"] not in TYPES:
        out.append(f"unknown item_type {item['item_type']!r}")
    if item.get("creators") and not any(isinstance(c, dict) and (c.get("last") or c.get("name")) for c in item["creators"]):
        out.append("no creator has a name")
    doi = item.get("doi")
    if doi and not re.match(r"^10\.\d{4,9}/\S+$", str(doi)):
        out.append(f"DOI {doi!r} does not look like 10.xxxx/…")
    for f in item.get("files") or []:
        if not str((f or {}).get("url", "")).startswith("https://"):
            out.append(f"file {f!r} has no https address")
    if EMAIL.search(text):
        out.append("contains an e-mail address")
    return out


def main() -> int:
    files = sorted((ROOT / "community" / "datasets").glob("*.y*ml"))
    bad = 0
    for path in files:
        found = problems(path)
        if found:
            bad += 1
            print(f"✗ {path.relative_to(ROOT)}: " + "; ".join(found))
    print(f"{len(files)} file(s) checked, {bad} with problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
