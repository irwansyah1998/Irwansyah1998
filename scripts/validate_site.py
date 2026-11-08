#!/usr/bin/env python3
"""Check static portfolio structure and local references using the Python standard library."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ENTRY = SITE / "index.html"


class SiteAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.hrefs: list[tuple[str, str | None, str | None]] = []
        self.resources: list[str] = []
        self.section_ids: set[str] = set()
        self.project_statuses: list[str | None] = []
        self.aria_references: list[tuple[str, str]] = []
        self.heading_counts: dict[str, int] = {}
        self.duplicate_ids: set[str] = set()
        self.has_description = False
        self.has_title = False
        self.has_language = False
        self.has_og_image = False
        self.has_theme_toggle = False
        self.has_filter_controls = False
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.has_language = bool(attributes.get("lang"))
        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_counts[tag] = self.heading_counts.get(tag, 0) + 1
        for attribute in ("aria-controls", "aria-labelledby", "aria-describedby"):
            reference = attributes.get(attribute)
            if reference:
                self.aria_references.extend((attribute, token) for token in reference.split())
        if tag == "section" and element_id:
            self.section_ids.add(element_id)
        if tag == "a":
            href = attributes.get("href")
            if href is not None:
                self.hrefs.append((href, attributes.get("target"), attributes.get("rel")))
        if tag == "link" and attributes.get("rel") in {"stylesheet", "icon"}:
            href = attributes.get("href")
            if href:
                self.resources.append(href)
        if tag == "script" and attributes.get("src"):
            self.resources.append(attributes["src"])
        if tag == "meta" and attributes.get("name") == "description":
            self.has_description = bool(attributes.get("content"))
        if tag == "meta" and attributes.get("property") == "og:image":
            self.has_og_image = bool(attributes.get("content", "").endswith("/site/assets/social-preview.png"))
        if tag == "title":
            self._in_title = True
        if tag == "button" and "theme-toggle" in (attributes.get("class") or "").split():
            self.has_theme_toggle = True
        if tag == "button" and "filter-button" in (attributes.get("class") or "").split():
            self.has_filter_controls = True
        if tag == "article" and "project-card" in (attributes.get("class") or "").split():
            self.project_statuses.append(attributes.get("data-status"))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title and data.strip():
            self.has_title = True


def main() -> int:
    errors: list[str] = []
    if not ENTRY.is_file():
        print(f"ERROR: Missing site entry point: {ENTRY.relative_to(ROOT)}")
        return 1

    parser = SiteAudit()
    parser.feed(ENTRY.read_text(encoding="utf-8"))
    parser.close()

    for resource in parser.resources:
        parsed = urlsplit(resource)
        if parsed.scheme or parsed.netloc:
            errors.append(f"External runtime resource is not expected: {resource}")
            continue
        path = unquote(parsed.path)
        if path and not (SITE / path).resolve().is_file():
            errors.append(f"Missing local resource: {resource}")

    for href, target, rel in parser.hrefs:
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            if parsed.scheme in {"http", "https"} and target == "_blank":
                rel_tokens = set((rel or "").lower().split())
                if not {"noopener", "noreferrer"}.issubset(rel_tokens):
                    errors.append(f"New browsing context needs rel=noopener noreferrer: {href}")
            continue
        if parsed.path and not (SITE / unquote(parsed.path)).resolve().is_file():
            errors.append(f"Missing linked local file: {href}")
        if parsed.fragment and unquote(parsed.fragment) not in parser.ids:
            errors.append(f"Missing in-page anchor target: #{parsed.fragment}")

    expected_sections = {
        "home", "about", "experience", "expertise", "work",
        "architecture", "principles", "education", "contact",
    }
    missing_sections = expected_sections - parser.section_ids
    if missing_sections:
        errors.append(f"Missing expected sections: {', '.join(sorted(missing_sections))}")
    if parser.duplicate_ids:
        errors.append(f"Duplicate document IDs: {', '.join(sorted(parser.duplicate_ids))}")
    missing_aria_targets = {
        target for _, target in parser.aria_references if target not in parser.ids
    }
    if missing_aria_targets:
        errors.append(f"Missing ARIA reference targets: {', '.join(sorted(missing_aria_targets))}")
    if parser.heading_counts.get("h1") != 1:
        errors.append(f"Expected one primary heading, found {parser.heading_counts.get('h1', 0)}.")
    if not parser.has_title:
        errors.append("Missing document title.")
    if not parser.has_description:
        errors.append("Missing meta description.")
    if not parser.has_language:
        errors.append("Missing document language.")
    if not parser.has_og_image or not (SITE / "assets" / "social-preview.png").is_file():
        errors.append("Missing working Open Graph PNG image metadata/asset.")
    if not parser.has_theme_toggle:
        errors.append("Missing theme toggle.")
    if not parser.has_filter_controls:
        errors.append("Missing project filter controls.")
    if len(parser.project_statuses) != 11:
        errors.append(f"Expected 11 project entries, found {len(parser.project_statuses)}.")
    if any(not status for status in parser.project_statuses):
        errors.append("Every project entry needs an explicit data-status.")

    javascript = (SITE / "script.js").read_text(encoding="utf-8")
    stylesheet = (SITE / "styles.css").read_text(encoding="utf-8")
    if "prefers-reduced-motion" not in stylesheet:
        errors.append("Missing reduced-motion stylesheet support.")
    if "aria-pressed" not in javascript or "localStorage" not in javascript:
        errors.append("Missing accessible filter state or saved theme handling.")
    token_blocks = re.findall(
        r"(?m)^\s*:root\s*\{([^}]+)\}|^\s*html\[data-theme=\"light\"\]\s*\{([^}]+)\}",
        stylesheet,
    )
    if len(token_blocks) < 2:
        errors.append("Could not locate both design-token palettes for contrast checks.")
    else:
        dark_tokens = dict(re.findall(r"(--[\w-]+):\s*(#[0-9a-fA-F]{6})", token_blocks[0][0]))
        light_tokens = dict(re.findall(r"(--[\w-]+):\s*(#[0-9a-fA-F]{6})", token_blocks[1][1]))

        def luminance(color: str) -> float:
            channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
            linear = [
                channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
                for channel in channels
            ]
            return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

        def contrast(first: str, second: str) -> float:
            high, low = sorted((luminance(first), luminance(second)), reverse=True)
            return (high + 0.05) / (low + 0.05)

        contrast_results = []
        for label, palette in (("dark", dark_tokens), ("light", light_tokens)):
            surface_tokens = ("--bg", "--bg-soft", "--surface", "--surface-strong")
            text_tokens = ("--text", "--text-soft", "--muted", "--accent", "--violet")
            contrast_pairs = [
                (foreground, background)
                for foreground in text_tokens
                for background in surface_tokens
            ]
            contrast_pairs.append(("--accent-ink", "--accent"))
            for foreground, background in contrast_pairs:
                if foreground not in palette or background not in palette:
                    errors.append(f"Missing {label} theme contrast token: {foreground} or {background}.")
                elif contrast(palette[foreground], palette[background]) < 4.5:
                    ratio = contrast(palette[foreground], palette[background])
                    errors.append(f"{label} theme {foreground}/{background} contrast is only {ratio:.2f}:1.")
                else:
                    contrast_results.append((label, foreground, background, contrast(palette[foreground], palette[background])))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("PASS: site entry point, local resources, links, metadata, sections, and controls")
    print(f"PASS: {len(parser.project_statuses)} project cards have explicit statuses")
    print(f"PASS: {len(parser.resources)} local runtime resources; no external runtime dependencies")
    print(f"PASS: key design-token contrast checks >= 4.5:1 ({len(contrast_results)} color pairs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
