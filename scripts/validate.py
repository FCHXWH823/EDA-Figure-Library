#!/usr/bin/env python3
"""Validate figure files, catalog completeness, downloads and native palette XML."""

import json
import re
import shutil
import struct
import subprocess
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
SVG = "{http://www.w3.org/2000/svg}"
STAGES = {
    "specification", "architecture", "rtl-code", "high-level-synthesis",
    "logic-synthesis", "functional", "formal", "floorplan", "placement",
    "clock-tree", "routing", "physical-verification", "gds-layout", "tapeout",
    "agent", "evolutionary-optimization", "design-space", "gpu-compute",
    "cross-stage-feedback",
}
ARTIFACT_CATEGORIES = {"frontend", "verification", "backend"}


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def check_svg(path, original):
    document = ET.parse(path).getroot()
    require(document.tag == SVG + "svg", f"Missing SVG root: {path}")
    view_box = document.get("viewBox")
    if view_box:
        values = re.split(r"[ ,]+", view_box.strip())
        require(len(values) == 4 and all(float(value) > 0 for value in values[2:]),
                f"Invalid SVG viewBox: {path}")
    else:
        require(not original and all(float(document.get(key, "0").removesuffix("px")) > 0
                                     for key in ("width", "height")),
                f"Missing SVG dimensions: {path}")
    for element in document.iter():
        require(element.tag != SVG + "script", f"Active SVG script: {path}")
        for key, value in element.attrib.items():
            require(not key.lower().startswith("on"), f"SVG event handler: {path}")
            if key.rsplit("}", 1)[-1] == "href":
                is_link = not original and element.tag == SVG + "a" and value.startswith("https://")
                require(is_link or value.startswith(("#", "data:image/")), f"External SVG reference: {path}")
        if original:
            require(element.tag not in {SVG + "image", SVG + "foreignObject", SVG + "filter"},
                    f"Original must export as vector: {path}")


def check_png(path, transparent=False):
    png = path.read_bytes()
    require(png[:8] == b"\x89PNG\r\n\x1a\n" and png[12:16] == b"IHDR" and b"IEND" in png[-12:],
            f"Invalid PNG stream: {path}")
    width, height, depth, color = struct.unpack(">IIBB", png[16:26])
    require(width > 0 and height > 0 and depth > 0, f"Invalid PNG size: {path}")
    if transparent:
        require(color in {4, 6} and width >= 3000, f"Missing alpha or sufficient resolution: {path}")


def check_pdf(path):
    require(path.read_bytes().startswith(b"%PDF-"), f"Invalid PDF: {path}")
    if shutil.which("pdfimages"):
        output = subprocess.check_output(["pdfimages", "-list", path], text=True)
        require(len(output.splitlines()) == 2, f"Raster content in vector PDF: {path}")
    if shutil.which("pdfinfo"):
        output = subprocess.check_output(["pdfinfo", path], text=True)
        require(re.search(r"^Pages:\s+1$", output, re.M), f"Expected one page: {path}")


class GalleryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []
        self.cards = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "article" and attrs.get("class") == "card":
            self.cards += 1
        for key in ("href", "src"):
            if key in attrs:
                parts = urlsplit(attrs[key])
                if parts.path and not parts.scheme and not parts.netloc:
                    self.paths.append(unquote(parts.path))


def check_gallery(count):
    path = ROOT / "docs/index.html"
    gallery = GalleryParser()
    gallery.feed(path.read_text())
    require(gallery.cards == count, "The gallery must have one card per catalog asset.")
    for relative in gallery.paths:
        require((path.parent / relative).exists(), f"Broken gallery URL: {relative}")


def check_library(originals):
    wrapper = ET.parse(ROOT / "drawio/eda-shapes.xml").getroot()
    require(wrapper.tag == "mxlibrary", "Expected a Draw.io mxlibrary wrapper.")
    palette = json.loads(wrapper.text)
    names = set()
    for item in palette:
        graph = ET.fromstring(item["xml"])
        objects = graph.findall("./root/mxCell[@parent='1']")
        require(graph.tag == "mxGraphModel" and len(objects) == 1,
                f"Invalid native Draw.io shape: {item['title']}")
        node = objects[0]
        require(node.find("mxGeometry") is not None and ("vertex" in node.attrib or "edge" in node.attrib),
                f"Non-editable palette entry: {item['title']}")
        names.add(item["title"])
    require(len(names) == originals + 2 == len(palette), "Missing or duplicate Draw.io entries.")
    return len(palette)


def main():
    manifest = json.loads((ROOT / "resources/assets.json").read_text())["assets"]
    ids = {asset["id"] for asset in manifest}
    require(len(ids) == len(manifest) and STAGES <= ids, "Missing stages or duplicate catalog IDs.")
    visual_paths = set()
    source_paths = set()
    for asset in manifest:
        path = ROOT / asset["file"]
        require(path.is_file() and path not in visual_paths, f"Missing or duplicate asset: {path}")
        visual_paths.add(path)
        original = asset["category"] != "external"
        if asset["category"] in ARTIFACT_CATEGORIES:
            require(bool(asset.get("formats")), f"Missing artifact format examples: {path}")
        if asset["category"] == "tasks":
            task = ET.parse(path).getroot()
            require(len(task.findall(SVG + "rect")) == 1
                    and len(task.findall(SVG + "text")) == 1
                    and task.findtext(SVG + "text") == asset["title"],
                    f"Expected a single named task rectangle: {path}")
        if not original:
            for key in ("source", "licenseSource", "licenseUrl"):
                require(asset[key].startswith("https://"), f"Missing {key}: {path}")
            for key in ("license", "credit", "restrictions", "changes"):
                require(asset[key].strip(), f"Missing {key}: {path}")
            if not asset["license"].startswith("CC-"):
                require((path.parent / "LICENSE").is_file(), f"Missing license notice: {path}")
            for source_file in asset["sourceFiles"]:
                source = ROOT / source_file["file"]
                require(source.is_file() and source_file["source"].startswith("https://"),
                        f"Missing source or source URL: {source}")
                source_paths.add(source)
        if path.suffix == ".svg":
            check_svg(path, original)
        if path.suffix == ".png":
            check_png(path)
        if asset["category"] == "examples":
            check_png(path.with_suffix(".png"), transparent=True)
            check_pdf(path.with_suffix(".pdf"))
        for export in asset.get("exports", []):
            export_path = ROOT / export
            require(export_path.is_file() and export_path.suffix == ".pdf",
                    f"Invalid cataloged vector export: {export_path}")
            check_pdf(export_path)
            source_paths.add(export_path)
    for path in (ROOT / "assets/external").glob("*/*"):
        require(path.name == "LICENSE" or path in visual_paths | source_paths,
                f"Uncatalogued third-party file: {path}")
    for path in (ROOT / "icons").glob("*/*.svg"):
        require(path in visual_paths, f"Uncatalogued original icon: {path}")
    originals = sum(asset["file"].startswith("icons/") for asset in manifest)
    shapes = check_library(originals)
    check_gallery(len(manifest))
    print(f"Validated {len(manifest)} gallery figures, their downloads and {shapes} Draw.io elements.")


if __name__ == "__main__":
    main()
