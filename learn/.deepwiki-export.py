from __future__ import annotations

import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from markdownify import markdownify


BASE = "https://deepwiki.com"
REPOSITORY_PATH = "/deepseek-ai/deepseek-harness"
OUTPUT = Path("learn/deepwiki")


def fetch(path: str) -> str:
    request = Request(urljoin(BASE, path), headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def page_paths(index_html: str) -> list[str]:
    soup = BeautifulSoup(index_html, "html.parser")
    paths = {
        anchor["href"]
        for anchor in soup.find_all("a", href=True)
        if anchor["href"].startswith(f"{REPOSITORY_PATH}/")
    }
    return sorted(paths, key=lambda path: [int(piece) if piece.isdigit() else piece for piece in re.split(r"([0-9]+)", path)])


def convert(html: str, source_url: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("div.prose-custom.prose-custom-md")
    if content is None:
        raise RuntimeError(f"Could not find article content in {source_url}")
    title = content.find("h1").get_text(" ", strip=True)
    for anchor in content.find_all("a", href=True):
        href = anchor["href"]
        if href.startswith(REPOSITORY_PATH):
            anchor["href"] = f"./{href.rsplit('/', 1)[-1]}.md"
        elif href.startswith("/"):
            anchor["href"] = urljoin(BASE, href)
    body = markdownify(str(content), heading_style="ATX", bullets="-").strip()
    preamble = f"<!-- Source: {source_url}; extracted 2026-09-24 -->\n\n"
    return title, preamble + body + "\n"


def main() -> None:
    index_html = Path("/tmp/deepwiki-harness.html").read_text()
    pages = page_paths(index_html)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    entries: list[tuple[str, str]] = []
    for number, path in enumerate(pages, start=1):
        html = index_html if path.endswith("/1-overview") else fetch(path)
        title, document = convert(html, urljoin(BASE, path))
        filename = f"{path.rsplit('/', 1)[-1]}.md"
        (OUTPUT / filename).write_text(document)
        entries.append((title, filename))
        print(f"[{number}/{len(pages)}] {filename}", flush=True)
        time.sleep(0.15)
    readme = "# DeepWiki export: deepseek-harness\n\n"
    readme += "Source: <https://deepwiki.com/deepseek-ai/deepseek-harness>  \n"
    readme += "Extracted: 2026-09-24\n\n"
    readme += "This is a point-in-time export of DeepWiki's generated documentation. It is not authoritative repository documentation.\n\n"
    readme += "## Contents\n\n"
    readme += "".join(f"- [{title}](./{filename})\n" for title, filename in entries)
    (OUTPUT / "README.md").write_text(readme)


if __name__ == "__main__":
    main()
