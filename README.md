# EDA Figure Library

Editable illustrations for electronic design automation, digital ASIC design, and AI-assisted hardware research. Build a paper figure, proposal diagram, or lecture slide from transparent SVGs, vector PDFs, native diagrams.net blocks, and LaTeX templates.

[Search the visual gallery](https://fchxwh823.github.io/EDA-Figure-Library/) · [Draw.io palette](drawio/eda-shapes.xml) · [TikZ templates](tikz) · [Resource catalog](resources) · [Licenses and credits](LICENSES.md)

## Example figures

### Complete EDA flow

![Complete digital ASIC design flow with optional HLS, parallel verification, signoff and tape-out](examples/eda-flow.svg)

[Editable SVG](examples/eda-flow.svg) · [Vector PDF](examples/eda-flow.pdf) · [Transparent PNG](examples/eda-flow.png) · [Compact TikZ template](tikz/eda-flow.tex)

The diagram follows design intent through architecture, hand-written or HLS-generated RTL, logic synthesis, physical implementation and foundry handoff. It shows representative verification and closure feedback.

### Agentic EDA flow

![Agentic EDA flow with specialized agents, executable tools, design-space exploration, GPU compute and evidence feedback](examples/agentic-eda-flow.svg)

[Editable SVG](examples/agentic-eda-flow.svg) · [Vector PDF](examples/agentic-eda-flow.pdf) · [Transparent PNG](examples/agentic-eda-flow.png) · [Compact TikZ template](tikz/agentic-eda-flow.tex)

The diagram illustrates how specialized agents can coordinate experiments, evaluate correctness and power, performance and area (PPA), and feed evidence back into earlier design decisions. Both examples are conceptual schematics.

## Browse by EDA stage

### Front-end design and verification

<table>
  <tr>
    <td width="25%" align="center"><a href="icons/frontend/specification.svg"><img src="icons/frontend/specification.svg" width="120" alt=""><br>Specification</a></td>
    <td width="25%" align="center"><a href="icons/frontend/architecture.svg"><img src="icons/frontend/architecture.svg" width="120" alt=""><br>Architecture</a></td>
    <td width="25%" align="center"><a href="icons/frontend/rtl-code.svg"><img src="icons/frontend/rtl-code.svg" width="120" alt=""><br>RTL source</a></td>
    <td width="25%" align="center"><a href="icons/frontend/constraints.svg"><img src="icons/frontend/constraints.svg" width="120" alt=""><br>Design constraints</a></td>
  </tr>
  <tr>
    <td width="25%" align="center"><a href="icons/frontend/logic-netlist.svg"><img src="icons/frontend/logic-netlist.svg" width="120" alt=""><br>Gate-level netlist</a></td>
    <td width="25%" align="center"><a href="icons/verification/waveform.svg"><img src="icons/verification/waveform.svg" width="120" alt=""><br>Timing waveform</a></td>
    <td width="25%" align="center"><a href="icons/verification/proof-report.svg"><img src="icons/verification/proof-report.svg" width="120" alt=""><br>Formal verification results</a></td>
  </tr>
</table>

### Physical design and signoff

<table>
  <tr>
    <td width="25%" align="center"><a href="icons/backend/floorplan.svg"><img src="icons/backend/floorplan.svg" width="120" alt=""><br>Floorplan</a></td>
    <td width="25%" align="center"><a href="icons/backend/placement.svg"><img src="icons/backend/placement.svg" width="120" alt=""><br>Placed layout</a></td>
    <td width="25%" align="center"><a href="icons/backend/clock-tree.svg"><img src="icons/backend/clock-tree.svg" width="120" alt=""><br>Clock tree</a></td>
    <td width="25%" align="center"><a href="icons/backend/routing.svg"><img src="icons/backend/routing.svg" width="120" alt=""><br>Routed layout</a></td>
  </tr>
  <tr>
    <td width="25%" align="center"><a href="icons/backend/physical-verification.svg"><img src="icons/backend/physical-verification.svg" width="120" alt=""><br>DRC / LVS results</a></td>
    <td width="25%" align="center"><a href="icons/backend/tapeout.svg"><img src="icons/backend/tapeout.svg" width="120" alt=""><br>Tape-out package</a></td>
    <td width="25%" align="center"><a href="icons/backend/gds-layout.svg"><img src="icons/backend/gds-layout.svg" width="120" alt=""><br>GDSII layout</a></td>
  </tr>
</table>

## AI-assisted hardware design

[Agent](icons/ai/agent.svg) · [Evolutionary optimization](icons/ai/evolutionary-optimization.svg) · [Design space exploration](icons/ai/design-space.svg) · [GPU](icons/ai/gpu-compute.svg) · [Cross-stage feedback](icons/ai/cross-stage-feedback.svg) · [Feedback loop](icons/ai/feedback.svg) · [PPA](icons/ai/ppa.svg)

## How to use the library

- **Browse and download.** Open the [published gallery](https://fchxwh823.github.io/EDA-Figure-Library/) or open [docs/index.html](docs/index.html) locally after downloading the repository. Search by title, description, artifact format, source credit or license, or filter by category.
- **Edit vectors.** Open the SVG directly in Inkscape or another vector editor. Keep text editable while composing. Use a light canvas to preserve contrast, and preview at the final print size.
- **Draw diagrams.** Load the [Draw.io palette](drawio/README.md) for editable task rectangles, artifact blocks and connectors. Import the SVG icons separately for detailed artwork.
- **Typeset figures.** Download a vector PDF and use `\includegraphics[width=\linewidth]{eda-flow.pdf}`, or edit the [standalone TikZ templates](tikz/README.md) for document-matched typography.
- **Credit the source.** Check the [license guide](LICENSES.md) for original figure attribution and the [manifest](resources/assets.json) for each third-party asset.

The third-party collection covers OpenROAD, OpenLane, SiliconCompiler, NetlistSVG, WaveDrom, CircuiTikZ, Tiny Tapeout, KLayout, Tabler Icons and Wikimedia Commons. The [resource catalog](resources/README.md) explains what is included and how to use each source.

## Contributing

Use transparent SVGs with a viewBox, editable paths and text, and descriptive titles. Label synthetic diagrams as conceptual. For external assets, supply a stable per-file source, the license evidence, the credit line, any restrictions and what changed. Include the corresponding notice when required.

Update [resources/assets.json](resources/assets.json), then run `python3 scripts/build.py` and `python3 scripts/validate.py`. See the [maintenance guide](resources/maintenance.md) for exports and publishing.
