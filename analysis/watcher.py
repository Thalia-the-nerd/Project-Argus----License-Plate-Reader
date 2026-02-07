import time
import sys
import cv2
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from detector import ArgusBrain


class NewFrameHandler(FileSystemEventHandler):
    def __init__(self):
        self.brain = ArgusBrain()

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".jpg"):
            # Brief pause to ensure file write is finished
            time.sleep(0.1)

            # Process frame
            annotated_frame = self.brain.scan_and_draw(event.src_path)

            if annotated_frame is not None:
                # Show the dashboard window
                cv2.imshow("Argus Intelligence Dashboard", annotated_frame)

                # Wait 1ms to allow the window to render graphics
                cv2.waitKey(1)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f">> Argus Dashboard Online. Monitoring: {path}")

    event_handler = NewFrameHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        cv2.destroyAllWindows()
    observer.join()
