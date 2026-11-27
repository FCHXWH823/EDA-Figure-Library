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

Use the labeled rectangles for **tasks** and the pictograms for **design artifacts**. A task can pass several artifacts to the next stage. The formats below are examples from digital ASIC flows. Click a rectangle or pictogram to open its editable SVG.

### Specification, architecture and logic

| EDA task | Typical inputs | Representative output | Artifact preview |
| --- | --- | --- | :---: |
| [<img src="icons/tasks/specification.svg" width="192" alt="Write specification">](icons/tasks/specification.svg) | Workloads, requirements, PPA goals | Specification document (`.md`, `.pdf`) | [<img src="icons/frontend/specification.svg" width="110" alt="Specification document">](icons/frontend/specification.svg) |
| [<img src="icons/tasks/architecture.svg" width="192" alt="Define architecture">](icons/tasks/architecture.svg) | Specification, interface requirements | Architecture block diagram | [<img src="icons/frontend/architecture.svg" width="110" alt="Architecture block diagram">](icons/frontend/architecture.svg) |
| [<img src="icons/tasks/rtl-design.svg" width="192" alt="RTL design">](icons/tasks/rtl-design.svg) | Architecture, interface and timing requirements | RTL source (`.sv`, `.v`, `.vhd`) | [<img src="icons/frontend/rtl-code.svg" width="110" alt="SystemVerilog RTL source">](icons/frontend/rtl-code.svg) |
| [<img src="icons/frontend/high-level-synthesis.svg" width="192" alt="High-level synthesis">](icons/frontend/high-level-synthesis.svg) | C, C++ or a domain-specific language and synthesis directives | Generated RTL (`.v`, `.sv`) | [<img src="icons/frontend/rtl-code.svg" width="110" alt="Generated RTL source">](icons/frontend/rtl-code.svg) |
| [<img src="icons/frontend/logic-synthesis.svg" width="192" alt="Logic synthesis">](icons/frontend/logic-synthesis.svg) | RTL, [design constraints](icons/frontend/constraints.svg) (`.sdc`), cell library (`.lib`) | Gate-level Verilog netlist (`.v`) | [<img src="icons/frontend/logic-netlist.svg" width="110" alt="Connected gates in a gate-level netlist">](icons/frontend/logic-netlist.svg) |
| [<img src="icons/verification/functional.svg" width="192" alt="Functional verification">](icons/verification/functional.svg) | RTL or netlist, testbench and stimuli | Simulation waveform (`.vcd`, `.fst`) and coverage reports | [<img src="icons/verification/waveform.svg" width="110" alt="Simulation timing waveform">](icons/verification/waveform.svg) |
| [<img src="icons/verification/formal.svg" width="192" alt="Formal verification">](icons/verification/formal.svg) | RTL or netlist, properties or reference design | Proof report or counterexample trace | [<img src="icons/verification/proof-report.svg" width="110" alt="Formal verification report">](icons/verification/proof-report.svg) |

### Physical design and signoff

| EDA task | Typical inputs | Representative output | Artifact preview |
| --- | --- | --- | :---: |
| [<img src="icons/tasks/floorplanning.svg" width="192" alt="Floorplanning">](icons/tasks/floorplanning.svg) | Mapped netlist, LEF, die and I/O constraints | Floorplan (`.def`, `.odb`) | [<img src="icons/backend/floorplan.svg" width="110" alt="Die with macro regions">](icons/backend/floorplan.svg) |
| [<img src="icons/tasks/placement.svg" width="192" alt="Placement">](icons/tasks/placement.svg) | Floorplan, mapped cells, constraints | Placed layout (`.def`, `.odb`) | [<img src="icons/backend/placement.svg" width="110" alt="Legalized standard-cell rows">](icons/backend/placement.svg) |
| [<img src="icons/tasks/clock-tree-synthesis.svg" width="192" alt="Clock tree synthesis">](icons/tasks/clock-tree-synthesis.svg) | Placed design and clock constraints | Post-CTS layout (`.def`, `.odb`) with a buffered clock tree | [<img src="icons/backend/clock-tree.svg" width="110" alt="Buffered clock tree">](icons/backend/clock-tree.svg) |
| [<img src="icons/tasks/routing.svg" width="192" alt="Routing">](icons/tasks/routing.svg) | Post-CTS design, routing layers and rules | Routed layout (`.def`, `.odb`) | [<img src="icons/backend/routing.svg" width="110" alt="Metal routes and vias connecting standard-cell pins">](icons/backend/routing.svg) |
| [<img src="icons/tasks/stream-out.svg" width="192" alt="Layout stream-out">](icons/tasks/stream-out.svg) | Routed design, cell and macro geometry, layer mapping | Mask layout (`.gds`, `.oas`) | [<img src="icons/backend/gds-layout.svg" width="110" alt="Layered GDSII mask polygons">](icons/backend/gds-layout.svg) |
| [<img src="icons/tasks/physical-verification.svg" width="192" alt="Physical verification">](icons/tasks/physical-verification.svg) | Layout, rule decks and reference netlist | DRC/LVS reports and violation markers | [<img src="icons/backend/physical-verification.svg" width="110" alt="DRC and LVS results">](icons/backend/physical-verification.svg) |
| [<img src="icons/tasks/tapeout.svg" width="192" alt="Tape-out">](icons/tasks/tapeout.svg) | Signed-off mask layout and required reports | Foundry-specific delivery package | [<img src="icons/backend/tapeout.svg" width="110" alt="Tape-out package">](icons/backend/tapeout.svg) |

A Verilog **netlist** describes cell instances and which pins share a logical net. Routing adds the physical wire and via geometry to the **routed layout**, typically stored in DEF or OpenDB. Some flows also export an updated netlist after routing, for example when implementation changes cell instances or logical connectivity. The GDSII icon shows separate mask layers as an exploded view of planar polygons. See [OpenLane’s detailed-routing and stream-out documentation](https://openlane2.readthedocs.io/en/latest/reference/step_config_vars.html#detailed-routing).

### AI-assisted hardware design

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
