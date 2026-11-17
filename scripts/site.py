"""Static HTML site from the repository markdown.

`python -m scripts.site` builds ~/.local/share/finance-site (FINANCE_SITE overrides), outside
the repository, and copies in ~/.local/share/finance-reports (FINANCE_REPORTS overrides);
templates and CSS are in site/. `python -m scripts.site --serve` builds, then
starts a local server on http://127.0.0.1:8765 unless one is already running.
"""
import argparse
import html
import os
import re
import shutil
import socket
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from string import Template

import markdown

REPO = Path(__file__).resolve().parent.parent
OUT = Path(os.environ["FINANCE_SITE"]).expanduser() if os.environ.get("FINANCE_SITE") \
    else Path.home() / ".local" / "share" / "finance-site"
# Generated reports kept outside git (e.g. backtest tearsheets); paths below the root mirror the repo.
REPORTS = Path(os.environ["FINANCE_REPORTS"]).expanduser() if os.environ.get("FINANCE_REPORTS") \
    else Path.home() / ".local" / "share" / "finance-reports"
HOST, PORT = "127.0.0.1", 8765
FOLDERS = ["portfolio", "research", "scout", "news", "trading", "tax", "legal", "journal", "roles"]
SKIP_DIRS = {"__pycache__", ".cache", "data"}

MENU = [("home", "Home", "index.html"), ("market", "Market", "market.html"), ("decisions", "Decisions", "decisions.html"),
        ("portfolio", "Portfolio", "portfolio/summary.html"), ("library", "Library", "library.html")]
GROUP_ORDER = ["portfolio", "tax", "legal", "research", "scout", "news", "trading", "journal"]
TEAM = "Team files"
# Files written for the sessions rather than the user; the Library lists them last, collapsed.
TEAM_FILES = re.compile(r"^(AGENTS|MAP|README|STATUS)\.md$|^roles/|(^|/)(sources|sources-notes)\.md$")
LONG_NOTE = 80       # lines; longer notes get a table of contents
LONG_TABLE = 50      # rows; longer tables are collapsed

MONTHS = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}
NUM = re.compile(
    r"^[~+\-]?\s*(?:Rs\.?|\$|EUR|USD|JPY|INR|HKD|GBP)?\s*[+\-]?\$?[0-9][0-9,]*(?:\.[0-9]+)?"
    r"\s*(?:%|L|Cr|k|x|bn|B|M|pts)?(?:\s*\([+\-]?[0-9.,]+%\))?$")


# ---------- repository ----------

def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, check=True).stdout


def notes() -> list[str]:
    """Repository-relative paths of every markdown note in scope."""
    found = [p.name for p in REPO.glob("*.md")]
    for folder in FOLDERS:
        for p in (REPO / folder).rglob("*.md"):
            rel = p.relative_to(REPO)
            if not any(part.startswith(".") or part in SKIP_DIRS for part in rel.parts):
                found.append(rel.as_posix())
    return sorted(found)


def last_modified(paths: list[str]) -> dict[str, date]:
    """Last commit date per file; files changed but not committed use the file time."""
    dates: dict[str, date] = {}
    when = None
    for line in git("log", "--format=%x01%cs", "--name-only", "--", "*.md").splitlines():
        if line.startswith("\x01"):
            when = date.fromisoformat(line[1:])
        elif line and line not in dates:
            dates[line] = when
    dirty = {line[3:].strip('"') for line in git("status", "--porcelain", "-uall").splitlines()}
    for p in paths:
        if p in dirty or p not in dates:
            dates[p] = date.fromtimestamp((REPO / p).stat().st_mtime)
    return dates


def group_of(path: str) -> str:
    """Library group: top folder, or top two folders for deeper notes; team files apart."""
    if TEAM_FILES.search(path):
        return TEAM
    parts = path.split("/")
    return "/".join(parts[:2]) if len(parts) > 2 else parts[0]


# ---------- markdown text helpers ----------

