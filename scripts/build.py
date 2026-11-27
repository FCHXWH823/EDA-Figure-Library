#!/usr/bin/env python3
"""Build the offline gallery, diagrams.net palette and GitHub Pages bundle."""

import argparse
import html
import json
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "examples": "Example figures",
    "frontend": "Specification, RTL and synthesis",
    "verification": "Functional and formal verification",
    "backend": "Physical design and tape-out",
    "ai": "AI and optimization",
    "external": "Third-party assets",
}
COLORS = {
    "frontend": ("#EAF3FC", "#2563A6"),
    "verification": ("#F0E9FA", "#7756A5"),
    "backend": ("#E6F5F1", "#16736A"),
    "ai": ("#F0E9FA", "#7756A5"),
}
SHAPES = {
    "specification": "document", "architecture": "swimlane", "rtl-code": "note",
    "high-level-synthesis": "hexagon", "logic-synthesis": "process",
    "logic-netlist": "process", "constraints": "note",
    "functional": "process", "waveform": "parallelogram", "formal": "rhombus",
    "floorplan": "rectangle", "placement": "rectangle", "clock-tree": "triangle",
    "routing": "process", "physical-verification": "rhombus",
    "gds-layout": "cylinder3", "tapeout": "document",
    "agent": "hexagon", "evolutionary-optimization": "ellipse",
    "design-space": "parallelogram", "gpu-compute": "process",
    "cross-stage-feedback": "parallelogram", "feedback": "ellipse", "ppa": "rhombus",
}


def link(path, label, download=False):
    suffix = " download" if download else ""
    return f'<a href="{html.escape(path, quote=True)}"{suffix}>{html.escape(label)}</a>'


def gallery_card(asset):
    group = asset["category"]
    path = asset["file"]
    title = asset["title"]
    search = " ".join([
        title, asset["id"].replace("-", " "), asset["description"],
        CATEGORIES[group], asset.get("license", "CC-BY-4.0"), asset.get("credit", ""),
    ]).lower()
    downloads = [link("../" + path, Path(path).suffix[1:].upper(), download=True)]
    if group == "examples":
        for suffix in (".pdf", ".png"):
            export = Path(path).with_suffix(suffix).as_posix()
            downloads.append(link("../" + export, suffix[1:].upper(), download=True))
        downloads.append(link(f"../tikz/{asset['id']}.tex", "TikZ", download=True))
    for export in asset.get("exports", []):
        downloads.append(link("../" + export, Path(export).suffix[1:].upper(), download=True))
    for source_file in asset.get("sourceFiles", []):
        filename = source_file["file"]
        downloads.append(link("../" + filename, Path(filename).suffix[1:].upper(), download=True))

    if group == "external":
        license_link = link(asset["licenseUrl"], asset["license"])
        source_link = link(asset["source"], "Original source")
        credit = html.escape(asset["credit"])
        changes = html.escape(asset["changes"])
        restrictions = html.escape(asset["restrictions"])
        terms_link = link(asset["licenseSource"], "Upstream license evidence")
        details = (
            f"<p>{credit} · {license_link} · {source_link}</p>"
            f"<p>{changes}</p><p>{restrictions}</p><p>{terms_link}</p>"
        )
    else:
        license_link = link("https://creativecommons.org/licenses/by/4.0/", "CC BY 4.0")
        details = f"<p>EDA Figure Library contributors · {license_link}</p>"
    preview_class = "preview icon" if group in COLORS else "preview"
    return (
        f'<article class="card" data-category="{group}" data-search="{html.escape(search)}">\n'
        f'  <a class="{preview_class}" href="../{path}">'
        f'<img loading="lazy" src="../{path}" alt="{html.escape(title)}"></a>\n'
        f'  <div class="card-body"><p class="category">{CATEGORIES[group]}</p>'
        f'<h3>{html.escape(title)}</h3><p>{html.escape(asset["description"])}</p>'
        f'<p class="downloads">{" ".join(downloads)}</p>\n'
        f"    <details><summary>License and credit</summary>{details}</details></div>\n"
        "</article>"
    )


