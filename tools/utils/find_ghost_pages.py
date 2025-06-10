#!/usr/bin/env python3
"""
find_ghost_pages_ruamel.py
Pin-point Markdown files that sit inside an MkDocs docs tree but are *not*
referenced by any “nav” entry (supports monorepo + docs_dir).

Requires:  ruamel.yaml   (pip install ruamel.yaml)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable, Set, Tuple

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import ScalarString

yaml = YAML(typ="rt")
yaml.preserve_quotes = True


# ─────────────────────────────────────────────────────────────────────────────
def _candidate_md(value: str, base_dir: Path, docs_root: Path) -> Path:
    """
    Resolve a nav reference to the on-disk Markdown file:
      1. <docs_root>/<value>  (normal MkDocs behaviour)
      2. <base_dir>/<value>   (fallback – handles non-standard layouts)
    """
    preferred = (docs_root / value).resolve()
    return preferred if preferred.exists() else (base_dir / value).resolve()


def _parse_nav(
    nav: list,
    base_dir: Path,
    docs_root: Path
) -> Tuple[Set[Path], Set[Path]]:
    """Return (referenced_md, included_mkdocs) for one nav tree."""
    referenced, includes = set(), set()

    def walk(items: Iterable):
        for item in items:
            if isinstance(item, dict):
                for _label, val in item.items():
                    if isinstance(val, (str, ScalarString)):
                        s = str(val)
                        if s.lower().endswith(".md"):
                            referenced.add(_candidate_md(s, base_dir, docs_root))
                        elif s.startswith("!include"):
                            inc = s.split("!include", 1)[1].strip()
                            includes.add((base_dir / inc).resolve())
                    elif isinstance(val, list):
                        walk(val)
            elif isinstance(item, list):
                walk(item)

    walk(nav)
    return referenced, includes


def _harvest(root_yaml: Path) -> Tuple[Set[Path], Set[Path]]:
    """
    Walk every linked mkdocs.yml and gather:
      referenced_md  – all Markdown paths explicitly mentioned in nav entries
      docs_roots     – the set of <base_dir>/<docs_dir> directories encountered
    """
    referenced, docs_roots = set(), set()
    queue, seen = {root_yaml.resolve()}, set()

    while queue:
        current = queue.pop()
        if current in seen:
            continue
        seen.add(current)

        try:
            data = yaml.load(current.open("r", encoding="utf-8")) or {}
        except Exception as err:
            sys.exit(f"[ERROR] Cannot parse {current}: {err}")

        base_dir = current.parent
        docs_dir = str(data.get("docs_dir", "docs")).lstrip("./\\")
        docs_root = (base_dir / docs_dir).resolve()
        if docs_root.is_dir():
            docs_roots.add(docs_root)

        nav = data.get("nav", [])
        refs, inc = _parse_nav(nav, base_dir, docs_root)
        referenced.update(refs)
        queue.update(inc - seen)

    return referenced, docs_roots


def main() -> None:
    ap = argparse.ArgumentParser(
        description="List Markdown files inside docs trees that are not "
                    "referenced from any MkDocs nav entry.")
    ap.add_argument("--root", required=True, type=Path,
                    help="Path to the top-level mkdocs.yml")
    args = ap.parse_args()

    root_yaml = args.root.resolve()
    if not root_yaml.is_file():
        sys.exit(f"[ERROR] {root_yaml} does not exist or is unreadable")

    referenced, docs_roots = _harvest(root_yaml)

    # Discover every *.md under the collected docs roots
    all_md: Set[Path] = set()
    for d in docs_roots:
        all_md.update(p.resolve() for p in d.rglob("*.md"))

    ghosts = sorted(all_md - referenced)

    print(f"Docs roots         : {len(docs_roots):>5}")
    print(f"Referenced pages   : {len(referenced):>5}")
    print(f"Markdown discovered: {len(all_md):>5}")
    print(f"Ghost pages        : {len(ghosts):>5}\n")

    if ghosts:
        for p in ghosts:
            print(p)          # absolute path
    else:
        print("None")


if __name__ == "__main__":
    main()