def plain(text: str) -> str:
    """Markdown inline text -> plain text."""
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`]{1,3}([^*_`]+)[*_`]{1,3}", r"\1", text)
    return re.sub(r"\s+", " ", text.replace("`", "")).strip()


def short(text: str, n: int = 170) -> str:
    return text if len(text) <= n else text[:n].rsplit(" ", 1)[0] + " ..."


def title_of(text: str, path: str) -> str:
    m = re.search(r"^# (.+)$", text, re.M)
    return plain(m.group(1)) if m else Path(path).stem


def sections(text: str, level: int = 2) -> list[tuple[str, str]]:
    """(heading, body) for each heading of the given level; the text before is heading ''."""
    out, head, buf = [], "", []
    mark = "#" * level + " "
    fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            fence = not fence
        if not fence and line.startswith(mark):
            out.append((head, "\n".join(buf)))
            head, buf = line[len(mark):].strip(), []
        else:
            buf.append(line)
    out.append((head, "\n".join(buf)))
    return out


def section(text: str, name: str, level: int = 2) -> str:
    for head, body in sections(text, level):
        if head.lower().startswith(name.lower()):
            return body
    return ""


def tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    """Markdown tables in text: (header cells, rows of cells), cells as raw markdown."""
    out, block = [], []
    for line in text.splitlines() + [""]:
        if line.strip().startswith("|"):
            block.append(line.strip())
            continue
        if len(block) >= 2:
            cells = [[c.strip() for c in row.strip("|").split("|")] for row in block]
            out.append((cells[0], [r for r in cells[2:]]))
        block = []
    return out


def first_sentence(text: str) -> str:
    """First sentence of the Summary, or of the first paragraph after the title."""
    summary = split_summary(text)
    body = summary[1] if summary else re.sub(r"^# .*$", "", text, count=1, flags=re.M)
    para = []
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "|", "```", "<")):
            if para:
                break
            continue
        if re.match(r"^([-*]|\d+\.)\s", s):
            if para:
                break
            para.append(re.sub(r"^([-*]|\d+\.)\s+", "", s))
            break
        para.append(s)
    txt = plain(" ".join(para))
    m = re.match(r"^(.+?[.!?])(\s|$)", txt)
    return short(m.group(1) if m else txt, 160)


PATH = r"`?([\w./\-]+\.md)(#[\w\-]+)?`?"


def clean(text: str, titles: dict[str, str] | None = None) -> str:
    """Repository paths -> nothing inside brackets (the details link replaces them), the note
    title elsewhere; brackets left empty are dropped."""
    text = re.sub(r"\([^()]*\)", lambda m: re.sub(r"[;,]?\s*" + PATH, "", m.group(0)), text)
    text = re.sub(PATH, lambda m: (titles or {}).get(m.group(1), ""), text)
    return re.sub(r"\s*\(\s*[;,]?\s*\)", "", text)


