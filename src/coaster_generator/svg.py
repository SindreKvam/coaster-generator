import base64
import mimetypes


def embed_image_base64(path):
    mime, _ = mimetypes.guess_type(path)
    if mime is None:
        raise ValueError(f"Cannot determine MIME type for file: {path}")

    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")

    return f"data:{mime};base64,{data}"


class Svg:
    svg_file_content = ""

    def __init__(self, canvas_width: float, canvas_height: float) -> None:
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.svg_file_content += f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
  width="{canvas_width}mm"
  height="{canvas_height}mm"
  viewBox="0 0 {canvas_width} {canvas_height}"
  xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:svg="http://www.w3.org/2000/svg"
  >
"""

    def add_circle(
        self,
        cx: float,
        cy: float,
        radius: float,
        *,
        id: str,
        stroke_color: str = "black",
        stroke_width: float = 0.2,
        metadata: str = "",
    ) -> None:
        """Add circle to the svg"""

        self.svg_file_content += f"""  <circle cx="{cx}" cy="{cy}" r="{radius}"
              id="{id}"
              fill="none"
              stroke="{stroke_color}"
              stroke-width="{stroke_width}"
              inkscape:label="coaster inner edge"/>
"""

    def embed_image(
        self,
        cx,
        cy,
        radius: float,
        image_path: str,
        img_x,
        img_y,
        img_w,
        img_h,
        *,
        id="",
    ) -> None:
        """Embed image into the svg"""

        self.svg_file_content += f"""  <defs id="defs1">
    <clipPath id="imageClip">
      <circle cx="{cx}" cy="{cy}" r="{radius}" />
    </clipPath>
  </defs>

  <image href="{embed_image_base64(image_path)}"
  x="{img_x}" y="{img_y}" width="{img_w}" height="{img_h}" clip-path="url(#imageClip)"/>
"""

    def export_image(self, filename: str) -> None:
        self.svg_file_content += "</svg>"

        with open(filename, "w") as f:
            f.write(self.svg_file_content)
