"""Render this overview's fixed-layout Mermaid subset as standalone SVG.

Adapted from the OSDS and Ecological Information diagram protocol. Labels,
colours, edges and layout belong in the adjacent .mmd source. This is a
purpose-specific renderer, not a general Mermaid engine. Python 3 only.
"""
from pathlib import Path
from html import escape
import hashlib
import re
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "osds_federation.mmd"
DESTINATION = HERE / "osds_federation.svg"


def render():
    source = SOURCE.read_text(encoding="utf-8")
    width, height = map(int, re.search(r"^%% @canvas (\d+) (\d+)$", source, re.M).groups())
    title = re.search(r"^%% @title (.+)$", source, re.M).group(1)
    description = re.search(r"^%% @description (.+)$", source, re.M).group(1)
    labels = dict(re.findall(r'^\s*(?:subgraph\s+)?(\w+)\["([^"\n]+)"\]', source, re.M))
    hints = re.findall(r"^%% @(box|group) (\w+) (\d+) (\d+) (\d+) (\d+) (\w+)$", source, re.M)
    boxes = {name: tuple(map(int, (x, y, w, h))) for _, name, x, y, w, h, _ in hints}
    styles = {name: dict(item.split(":", 1) for item in declarations.split(","))
              for name, declarations in re.findall(r"^\s*classDef (\w+) ([^\n;]+);", source, re.M)}
    assert set(boxes) == set(labels), "Every diagram label needs a layout hint."
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
             f'<title id="title">{escape(title)}</title>',
             f'<desc id="description">{escape(description)}</desc>',
             f'<!-- Derived from {SOURCE.name}; SHA-256 {hashlib.sha256(SOURCE.read_bytes()).hexdigest()}. Do not edit this SVG directly. -->',
             '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#637286"/></marker></defs>',
             f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
             '<g font-family="Arial, Helvetica, sans-serif" text-anchor="middle">']
    # Edges express documented organisation; ~~~ is layout only.
    for a, relationship, b in re.findall(r"^\s*(\w+) (<-->|-->) (\w+)\s*$", source, re.M):
        ax, ay, aw, ah = boxes[a]; bx, by, bw, bh = boxes[b]
        assert by > ay + ah, "Overview connectors must run downward between bands."
        start = ' marker-start="url(#arrow)"' if relationship == "<-->" else ""
        parts.append(f'<path d="M {ax+aw/2:g} {ay+ah+4} L {bx+bw/2:g} {by-5}" fill="none" stroke="#637286" stroke-width="1.6" marker-end="url(#arrow)"{start}/>')
    for kind, name, _, _, _, _, role in hints:
        x, y, w, h = boxes[name]; style = styles[role]
        assert 0 <= x < x+w <= width and 0 <= y < y+h <= height, name
        dash = ' stroke-dasharray="6 4"' if name == "DRM" else ""
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-width="{style.get("stroke-width", "1.5")}"{dash}/>')
        lines = labels[name].split("<br/>")
        # Explicit typography offsets keep compact layout faithful to the original.
        text_hint = re.search(r"^%% @text " + name + r" ([\d.,]+) ([\d.,]+) ([\d,]+)$", source, re.M)
        assert text_hint is not None, name
        sizes, offsets, weights = [list(map(float, values.split(","))) for values in text_hint.groups()]
        assert len(lines) == len(sizes) == len(offsets) == len(weights), name
        for line, size, offset, weight in zip(lines, sizes, offsets, weights):
            assert offset - size * .8 > 0 and offset + size * .25 < h, name
            parts.append(f'<text x="{x+w/2:g}" y="{y+offset:g}" font-size="{size:g}" font-weight="{weight:g}" fill="{style["color"]}">{escape(line)}</text>')
    for x, y, note in re.findall(r"^%% @note (\d+) (\d+) (.+)$", source, re.M):
        parts.append(f'<text x="{x}" y="{y}" font-size="17" fill="#526174">{escape(note)}</text>')
    parts.append("</g></svg>")
    svg = "\n".join(parts) + "\n"
    ET.fromstring(svg)
    DESTINATION.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    render()
