"""Script to generate coaster from any image."""

import argparse



def generate_coaster_svg(filename:str, diameter_mm:float = 100.0, margin_mm:float = 5.0) -> None:
    """Generate an .svg file with a coaster of a given size."""

    r_outer = diameter_mm / 2
    r_inner = (diameter_mm - margin_mm) / 2
    cx = cy = r_outer

    svg = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
  width="{diameter_mm}mm"
  height="{diameter_mm}mm"
  viewBox="0 0 {diameter_mm} {diameter_mm}"
  xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:svg="http://www.w3.org/2000/svg"
  >

  <circle cx="{cx}" cy="{cy}" r="{r_outer}"
          id="outline"
          fill="none"
          stroke="red"
          stroke-width="0.2"
          inkscape:label="coaster outline"/>

  <circle cx="{cx}" cy="{cy}" r="{r_inner}"
          id="inner_edge"
          fill="none"
          stroke="black"
          stroke-width="0.2"
          inkscape:label="coaster inner edge"/>
</svg>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-d", "--diameter", type=float, default=100.0)
    parser.add_argument("-m", "--margin", type=float, default=5.0)
    args = parser.parse_args()

    generate_coaster_svg(args.filename, args.diameter, args.margin)
