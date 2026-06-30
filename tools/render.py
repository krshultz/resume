#!/usr/bin/env python3
"""Render the resume (README.md) into a clean, print-ready standalone HTML file.

Usage: render.py <input.md> <output.html>

The output has no GitHub chrome (no Releases/Packages/sidebar) and carries
print-tuned CSS, so you can open it in a browser and Print -> Save as PDF.
"""
import sys
import markdown

CSS = """
@page { size: Letter; margin: 0.6in 0.7in; }
* { box-sizing: border-box; }
body {
  font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt; line-height: 1.4; color: #1a1a1a;
  max-width: 7.1in; margin: 0 auto; padding: 0.4in 0;
}
h1 { font-size: 22pt; margin: 0 0 2pt; }
h2 {
  font-size: 13pt; margin: 16pt 0 6pt; padding-bottom: 2pt;
  border-bottom: 1.5px solid #333; break-after: avoid;
}
h3 { font-size: 11.5pt; margin: 12pt 0 2pt; break-after: avoid; }
p { margin: 4pt 0; }
ul { margin: 4pt 0 8pt; padding-left: 18px; }
ul ul { margin: 2pt 0; }
li { margin: 2pt 0; break-inside: avoid; }
a { color: #1a1a1a; text-decoration: none; }
strong { font-weight: 600; }
em { color: #555; }
hr { border: none; border-top: 1px solid #ddd; margin: 10pt 0; }
table { border-collapse: collapse; }
/* keep a job's heading attached to its first lines */
h3 + p, h3 + ul { break-before: avoid; }
@media print { body { padding: 0; } }
"""


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: render.py <input.md> <output.html>")
    src, out = sys.argv[1], sys.argv[2]
    with open(src) as f:
        body = markdown.markdown(
            f.read(),
            extensions=["extra", "sane_lists", "smarty"],
        )
    html = (
        '<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">\n'
        "<title>Karl Shultz — Resume</title>\n"
        f"<style>{CSS}</style></head>\n<body>{body}</body></html>\n"
    )
    with open(out, "w") as f:
        f.write(html)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
