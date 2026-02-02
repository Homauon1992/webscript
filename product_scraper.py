import csv
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


class LinkHeadingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.results: list[dict[str, str]] = []
        self._current_tag: str | None = None
        self._current_href: str = ""
        self._current_text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"a", "h1", "h2", "h3"}:
            self._current_tag = tag
            self._current_text_parts = []
            self._current_href = ""
            if tag == "a":
                for key, value in attrs:
                    if key == "href" and value:
                        self._current_href = value
                        break

    def handle_data(self, data: str) -> None:
        if self._current_tag:
            text = data.strip()
            if text:
                self._current_text_parts.append(text)

    def handle_endtag(self, tag: str) -> None:
        if self._current_tag == tag:
            text = " ".join(self._current_text_parts).strip()
            if text:
                entry = {
                    "type": "link" if tag == "a" else "heading",
                    "tag": tag,
                    "text": text,
                    "href": self._current_href,
                }
                self.results.append(entry)
            self._current_tag = None
            self._current_href = ""
            self._current_text_parts = []


def validate_url(url: str) -> None:
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError("URL must include scheme and host (e.g., https://example.com).")


def fetch_html(url: str, timeout_seconds: int) -> str:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=timeout_seconds) as response:
        return response.read().decode("utf-8", errors="replace")


def save_csv(rows: list[dict[str, str]], output_path: str) -> None:
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["type", "tag", "text", "href"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    url = input("Enter your link or website: ").strip()
    if not url:
        print("No URL provided.")
        return

    try:
        validate_url(url)
        html = fetch_html(url, timeout_seconds=10)
    except (ValueError, HTTPError, URLError, TimeoutError) as exc:
        print(f"Failed to fetch URL: {exc}")
        return

    parser = LinkHeadingParser()
    parser.feed(html)
    save_csv(parser.results, "scraped_content.csv")
    print(f"Saved {len(parser.results)} items to scraped_content.csv")


if __name__ == "__main__":
    main()
