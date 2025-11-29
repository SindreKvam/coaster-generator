"""Script to generate coaster from any image."""

import argparse
from circle_picker import CirclePicker
from svg import Svg


def generate_coaster_svg(
    filename: str,
    diameter_mm: float = 100.0,
    margin_mm: float = 5.0,
    image_path: str | None = None,
) -> None:
    """Generate an .svg file with a coaster of a given size."""

    r_outer = diameter_mm / 2
    r_inner = r_outer - margin_mm
    cx = cy = r_outer

    svg = Svg(diameter_mm, diameter_mm)

    svg.add_circle(cx, cy, r_outer, id="coaster_outline", stroke_color="red")

    if image_path is not None:
        # Have the user circle out which part of the image they want on the coaster
        picker = CirclePicker(image_path)
        img_h, img_w, img_center, img_radius = picker.run()

        img_cx, img_cy = img_center
        S = r_inner / img_radius

        img_x = cx - img_cx * S
        img_y = cy - img_cy * S
        img_w *= S
        img_h *= S

        svg.embed_image(
            cx,
            cy,
            r_inner,
            image_path,
            img_x,
            img_y,
            img_w,
            img_h,
            id="coaster_inner_image",
        )

    else:
        svg.add_circle(cx, cy, r_inner, id="coaster_inner_circle")

    svg.export_image(filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-d", "--diameter", type=float, default=100.0)
    parser.add_argument("-m", "--margin", type=float, default=5.0)
    parser.add_argument("-i", "--image", type=str, default=None)
    args = parser.parse_args()

    generate_coaster_svg(
        args.filename, args.diameter, args.margin, image_path=args.image
    )