def sentences(text: str) -> list[str]:
    return [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", plain(text)) if x]


def sentence(text: str) -> str:
    parts = sentences(text)
    return short(parts[0], 260) if parts else ""


def first_text(body: str) -> str:
    """First paragraph or first list item of a markdown block."""
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if b and not b.startswith(("|", "#", "```")):
            return re.sub(r"^([-*]|\d+\.)\s+", "", b)
    return ""


def headed(text: str) -> list[tuple[str, str]]:
    """(heading, body up to the next heading) for headings of level 2-4."""
    out, head, buf = [], None, []
    for line in text.splitlines():
        m = re.match(r"^#{2,4}\s+(.*)", line)
        if m:
            if head is not None:
                out.append((head, "\n".join(buf)))
            head, buf = m.group(1), []
        elif head is not None:
            buf.append(line)
    if head is not None:
        out.append((head, "\n".join(buf)))
    return out


def amount(cell: str) -> float:
    m = re.search(r"-?[0-9][0-9,]*(?:\.[0-9]+)?", plain(cell))
    return float(m.group(0).replace(",", "")) if m else 0.0


def crore(rs: float) -> str:
    if rs >= 1e7:
        return f"Rs {rs / 1e7:.2f} Cr"
    return f"Rs {rs / 1e5:.1f} L" if rs >= 1e5 else f"Rs {rs:,.0f}"


def split_summary(text: str):
    """(before, summary, after) when the first h2 of the note is a Summary, else None."""
    parts = sections(text, 2)
    if len(parts) > 1 and re.match(r"^(\d+\.\s*)?summary\b", parts[1][0], re.I):
        rest = "\n".join(f"## {h}\n{b}" for h, b in parts[2:])
        return parts[0][1], f"## {parts[1][0]}\n{parts[1][1]}", rest
    return None


# ---------- dates ----------

def near_year(month: int, day: int, today: date) -> date | None:
    best = None
    for year in (today.year - 1, today.year, today.year + 1):
        try:
            d = date(year, month, day)
        except ValueError:
            continue
        if best is None or abs((d - today).days) < abs((best - today).days):
            best = d
    return best


def dates_in(text: str, today: date, short_form: bool = False) -> list[date]:
    """Dates in text, in order: 2026-11-18, 16-25 Nov 2026, Wed 18 Nov; MM-DD if short_form."""
    hits = []
    for m in re.finditer(r"\b(20\d\d)-(\d\d)-(\d\d)\b", text):
        try:
            hits.append((m.start(), date(int(m[1]), int(m[2]), int(m[3]))))
        except ValueError:
            pass
    for m in re.finditer(r"\b(\d{1,2})(?:\s*-\s*\d{1,2})?\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?"
                         r"(?:\s+(20\d\d))?\b", text, re.I):
        month, day = MONTHS[m[2].lower()], int(m[1])
        try:
            d = date(int(m[3]), month, day) if m[3] else near_year(month, day, today)
        except ValueError:
            d = None
        if d:
            hits.append((m.start(), d))
    if short_form:
        for m in re.finditer(r"(?<![\d\-])(0[1-9]|1[0-2])-([0-3]\d)(?![\d%\-])", text):
            d = near_year(int(m[1]), int(m[2]), today)
            if d:
                hits.append((m.start(), d))
    return [d for _, d in sorted(hits, key=lambda h: h[0])]


def pick(ds: list[date], today: date) -> date | None:
    """First date from today on, else the first date."""
    return next((d for d in ds if d >= today), ds[0] if ds else None)


def deadline(text: str, today: date) -> date | None:
    """First date from today on, ignoring dates in brackets (references such as "(Decisions 2026-11-15)")."""
    return next((d for d in dates_in(re.sub(r"\([^()]*\)", "", text), today) if d >= today), None)


def entries(text: str) -> list[tuple[int, str]]:
    """List items of a markdown block as (depth, text), wrapped lines joined."""
    out: list[tuple[int, str]] = []
    for line in text.splitlines():
        m = re.match(r"^(\s*)(?:[-*+]|\d+[a-z]?\.)\s+(.*)", line)
        if m:
            out.append((1 if m.group(1) else 0, m.group(2)))
        elif line.strip() and out:
            out[-1] = (out[-1][0], out[-1][1] + " " + line.strip())
    return out


def fmt(d: date | None) -> str:
    return d.strftime("%a %d %b") if d else "-"


# ---------- rendering ----------

def gh_slug(value: str, separator: str = "-") -> str:
    """GitHub-style heading anchors, so links such as feed.md#2026-11-14---india-ipo work."""
    value = re.sub(r"<[^>]+>", "", html.unescape(value)).strip().lower()
    value = re.sub(r"[^\w\- ]", "", value)
    return value.replace(" ", separator)


def normalise(text: str) -> str:
    """GitHub-flavoured habits -> python-markdown: blank line before lists and tables,
    nested list indent of 2-3 spaces -> 4."""
    # A blank line inside a table (rows on both sides, no new header) would split it in two.
    text = re.sub(r"(\n\|[^\n]*)\n[ \t]*\n(?=\|[^\n]*\n(?!\|[\s:|-]*-[\s:|-]*\n))", r"\1\n", text)
    out, stack, fence, in_list, prev = [], [], False, False, ""
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
            out.append(line)
            prev = line
            continue
        if fence:
            out.append(line)
            prev = line
            continue
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        is_item = bool(re.match(r"([-*+]|\d+\.)\s", stripped))
        is_row = stripped.startswith("|")
        prev_row = prev.lstrip().startswith("|")
        if is_item:
            if prev.strip() and not in_list and not re.match(r"\s*([-*+]|\d+\.)\s", prev):
                out.append("")
            while stack and stack[-1] > indent:
                stack.pop()
            if not stack or stack[-1] < indent:
                stack.append(indent)
            line = " " * (4 * (len(stack) - 1)) + stripped
            in_list = True
        elif not stripped:
            pass
        elif indent == 0 and (not prev.strip() or stripped.startswith("#") or is_row):
            in_list, stack = False, []
        if is_row and prev.strip() and not prev_row:
            out.append("")
        if not is_row and stripped and prev_row:
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


def md(text: str) -> markdown.Markdown:
    return markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list"],
        extension_configs={"toc": {"slugify": gh_slug, "toc_depth": "2-3"}})


def is_num(cell_html: str) -> bool:
    text = html.unescape(re.sub(r"<[^>]+>", "", cell_html)).replace("*", "").strip()
    return bool(text) and bool(NUM.match(text))


