import time
import sys
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
            print(f">> New packet received: {event.src_path}")
            # Give I/O a split second to finish writing the file
            time.sleep(0.1)
            self.brain.scan_image(event.src_path)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f">> Argus Intelligence Node watching: {path}")

    event_handler = NewFrameHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
