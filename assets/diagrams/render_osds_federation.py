"""Render this diagram's fixed-layout Mermaid subset as portable SVG.

Labels, groups, relationships and layout all come from osds_federation.mmd.
This is a purpose-specific renderer, not a general Mermaid implementation.
Run with Python 3 from any directory; no third-party packages are required.
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
    labels = dict(re.findall(r'^\s*(?:subgraph\s+)?(\w+)\["([^"\n]+)"\]', source, re.M))
    width, height = map(int, re.search(r'^%% @canvas (\d+) (\d+)$', source, re.M).groups())
    hints = re.findall(r'^%% @(box|container|region) (\w+) (\d+) (\d+) (\d+) (\d+)(?: (\w+))?$', source, re.M)
    boxes = {name: tuple(map(int, (x, y, w, h))) for _, name, x, y, w, h, _ in hints}
    roles = {name: role for _, name, _, _, _, _, role in hints}
    styles = {}
    for name, declarations in re.findall(r'^\s*classDef (\w+) ([^\n;]+);', source, re.M):
        styles[name] = dict(item.split(":", 1) for item in declarations.split(","))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
             '<title id="title">OSDS within the Ecological Information federation</title>',
             '<desc id="description">Interdisciplinary synthesis above shared methodology and seven autonomous neighbouring research databases; OSDS below, with eight observation categories in two columns.</desc>',
             f'<!-- Derived from osds_federation.mmd; SHA-256 {hashlib.sha256(SOURCE.read_bytes()).hexdigest()}. Do not edit this SVG directly. -->',
             '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#637286"/></marker></defs>',
             f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
             '<g font-family="Arial, Helvetica, sans-serif" text-anchor="middle">']
    # Only explicit conceptual graph edges are drawn. ~~~ edges are layout-only.
    for a, relation, b in re.findall(r'^\s*(\w+) (<-->|-->) (\w+)\s*$', source, re.M):
        ax, ay, aw, ah = boxes[a]; bx, by, bw, bh = boxes[b]
        start = ' marker-start="url(#arrow)"' if relation == '<-->' else ''
        parts.append(f'<path d="M {ax + aw / 2:g} {ay + ah + 5} L {bx + bw / 2:g} {by - 5}" fill="none" stroke="#637286" stroke-width="1.6" marker-end="url(#arrow)"{start}/>')
    for kind, name, _, _, _, _, role in hints:
        if kind == 'region':
            # An unlabelled grouping boundary prevents the central card from
            # appearing to be the sole endpoint of federation connectors.
            x, y, w, h = boxes[name]
            declarations = re.search(r'^\s*style ' + name + r' ([^\n]+)$', source, re.M).group(1)
            style = dict(item.split(':', 1) for item in declarations.split(','))
            parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-dasharray="{style["stroke-dasharray"]}"/>')
            continue
        x, y, w, h = boxes[name]
        style = styles[roles[name]]
        stroke_width = style.get('stroke-width', '1px').removesuffix('px')
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-width="{stroke_width}"/>')
        lines = labels[name].split('<br/>')
        if kind == 'container':
            ys = [y + 36, y + 66]; sizes = [27, 18]
        elif role == 'synthesis':
            ys = [y + 43, y + 80]; sizes = [30, 22]
        elif role == 'shared':
            ys = [y + h / 2 + 7]; sizes = [28]
        elif role == 'category':
            ys = [y + h / 2 + 6]; sizes = [22]
        elif len(lines) == 1:
            ys = [y + h / 2 + 7]; sizes = [23]
        else:
            ys = [y + h / 2 - 5, y + h / 2 + 20]; sizes = [22, 15]
        for index, (line, baseline, size) in enumerate(zip(lines, ys, sizes)):
            weight = '600' if index == 0 and role != 'category' else '400'
            parts.append(f'<text x="{x + w / 2:g}" y="{baseline:g}" font-size="{size}" font-weight="{weight}" fill="{style["color"]}">{escape(line)}</text>')
    nx, ny, note = re.search(r'^%% @note (\d+) (\d+) (.+)$', source, re.M).groups()
    parts.append(f'<text x="{nx}" y="{ny}" font-size="17" fill="#566579">{escape(note)}</text>')
    parts.append('</g></svg>')
    svg = '\n'.join(parts) + '\n'
    ET.fromstring(svg)
    DESTINATION.write_text(svg, encoding="utf-8")


if __name__ == '__main__':
    render()