def build_gallery(assets):
    template = (ROOT / "docs/gallery.html.in").read_text()
    options = "\n          ".join(
        f'<option value="{key}">{title}</option>' for key, title in CATEGORIES.items()
    )
    assets = sorted(assets, key=lambda asset: list(CATEGORIES).index(asset["category"]))
    cards = "\n        ".join(gallery_card(asset) for asset in assets)
    return template.replace("@OPTIONS@", options).replace("@CARDS@", cards)


def drawio_shape(asset):
    fill, stroke = COLORS[asset["category"]]
    width, height = 180, 72
    model = ET.Element("mxGraphModel")
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    shape = SHAPES[asset["id"]]
    style = (
        f"shape={shape};html=0;whiteSpace=wrap;strokeWidth=2;fillColor={fill};"
        f"strokeColor={stroke};fontColor=#13263D;fontSize=13;fontStyle=1;"
        "spacing=8;perimeterSpacing=1;"
    )
    if shape == "swimlane":
        style += "startSize=28;swimlaneFillColor=#FFFFFF;"
    card = ET.SubElement(
        root, "mxCell", id="2", value=asset["title"], style=style, vertex="1", parent="1"
    )
    ET.SubElement(card, "mxGeometry", x="0", y="0", width=str(width), height=str(height),
                  attrib={"as": "geometry"})
    return {
        "xml": ET.tostring(model, encoding="unicode"),
        "w": width, "h": height, "aspect": "fixed", "title": asset["title"],
    }


def drawio_arrow(title, color, dashed):
    model = ET.Element("mxGraphModel")
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    edge = ET.SubElement(
        root, "mxCell", id="2", value="", edge="1", parent="1",
        style=f"endArrow=block;endFill=1;rounded=1;strokeWidth=2;strokeColor={color};dashed={dashed};"
    )
    geometry = ET.SubElement(edge, "mxGeometry", relative="1", attrib={"as": "geometry"})
    ET.SubElement(geometry, "mxPoint", x="0", y="12", attrib={"as": "sourcePoint"})
    ET.SubElement(geometry, "mxPoint", x="120", y="12", attrib={"as": "targetPoint"})
    return {"xml": ET.tostring(model, encoding="unicode"), "w": 120, "h": 24, "title": title}


def build_library(assets):
    entries = [drawio_shape(asset) for asset in assets if asset["category"] in COLORS]
    entries.extend([
        drawio_arrow("Artifact handoff", "#526579", 0),
        drawio_arrow("Feedback / iteration", "#B45309", 1),
    ])
    library = ET.Element("mxlibrary")
    library.text = "\n" + json.dumps(entries, indent=2, ensure_ascii=False) + "\n"
    return ET.tostring(library, encoding="unicode") + "\n"


def write_or_check(path, data, check):
    if check:
        if not path.exists() or path.read_text() != data:
            raise SystemExit(f"{path.relative_to(ROOT)} is stale. Run python3 scripts/build.py.")
    else:
        path.write_text(data)


def build_site(destination):
    destination.mkdir(parents=True, exist_ok=True)
    for name in ("assets", "drawio", "icons", "examples", "resources", "tikz"):
        shutil.copytree(ROOT / name, destination / name, dirs_exist_ok=True)
    for name in ("LICENSES.md", "LICENSE"):
        shutil.copy2(ROOT / name, destination / name)
    (destination / "docs").mkdir(exist_ok=True)
    for name in ("index.html", "gallery.css", "gallery.js"):
        shutil.copy2(ROOT / "docs" / name, destination / "docs" / name)
    (destination / "index.html").write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta http-equiv="refresh" content="0; url=docs/">'
        '<title>EDA Figure Library</title><a href="docs/">Open the visual gallery</a></html>\n'
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--site", type=Path, help="Copy the static gallery to this output directory.")
    args = parser.parse_args()
    assets = json.loads((ROOT / "resources/assets.json").read_text())["assets"]
    write_or_check(ROOT / "docs/index.html", build_gallery(assets), args.check)
    write_or_check(ROOT / "drawio/eda-shapes.xml", build_library(assets), args.check)
    if args.site:
        build_site(args.site)


if __name__ == "__main__":
    main()
