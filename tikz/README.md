# LaTeX and TikZ templates

Compile each standalone template from this directory with `pdflatex -halt-on-error -interaction=nonstopmode <name>.tex`. Install PGF/TikZ and the `standalone` class. The CMOS template also needs [CircuiTikZ](https://ctan.org/pkg/circuitikz).

| Template | Use |
| --- | --- |
| [eda-flow.tex](eda-flow.tex) | Compact ASIC workflow with an optional HLS path and closure feedback. |
| [agentic-eda-flow.tex](agentic-eda-flow.tex) | Agent planning, batched experiments, evaluation and human release review. |
| [cmos-inverter.tex](cmos-inverter.tex) | Original transistor-level example for adapting the circuit template. |

Adjust the nodes and arrows directly and use [eda-style.tex](eda-style.tex) to change the shared palette. Include the compiled vector figure with `\includegraphics[width=\linewidth]{eda-flow.pdf}` and put the caption in your manuscript.
