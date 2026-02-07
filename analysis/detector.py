from ultralytics import YOLO
import cv2
import os


class ArgusBrain:
    def __init__(self):
        # Load the model
        self.model = YOLO("yolov8n.pt")

    def scan_and_draw(self, image_path):
        if not os.path.exists(image_path):
            return None

        # Read the image from the buffer
        frame = cv2.imread(image_path)

        # Run inference
        results = self.model(frame)

        # Draw the "Clean" UI
        for result in results:
            # Ultralytics plot() returns the image with boxes drawn
            # line_width=2 makes it look sharp/clean
            frame = result.plot(line_width=2, font_size=1)

            # Add a Status Tag
            cv2.putText(
                frame,
                "ARGUS SYSTEM // ONLINE",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                1,
            )

        return frame
