"""Allow user to circle out a part of the image
returns information about the chosen image"""

import cv2


class CirclePicker:
    def __init__(self, image_path, svg_out="coaster.svg"):
        self.image_path = image_path
        self.svg_out = svg_out
        self.img = cv2.imread(image_path)
        if self.img is None:
            raise FileNotFoundError(image_path)
        self.display = self.img.copy()

        self.drawing = False
        self.center = None
        self.radius = 0

        self.h = None
        self.w = None

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.center = (x, y)

        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            self.display = self.img.copy()
            self.radius = int(
                ((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2) ** 0.5
            )
            cv2.circle(self.display, self.center, self.radius, (0, 255, 0), 2)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.display = self.img.copy()
            self.radius = int(
                ((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2) ** 0.5
            )
            cv2.circle(self.display, self.center, self.radius, (0, 255, 0), 2)
            print(f"Selected circle: center={self.center}, radius={self.radius}")

            self.h, self.w = self.img.shape[:2]
            print("Press ESC or 'q' to quit, or draw another circle to overwrite.")

    def run(self):
        cv2.namedWindow("Circle picker", cv2.WINDOW_AUTOSIZE)
        cv2.setMouseCallback("Circle picker", self.mouse_callback)

        while True:
            cv2.imshow("Circle picker", self.display)
            key = cv2.waitKey(20) & 0xFF
            if key == 27 or key == ord("q"):
                break

        cv2.destroyAllWindows()

        return self.h, self.w, self.center, self.radius
