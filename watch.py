import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from pathlib import Path

current_path = Path(__file__).parent
main_file = Path(current_path, "main.py").absolute()
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')
        os.system(f'python3 {main_file}')
        print("main.py file reloaded")


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./templates', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()