def fix_table(m: re.Match) -> str:
    table = m.group(0)
    rows = re.findall(r"<tr>(.*?)</tr>", table, re.S)
    grid = [re.findall(r"<(td|th)([^>]*)>(.*?)</\1>", r, re.S) for r in rows]
    ncols = max((len(r) for r in grid), default=0)
    body = [r for r in grid if r and r[0][0] == "td"]
    numeric = set()
    for c in range(ncols):
        vals = [r[c][2] for r in body if c < len(r) and r[c][2].strip()]
        if c > 0 and vals and sum(map(is_num, vals)) >= 0.6 * len(vals):
            numeric.add(c)

    def cell_tag(i: int, cell) -> str:
        tag, attrs, content = cell
        if i in numeric and (tag == "th" or is_num(content)):
            attrs = re.sub(r'\s*style="[^"]*"', "", attrs) + ' class="num"'
        return f"<{tag}{attrs}>{content}</{tag}>"

    for row, cells in zip(rows, grid):
        table = table.replace(f"<tr>{row}</tr>", "<tr>" + "".join(cell_tag(i, c) for i, c in enumerate(cells)) + "</tr>", 1)
    width = max((len(re.sub(r"<[^>]+>", "", r)) for r in rows), default=0)
    wide = " wide" if ncols >= 5 or width > 140 else ""
    out = f'<div class="tw{wide}">{table}</div>'
    if len(body) > LONG_TABLE:
        out = f"<details><summary>Table with {len(body)} rows (click to open)</summary>{out}</details>"
    return out


def fix_links(page_html: str, path: str, known: set[str]) -> str:
    here = Path(path).parent

    def href(m: re.Match) -> str:
        url = m.group(1)
        if re.match(r"^[a-z]+:|^#|^/", url):
            return m.group(0)
        url = re.sub(r"\.md(?=$|#)", ".html", url)
        return f'href="{url}"'

    page_html = re.sub(r'href="([^"]*)"', href, page_html)

    def code(m: re.Match) -> str:
        target, anchor = m.group(1), m.group(2) or ""
        for cand in (target, (here / target).as_posix()):
            cand = os.path.normpath(cand)
            if cand in known:
                rel = os.path.relpath(cand, here.as_posix() or ".")
                return f'<a href="{rel[:-3]}.html{anchor}">{m.group(0)}</a>'
        return m.group(0)

    # Bare repository paths in code spans become links; skip those already inside a link.
    parts = re.split(r"(<a\b.*?</a>)", page_html, flags=re.S)
    return "".join(p if p.startswith("<a") else re.sub(r"<code>([\w./\-]+\.md)(#[\w\-]+)?</code>", code, p)
                   for p in parts)


def render(text: str, path: str, known: set[str]) -> tuple[str, str]:
    """(html, toc html) of markdown text."""
    conv = md(text)
    out = conv.convert(normalise(text))
    out = re.sub(r"<table>.*?</table>", fix_table, out, flags=re.S)
    return fix_links(out, path, known), conv.toc


