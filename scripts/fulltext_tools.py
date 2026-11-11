#!/usr/bin/env python3
"""Full-text helpers for the DMIC research sessions (stdlib + httpx for LlamaParse).

Subcommands
-----------
pmc <PMCID|PMID> --role ROLE
    Fetch open full text as JATS XML from NCBI E-utilities (official API, no browser
    spoofing), convert to Markdown, write literature/parsed/ROLE/<id>.md and a receipt.
llamaparse <pdf> --role ROLE
    Parse a local PDF with the LlamaParse REST API (key from $LLAMA_CLOUD_API_KEY or the
    file in $LLAMA_CLOUD_API_KEY_FILE, default ~/.config/llamaparse/api_key). The markdown
    is written to disk; only a short receipt is printed, so it never floods the session.
verify <md> --title "..." [--author Surname] [--year YYYY]
    Pollution check: confirm title words / first author / year occur in the first 6000 chars.
grep <role> <pattern>
    Case-insensitive search over literature/parsed/ROLE/*.md with filename:line output.

Outputs under literature/fulltext/ and literature/parsed/ are git-ignored (copyright).
Receipts under literature/receipts/ are committed (no text, only hashes and ids).
Run with ~/llamaparse-mcp/.venv/bin/python for the `llamaparse` command (needs httpx).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
LP_BASE = "https://api.cloud.llamaindex.ai/api/v1/parsing"
UA = "dmic-research-fulltext-tool/1.0"


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def receipt(role: str, rec: dict) -> None:
    out = ROOT / "literature" / "receipts"
    out.mkdir(parents=True, exist_ok=True)
    rec = {"time": now(), **rec}
    with (out / f"{role}.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def http_get(url: str, tries: int = 3) -> bytes:
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET failed: {url}: {last}")


# ---------------------------------------------------------------- PMC JATS -> md
def _txt(el: ET.Element) -> str:
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def jats_to_md(xml_bytes: bytes) -> str:
    root = ET.fromstring(xml_bytes)
    art = root.find(".//article")
    if art is None:
        art = root
    lines: list[str] = []
    title = art.find(".//article-title")
    if title is not None:
        lines.append(f"# {_txt(title)}\n")
    jt = art.find(".//journal-title")
    if jt is not None:
        lines.append(f"Journal: {_txt(jt)}\n")
    names = [f"{_txt(s)}" for s in art.findall(".//contrib-group/contrib/name/surname")]
    if names:
        lines.append("Authors: " + ", ".join(names[:12]) + "\n")
    yrs = [_txt(y) for y in art.findall(".//pub-date/year")]
    if yrs:
        lines.append("Year: " + ", ".join(sorted(set(yrs))) + "\n")
    for aid in art.findall(".//article-id"):
        lines.append(f"{aid.get('pub-id-type')}: {_txt(aid)}")
    lines.append("")
    ab = art.find(".//abstract")
    if ab is not None:
        lines.append("## Abstract\n")
        lines.append(_txt(ab) + "\n")

    def walk(sec: ET.Element, depth: int) -> None:
        t = sec.find("title")
        if t is not None:
            lines.append("#" * min(depth + 1, 6) + " " + _txt(t) + "\n")
        for ch in sec:
            if ch.tag == "p":
                lines.append(_txt(ch) + "\n")
            elif ch.tag == "sec":
                walk(ch, depth + 1)
            elif ch.tag in ("table-wrap", "fig"):
                cap = ch.find("caption")
                label = ch.find("label")
                head = " ".join(x for x in [_txt(label) if label is not None else "", _txt(cap) if cap is not None else ""] if x)
                lines.append(f"**{head}**\n")
                for tr in ch.findall(".//tr"):
                    cells = [_txt(c) for c in tr if c.tag in ("td", "th")]
                    lines.append("| " + " | ".join(cells) + " |")
                lines.append("")

    body = art.find(".//body")
    if body is not None:
        walk(body, 1)
    else:
        lines.append("_[No body in XML: full text not in PMC open subset]_\n")
    refs = art.findall(".//ref-list/ref")
    if refs:
        lines.append("## References\n")
        for i, r in enumerate(refs, 1):
            ids = {p.get("pub-id-type"): _txt(p) for p in r.iter("pub-id")}
            lines.append(f"{i}. {_txt(r)} {('PMID:' + ids['pmid']) if 'pmid' in ids else ''} {('DOI:' + ids['doi']) if 'doi' in ids else ''}".rstrip())
    return "\n".join(lines) + "\n"


def cmd_pmc(a: argparse.Namespace) -> int:
    ident = a.id.strip()
    if ident.isdigit():  # PMID -> PMCID
        # NOTE: do not use elink pubmed->pmc: it can return PMC articles that *cite* the PMID.
        # esummary articleids lists the article's own PMCID (if any).
        data = json.loads(http_get(f"{EUTILS}/esummary.fcgi?db=pubmed&id={ident}&retmode=json"))
        try:
            ids = data["result"][ident]["articleids"]
            pmcid = next(x["value"] for x in ids if x.get("idtype") == "pmc")
            pmcid = pmcid if pmcid.upper().startswith("PMC") else "PMC" + pmcid
        except (KeyError, IndexError, StopIteration):
            receipt(a.role, {"cmd": "pmc", "id": ident, "status": "no_pmc_record"})
            print(f"NO_PMC pmid={ident}")
            return 2
    else:
        pmcid = ident.upper()
    xml = http_get(f"{EUTILS}/efetch.fcgi?db=pmc&id={pmcid}&rettype=xml")
    md = jats_to_md(xml)
    body_ok = "No body in XML" not in md
    out = ROOT / "literature" / "parsed" / a.role
    out.mkdir(parents=True, exist_ok=True)
    f = out / f"{pmcid}.md"
    f.write_text(md, encoding="utf-8")
    receipt(a.role, {"cmd": "pmc", "id": ident, "pmcid": pmcid, "bytes_xml": len(xml), "chars_md": len(md),
                     "has_body": body_ok, "sha256_md": sha256(f), "path": str(f.relative_to(ROOT))})
    print(f"{'OK' if body_ok else 'ABSTRACT_ONLY'} {f.relative_to(ROOT)} chars={len(md)}")
    return 0 if body_ok else 3


# ---------------------------------------------------------------- LlamaParse
def lp_key() -> str:
    k = os.environ.get("LLAMA_CLOUD_API_KEY", "").strip()
    if k:
        return k
    p = Path(os.environ.get("LLAMA_CLOUD_API_KEY_FILE", "~/.config/llamaparse/api_key")).expanduser()
    return p.read_text().strip() if p.is_file() else ""


def cmd_llamaparse(a: argparse.Namespace) -> int:
    import httpx  # noqa: PLC0415

    pdf = Path(a.pdf).expanduser().resolve()
    if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
        print("ERROR not a pdf file")
        return 1
    key = lp_key()
    if not key:
        print("ERROR no LlamaParse key (set LLAMA_CLOUD_API_KEY or key file)")
        return 1
    h = {"Authorization": f"Bearer {key}", "Accept": "application/json"}
    with httpx.Client(timeout=120) as c:
        r = c.post(f"{LP_BASE}/upload", headers=h, files={"file": (pdf.name, pdf.read_bytes(), "application/pdf")})
        r.raise_for_status()
        job = r.json()["id"]
        t0, wait = time.monotonic(), 2.0
        while True:
            s = c.get(f"{LP_BASE}/job/{job}", headers=h)
            s.raise_for_status()
            st = str(s.json().get("status", "")).upper()
            if st == "SUCCESS":
                break
            if st in {"ERROR", "FAILED", "CANCELLED"}:
                receipt(a.role, {"cmd": "llamaparse", "pdf": pdf.name, "job": job, "status": st})
                print(f"FAILED job={job} {st}")
                return 4
            if time.monotonic() - t0 > 900:
                print(f"TIMEOUT job={job}")
                return 5
            time.sleep(wait)
            wait = min(wait * 1.6, 15)
        md = c.get(f"{LP_BASE}/job/{job}/result/markdown", headers=h)
        md.raise_for_status()
        text = md.json().get("markdown", "")
    out = ROOT / "literature" / "parsed" / a.role
    out.mkdir(parents=True, exist_ok=True)
    f = out / (pdf.stem + ".md")
    f.write_text(text, encoding="utf-8")
    receipt(a.role, {"cmd": "llamaparse", "pdf": pdf.name, "sha256_pdf": sha256(pdf), "job": job,
                     "chars_md": len(text), "sha256_md": sha256(f), "path": str(f.relative_to(ROOT))})
    print(f"OK {f.relative_to(ROOT)} chars={len(text)} job={job}")
    return 0


# ---------------------------------------------------------------- verify / grep
def cmd_verify(a: argparse.Namespace) -> int:
    head = Path(a.md).read_text(encoding="utf-8", errors="ignore")[:6000].lower()
    words = [w for w in re.findall(r"[a-z0-9]{5,}", a.title.lower())]
    hit = sum(w in head for w in words)
    ratio = hit / max(len(words), 1)
    ok_title = ratio >= 0.6
    ok_author = (a.author.lower() in head) if a.author else True
    ok_year = (a.year in head) if a.year else True
    verdict = "PASS" if (ok_title and ok_author and ok_year) else "POLLUTED_OR_MISMATCH"
    print(f"{verdict} title_hit={hit}/{len(words)} author={ok_author} year={ok_year} file={a.md}")
    return 0 if verdict == "PASS" else 6


def cmd_grep(a: argparse.Namespace) -> int:
    pat = re.compile(a.pattern, re.I)
    d = ROOT / "literature" / "parsed" / a.role
    n = 0
    for f in sorted(d.glob("*.md")):
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if pat.search(line):
                print(f"{f.name}:{i}: {line[:220]}")
                n += 1
    print(f"-- {n} matches")
    return 0 if n else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pmc"); p.add_argument("id"); p.add_argument("--role", required=True); p.set_defaults(fn=cmd_pmc)
    p = sub.add_parser("llamaparse"); p.add_argument("pdf"); p.add_argument("--role", required=True); p.set_defaults(fn=cmd_llamaparse)
    p = sub.add_parser("verify"); p.add_argument("md"); p.add_argument("--title", required=True)
    p.add_argument("--author", default=""); p.add_argument("--year", default=""); p.set_defaults(fn=cmd_verify)
    p = sub.add_parser("grep"); p.add_argument("role"); p.add_argument("pattern"); p.set_defaults(fn=cmd_grep)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
