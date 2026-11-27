# Resource catalog

Each asset in the [manifest](assets.json) has a category and stable local path. The third-party entries also provide the pinned source, license evidence, credit, applicable restrictions and modification status. Editable inputs have their own source URLs. The searchable gallery surfaces these fields on each card.

| Resource | Use in EDA figures | In this library |
| --- | --- | --- |
| [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) | RTL-to-GDSII flow, physical design and reports | [Flow diagram](../assets/external/openroad/rtl2gds.svg), BSD-3-Clause. Use a browser for its embedded HTML labels. |
| [OpenLane](https://github.com/The-OpenROAD-Project/OpenLane) | Digital ASIC implementation flow | [Flowchart PNG](../assets/external/openlane/flow.png), Apache-2.0. |
| [SiliconCompiler](https://github.com/siliconcompiler/siliconcompiler) | Task graphs and reproducible build artifacts | [Flowgraph SVG](../assets/external/siliconcompiler/flowgraph.svg), [vector PDF](../assets/external/siliconcompiler/flowgraph.pdf) and [DOT source](../assets/external/siliconcompiler/flowgraph.dot), Apache-2.0. |
| [NetlistSVG](https://github.com/nturley/netlistsvg) | Render Yosys-style JSON netlists as schematics | [Multiplexer SVG](../assets/external/netlistsvg/mux4.svg) and [input JSON](../assets/external/netlistsvg/mux4.json), MIT. |
| [WaveDrom](https://wavedrom.com/) | Draw digital timing diagrams from WaveJSON | [Timing arcs SVG](../assets/external/wavedrom/signal-arcs.svg) and [source](../assets/external/wavedrom/signal-arcs.json5), MIT. |
| [CircuiTikZ](https://ctan.org/pkg/circuitikz) | Typeset editable circuit diagrams as vector PDFs | [Original CMOS template](../tikz/cmos-inverter.tex). The upstream package is a dependency under LPPL or GPL. Review individual upstream examples before copying them. |
| [Tiny Tapeout chip renders](https://github.com/TinyTapeout/tinytapeout-chip-renders) | Real shuttle layouts and interconnect density | [TT04 full GDS PNG](../assets/external/tinytapeout/tt04-full-gds.png), CC BY 4.0. |
| [KLayout](https://www.klayout.de/) | Inspect layouts and export PNG screenshots | [Screenshot workflow](https://www.klayout.de/doc/manual/screenshots.html). Tool code is GPL-3.0. Use a layout you have permission to publish. Tool screenshots and documentation artwork are linked only. |
| [Tabler Icons](https://github.com/tabler/tabler-icons) | General compute, processor and automation symbols | [CPU](../assets/external/tabler/cpu.svg), [GPU](../assets/external/tabler/gpu.svg), [robot](../assets/external/tabler/robot.svg), MIT. |
| [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Logic_gates) | Logic and CMOS schematic artwork | [CMOS inverter](../assets/external/wikimedia/cmos-inverter.svg) by Abaddon1337, CC BY-SA 3.0. Review other Commons files individually. |

Use the original figure set when you need a consistent palette and transparent canvas. Upstream assets retain their existing visual style. The Tiny Tapeout render has an opaque background, and the OpenROAD browser SVG uses embedded HTML.

### Sample captions for third-party images

- “Tiny Tapeout 4 full GDS render” by Tiny Tapeout. [Source](https://github.com/TinyTapeout/tinytapeout-chip-renders/blob/64c58c2d33a95908fcf8ca172ef43b21d5177b68/shuttles/tt04/full_gds.png) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Unmodified.
- “CMOS inverter.svg” by Abaddon1337. [Source](https://commons.wikimedia.org/wiki/File:CMOS_inverter.svg?oldid=844011754) · [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) · Unmodified. Share adaptations under the same or a permitted compatible license.