class Site:
    def __init__(self, today: date | None = None):
        self.today = today or date.today()
        self.paths = notes()
        self.known = set(self.paths)
        self.dates = last_modified(self.paths)
        self.text = {p: (REPO / p).read_text(encoding="utf-8", errors="replace") for p in self.paths}
        self.template = Template((REPO / "site" / "page.html").read_text())
        self.built = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.titles = {p: title_of(t, p) for p, t in self.text.items()}

    def title(self, p: str) -> str:
        return title_of(self.text[p], p)

    def page(self, out_rel: str, title: str, body: str, current: str, kind: str = "") -> None:
        root = "../" * out_rel.count("/")
        links = " ".join(f'<a href="{root}{u}"{" class=on" if s == current else ""}>{html.escape(t)}</a>'
                         for s, t, u in MENU)
        doc = self.template.substitute(title=html.escape(title), root=root, nav=links, body=body, built=self.built,
                                       kind=kind)
        dest = OUT / out_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(doc, encoding="utf-8")

    # ----- note pages -----

    def note(self, p: str) -> None:
        title = self.title(p)
        text = re.sub(r"^# .*\n?", "", self.text[p], count=1, flags=re.M)
        parts = split_summary(text)
        summary_html = ""
        if parts:
            text = parts[0] + "\n" + parts[2]
            summary_html = f'<div class="summary">{render(parts[1], p, self.known)[0]}</div>'
        body, toc = render(text, p, self.known)
        lines = self.text[p].count("\n") + 1
        root = "../" * p.count("/")
        group = group_of(p)
        meta = (f'<div class="page-meta">{self.dates[p]} | <code>{html.escape(p)}</code> | '
                f'<a href="{root}library.html#{gh_slug(group)}">Library: {html.escape(group)}</a></div>')
        toc_html = f'<details class="toc"><summary>Contents</summary>{toc}</details>' \
            if lines > LONG_NOTE and "<li>" in toc else ""
        current = "portfolio" if p == "portfolio/summary.md" else "library"
        self.page(p[:-3] + ".html", title, f"<h1>{html.escape(title)}</h1>\n{meta}\n{summary_html}{toc_html}{body}",
                  current)

    def ref(self, text: str) -> str | None:
        """Site link of the first repository note named in text (`path.md#anchor` or a markdown link)."""
        for m in re.finditer(r"([\w./\-]+\.md)(#[\w\-]+)?", text):
            path = os.path.normpath(m.group(1))
            if path in self.known:
                return path[:-3] + ".html" + (m.group(2) or "")
        return None

    # ----- what waits for the user (STATUS.md) -----

    def todo(self) -> tuple[list[dict], list[dict], list[dict]]:
        """(needed from you, dated actions, decisions) from STATUS.md "Needed from user" and "Next"."""
        status = self.text.get("STATUS.md", "")
        needed = [{"text": t, "href": self.ref(t) or "STATUS.html#needed-from-user"}
                  for _, t in entries(section(status, "Needed from user"))]
        items: list[list[str]] = []
        for depth, text in entries(section(status, "Next")):
            if depth == 0:
                items.append([text])
            elif items:
                items[-1].append(text)
        dated, decide = [], []
        for head, *subs in items:
            if not re.search(r"\buser\b", " ".join([head, *subs]), re.I):
                continue
            topic = re.split(r"[,(:]", plain(head))[0].strip()
            href = self.ref(head) or "STATUS.html#next"
            subs_dated = [(deadline(s, self.today), s) for s in subs]
            subs_dated = [(d, s) for d, s in subs_dated if d and not re.search(r"not chosen", s, re.I)]
            for d, s in subs_dated:
                dated.append({"date": d, "topic": topic, "text": s, "href": self.ref(s) or href})
            if not subs_dated:
                d = deadline(head, self.today)
                entry = {"date": d, "topic": "", "text": head, "href": href, "subs": subs}
                (dated if d else decide).append(entry)
        dated.sort(key=lambda e: e["date"])
        return needed, dated, decide

    def advice(self, href: str) -> tuple[str, list[str]]:
        """(recommendation, options) from the note a decision links to, when the note gives them."""
        path = href.split("#")[0][:-5] + ".md"
        text = self.text.get(path, "")
        rec, options = "", []
        m = re.search(r"^(?:\*\*)?(?:Proposal|Recommendation|Recommended|Do first)(?:\*\*)?:\s*(.+(?:\n(?![\n#|]).+)*)",
                      text, re.M | re.I)
        if m:
            rec = sentence(m.group(1))
        for head, body in headed(text):
            if not rec and re.search(r"recommend|proposal", head, re.I):
                rec = sentence(first_text(body))
            if not options and re.search(r"\boptions?\b", head, re.I):
                rows = [r for _, rs in tables(body) for r in rs]
                options = [short(plain(" - ".join(c for c in r[:2] if c)), 110) for r in rows] or \
                          [short(plain(t), 110) for d, t in entries(body) if d == 0]
        return rec, options[:5]

    # ----- home: weekly letter -----

    def point(self, sentence_html: str, href: str) -> str:
        return f'<li>{sentence_html} <a class="more" href="{href}">details</a></li>'

    def action_line(self, e: dict) -> str:
        """One sentence for a dated action: bold date, topic, the sentence that holds the date."""
        text = clean(re.sub(r"\s*\([^()]*Decisions[^()]*\)", "", e["text"]), self.titles)
        parts = sentences(text)
        s = next((x for x in parts if deadline(x, self.today)), parts[0] if parts else plain(text))
        lead = fmt(e["date"])
        m = re.match(r"^((?:about |by |before |from )?[^:]{0,30}\b20\d\d):\s*(.+)$", s, re.I)
        if m:
            lead, s = re.sub(r"\s*20\d\d$", "", m.group(1)), m.group(2)
        topic = f"{e['topic']}: " if e["topic"] else ""
        return f"<b>{html.escape(lead)}</b> - {html.escape(topic + s[:1].upper() + s[1:])}"

    # ----- embedding notes in root pages -----

    def embed(self, text: str, path: str) -> str:
        """HTML of markdown from note `path`, with links rebased for a page at the site root."""
        out = render(text, path, self.known)[0]
        base = str(Path(path).parent) if "/" in path else ""

        def rebase(m: re.Match) -> str:
            url = m.group(1)
            if not base or re.match(r"^[a-z]+:|^#|^/", url):
                return m.group(0)
            return f'href="{os.path.normpath(os.path.join(base, url))}"'

        return re.sub(r'href="([^"]*)"', rebase, out)

    def inline(self, text: str, path: str) -> str:
        return re.sub(r"^<p>|</p>$", "", self.embed(text, path).strip())

    def glossary(self) -> list[tuple[str, list[re.Pattern]]]:
        """(meaning, patterns of its names) per line of portfolio/glossary.md, longest names first."""
        terms = []
        for _, line in entries(self.text.get("portfolio/glossary.md", "")):
            head, sep, meaning = plain(line).partition(": ")
            if not sep:
                continue
            names = set()
            for n in re.split(r"\s*(?:/|\(|\))\s*", head):
                pieces = [x.strip() for x in n.split(",")]
                # "SCLX, SMNR, IONQ": codes; "Direct, Growth": everyday words, not matched alone.
                names.update(pieces if len(pieces) == 1 else [x for x in pieces if x.isupper()])
            pats = [re.compile(rf"\b{re.escape(n)}(?:s|es)?\b", 0 if n.isupper() else re.I)
                    for n in sorted((n for n in names if len(n) >= 2), key=len, reverse=True)]
            if pats:
                terms.append((meaning, pats))
        return sorted(terms, key=lambda t: -len(t[1][0].pattern))

    def explain(self, page_html: str) -> str:
        """Dotted underline with the glossary meaning on hover, at the first use of each term;
        not inside links, headings, labels or the collapsed intro."""
        terms, used = self.glossary(), set()
        out, skip = [], 0
        for part in re.split(r"(<[^>]+>)", page_html):
            tag = re.match(r"</?(\w+)", part) if part.startswith("<") else None
            if tag:
                if tag.group(1) in ("a", "h1", "h2", "h3", "abbr", "code", "span", "th", "dt", "details"):
                    skip += -1 if part.startswith("</") else 1
                out.append(part)
                continue
            if skip > 0 or not part.strip():
                out.append(part)
                continue
            spans: list[tuple[int, int, str]] = []
            for meaning, pats in terms:
                if meaning in used:
                    continue
                hits = [m for pat in pats for m in pat.finditer(part)
                        if all(m.end() <= s0 or m.start() >= e0 for s0, e0, _ in spans)]
                if hits:
                    m = min(hits, key=lambda h: h.start())
                    spans.append((m.start(), m.end(), meaning))
                    used.add(meaning)
            for s0, e0, meaning in sorted(spans, reverse=True):
                part = (part[:s0] + f'<abbr class="g" title="{html.escape(meaning, quote=True)}">'
                        + part[s0:e0] + "</abbr>" + part[e0:])
            out.append(part)
        return "".join(out)

    # ----- home: the plan -----

    def cards(self, body: str, kind: str, path: str) -> str:
        out = []
        for header, rows in tables(body):
            cols = [h.lower() for h in header]
            find = lambda *keys: next((n for n, h in enumerate(cols) if h.startswith(keys)), None)
            what, amt, where, when, why = find("what"), find("how much", "amount"), find("where"), \
                find("when"), find("why")
            for r in rows:
                cell = lambda n: r[n].strip() if n is not None and n < len(r) else ""
                if not any(cell(n) for n in range(1, len(r))):
                    out.append(f'<p class="cardnote">{self.inline(cell(0), path)}</p>')
                    continue
                name, _, desc = cell(what).partition(": ")
                facts = [(lbl, cell(n)) for lbl, n in (("How much", amt), ("Where", where), ("When", when)) if cell(n)]
                parts = [f'<span class="label {kind}">{kind.upper()}</span>',
                         f'<div class="what">{self.inline(name, path)}</div>']
                if desc:
                    parts.append(f'<div class="desc">{self.inline(desc, path)}</div>')
                if facts:
                    parts.append('<dl class="facts">' + "".join(
                        f"<dt>{lbl}</dt><dd>{self.inline(v, path)}</dd>" for lbl, v in facts) + "</dl>")
                if cell(why):
                    parts.append(f'<p class="why">{self.inline(cell(why), path)}</p>')
                out.append(f'<div class="card {kind}">{"".join(parts)}</div>')
        return "".join(out)

    def home(self) -> None:
        path = "portfolio/plan.md"
        text = self.text.get(path)
        if not text:
            self.page("index.html", "Home", '<h1>Your money plan</h1><p class="empty">Coming.</p>', "home", "home")
            return
        parts = {re.sub(r"^\d+\.\s*", "", h).lower(): b for h, b in sections(text, 2) if h}
        get = lambda key: next((b for h, b in parts.items() if key in h), "")
        intro = re.sub(r"^# .*\n?", "", sections(text, 2)[0][1], count=1, flags=re.M).strip()
        body = [f"<h1>{html.escape(self.title(path))}</h1>"]
        if intro:
            first, _, rest = intro.partition("\n")
            body.append(f'<p class="page-meta">{self.inline(first, path)}</p>')
            if rest.strip():
                body.append(f'<details class="about"><summary>Words and short names</summary>'
                            f'{self.embed(rest, path)}</details>')
        money = entries(get("money today"))
        if money:
            lis = "".join(f"<li>{self.inline(t, path)}</li>" for _, t in money[1:])
            body.append(f'<div class="moneybox"><h2>Your money today</h2>'
                        f'<p class="total">{self.inline(money[0][1], path)}</p><ul>{lis}</ul></div>')
        steps_block = next((b for h, b in parts.items() if re.match(r"(your )?next\b", h)), "")
        steps = [t for d, t in entries(steps_block) if d == 0]
        if steps:
            lis = []
            for t in steps:
                lead, sep, rest = t.partition(": ")
                lis.append(f"<li><b>{self.inline(lead, path)}</b>: {self.inline(rest, path)}</li>" if sep and len(lead) < 50
                           else f"<li>{self.inline(t, path)}</li>")
            body.append(f'<h2>Your next {len(steps)} steps</h2><ol class="steps">{"".join(lis)}</ol>')
        for key, kind in (("sell", "sell"), ("buy", "buy"), ("keep", "keep")):
            block = parts.get(key, "")
            if block:
                body.append(f"<h2>{key.capitalize()}</h2>{self.cards(block, kind, path)}")
        picture = get("one picture")
        if picture:
            body.append(f"<h2>The plan in one picture</h2>{self.embed(picture, path)}")
        later = get("not now")
        if later:
            body.append(f"<h2>Not now</h2>{self.embed(later, path)}")
        tail = re.search(r"^Details:.*$", steps_block, re.M)
        if tail:
            body.append(f'<p class="page-meta">{self.inline(tail.group(0), path)}</p>')
        body.append(f'<p class="page-meta">Plan note: <a href="{self.link(path)}">{html.escape(path)}</a>, '
                    f'{self.dates[path]}.</p>')
        self.page("index.html", "Home", self.explain("\n".join(body)), "home", "home")

    # ----- market -----

    def market(self) -> None:
        body = ["<h1>Market</h1>"]
        days = sorted((p for p in self.paths if re.fullmatch(r"news/market/20\d\d-\d\d-\d\d\.md", p)), reverse=True)
        if days:
            p = days[0]
            text = re.sub(r"^# .*\n?", "", self.text[p], count=1, flags=re.M)
            body.append(f'<p class="page-meta">{html.escape(Path(p).stem)} | <a href="{self.link(p)}">full note</a></p>')
            body.append(self.embed(text, p))
        else:
            body.append('<p class="empty">Market note (news/market/&lt;date&gt;.md): coming.</p>')
        body.append("<h2>What to buy</h2>")
        p = "scout/buy-list.md"
        if p in self.known:
            text = re.sub(r"^# .*\n?", "", self.text[p], count=1, flags=re.M)
            body.append(f'<p class="page-meta">{self.dates[p]} | <a href="{self.link(p)}">full note</a></p>')
            body.append(self.embed(text.replace("\n### ", "\n#### ").replace("\n## ", "\n### "), p))
        else:
            body.append('<p class="empty">Buy list (scout/buy-list.md): coming.</p>')
        body.append("<h2>Sectors</h2>")
        sectors: dict[str, list[str]] = {}
        for q in self.paths:
            m = re.match(r"research/sectors/([^/]+)/", q)
            if m:
                sectors.setdefault(m.group(1), []).append(q)
        lis = []
        for name in sorted(sectors):
            qs = sectors[name]
            main = next((q for q in qs if Path(q).stem.lower() in ("index", "readme")), sorted(qs)[0])
            line = first_sentence(self.text[main])
            lis.append(f'<li><a href="{self.link(main)}">{html.escape(self.title(main))}</a>'
                       f'{" - " + html.escape(line) if line else ""}</li>')
        body.append(f'<ul class="letter">{"".join(lis)}</ul>' if lis
                    else '<p class="empty">Sector notes (research/sectors/): coming.</p>')
        self.page("market.html", "Market", "\n".join(body), "market")


    # ----- decisions -----

    def decisions(self, needed, dated, decide) -> None:
        body = ["<h1>Decisions</h1>",
                '<p class="page-meta">Everything waiting for you, from <a href="STATUS.html">STATUS.md</a>.</p>']
        body.append("<h2>Needed from you</h2>")
        body.append('<ul class="letter">' + "".join(self.point(html.escape(plain(clean(e["text"], self.titles))), e["href"])
                                                    for e in needed) + "</ul>")
        body.append("<h2>With a date</h2>")
        body.append('<ul class="letter">' + "".join(self.point(self.action_line(e), e["href"]) for e in dated) + "</ul>")
        body.append("<h2>To decide</h2>")
        for e in decide:
            rec, options = self.advice(e["href"]) if e["href"].endswith(".html") or ".html#" in e["href"] else ("", [])
            parts = [f'<p>{html.escape(short(plain(clean(e["text"], self.titles)), 400))}</p>']
            if options:
                parts.append("<p><b>Options:</b></p><ul>" + "".join(f"<li>{html.escape(o)}</li>" for o in options) + "</ul>")
            if rec:
                parts.append(f"<p><b>Recommended:</b> {html.escape(rec)}</p>")
            parts.append(f'<p><a class="more" href="{e["href"]}">details</a></p>')
            body.append(f'<div class="decision">{"".join(parts)}</div>')
        self.page("decisions.html", "Decisions", "\n".join(body), "decisions")

    # ----- library -----

    def link(self, p: str) -> str:
        return p[:-3] + ".html"

    def library(self) -> None:
        groups: dict[str, list[str]] = {}
        for p in self.paths:
            groups.setdefault(group_of(p), []).append(p)

        def order(g: str) -> tuple:
            top = g.split("/")[0]
            return (g == TEAM, GROUP_ORDER.index(top) if top in GROUP_ORDER else len(GROUP_ORDER), g)

        def note_order(p: str) -> tuple:
            return (Path(p).stem.lower() not in ("index", "readme"), -self.dates[p].toordinal(), p)

        body = ["<h1>Library</h1>",
                '<p><input id="q" type="search" placeholder="Filter, e.g. QCOM, tax, estate" autocomplete="off"></p>']
        for g in sorted(groups, key=order):
            ps = sorted(groups[g], key=note_order)
            lis = []
            for p in ps:
                sub = str(Path(p).parent)
                sub = sub[len(g) + 1:] if sub.startswith(g + "/") else ""
                meta = " | ".join(x for x in (sub, str(self.dates[p])) if x)
                lis.append(f'<li><a href="{self.link(p)}">{html.escape(self.title(p))}</a> '
                           f'<span class="meta">{html.escape(meta)}</span><span hidden>{html.escape(p)}</span></li>')
            body.append(f'<details class="group" id="{gh_slug(g)}"><summary>{html.escape(g)} '
                        f'<span class="meta">({len(ps)})</span></summary><ul class="lib">{"".join(lis)}</ul></details>')
        body.append("""<script>
document.getElementById("q").addEventListener("input", function () {
  var q = this.value.toLowerCase().trim();
  document.querySelectorAll("details.group").forEach(function (d) {
    var n = 0;
    d.querySelectorAll("li").forEach(function (li) {
      var hit = !q || li.textContent.toLowerCase().indexOf(q) >= 0;
      li.hidden = !hit; if (hit) n++;
    });
    d.hidden = q && !n; d.open = !!q && n > 0;
  });
});
if (location.hash) { var g = document.getElementById(location.hash.slice(1)); if (g) g.open = true; }
</script>""")
        self.page("library.html", "Library", "\n".join(body), "library")

    def build(self) -> None:
        if OUT.exists():
            if OUT == Path.home() or REPO in OUT.parents or OUT == REPO:
                raise SystemExit(f"refusing to clear {OUT}")
            shutil.rmtree(OUT)
        OUT.mkdir(parents=True)
        if REPORTS.is_dir():
            shutil.copytree(REPORTS, OUT, dirs_exist_ok=True)
        shutil.copy(REPO / "site" / "style.css", OUT / "style.css")
        for p in self.paths:
            self.note(p)
        for folder in FOLDERS:
            for f in [*(REPO / folder).rglob("*.csv"), *(REPO / folder).rglob("*.html")]:
                dest = OUT / f.relative_to(REPO)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(f, dest)
        self.home()
        self.market()
        self.decisions(*self.todo())
        self.library()
        print(f"{len(self.paths)} notes -> {OUT}")


def serve() -> None:
    """Start the local server in the background unless something already listens on PORT."""
    url = f"http://{HOST}:{PORT}"
    with socket.socket() as sock:
        sock.settimeout(1)
        if sock.connect_ex((HOST, PORT)) == 0:
            print(f"server already running: {url}")
            return
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(PORT), "--bind", HOST, "--directory", str(OUT)],
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        start_new_session=True)
    print(f"server started: {url} (pid {proc.pid})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the notes website.")
    parser.add_argument("--serve", action="store_true", help=f"also serve it on http://{HOST}:{PORT}")
    args = parser.parse_args()
    Site().build()
    if args.serve:
        serve()
