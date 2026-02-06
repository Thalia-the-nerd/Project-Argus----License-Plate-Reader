from ultralytics import YOLO
import cv2
import os


class ArgusBrain:
    def __init__(self):
        # Load the smallest YOLO model (nano) for speed
        print(">> Loading Neural Network...")
        self.model = YOLO("yolov8n.pt")
        print(">> Neural Network Online.")

    def scan_image(self, image_path):
        if not os.path.exists(image_path):
            return

        # Run inference
        results = self.model(image_path)

        # Process results
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Class 2 is 'car', Class 7 is 'truck' in COCO dataset
                # For real ALPR, you'd train a custom model for plates,
                # but for this demo, we detect cars.
                cls = int(box.cls[0])
                if cls in [2, 5, 7]:  # car, bus, truck
                    print(f"!! VEHICLE DETECTED in {image_path}")
                    # In a real app, you would crop this box here
