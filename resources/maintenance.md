# Maintaining the library

Update the editable SVG or template first. Export publication figures with [librsvg](https://wiki.gnome.org/Projects/LibRsvg) from the repository root.

```sh
for file in examples/*.svg; do
  rsvg-convert -f pdf "$file" -o "${file%.svg}.pdf"
  rsvg-convert -z 2 "$file" -o "${file%.svg}.png"
done
dot -Gbgcolor=transparent -Tsvg assets/external/siliconcompiler/flowgraph.dot \
  -o assets/external/siliconcompiler/flowgraph.svg
dot -Gbgcolor=transparent -Tpdf assets/external/siliconcompiler/flowgraph.dot \
  -o assets/external/siliconcompiler/flowgraph.pdf
python3 scripts/build.py
python3 scripts/validate.py
```

Install Poppler for the vector-PDF check. Its `pdfimages -list` output should have no image entries in original figure exports. Compile all three TikZ templates from the `tikz/` directory. Review the figures at print scale and check that thin strokes and dashed feedback paths remain distinguishable.

The gallery, Draw.io palette and task SVGs use [assets.json](assets.json). Edit task labels and descriptions in that manifest, then rebuild. For artifact illustrations, edit the SVG directly and list representative design formats in the manifest. To review the Pages bundle, run `python3 scripts/build.py --check --site work/site` and `python3 -m http.server --bind 127.0.0.1 --directory work/site 8000`. Visit `http://localhost:8000/`, try a multi-word search and category filter, and open a download.

To publish from GitHub, select **Settings → Pages → GitHub Actions** and run the **Visual library** workflow on `main` after merging. See [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
