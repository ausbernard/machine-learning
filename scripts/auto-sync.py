import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# Define a custom event handler that inherits from FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
    # This method is called when a file or directory is modified
    def on_modified(self, event):
        print("File changed, syncing...")
        # Call the sync.sh script using subprocess
        subprocess.call(['./sync.sh'])

# This is the main entry point of the script
if __name__ == "__main__":
    # Create an instance of the custom event handler
    event_handler = MyHandler()
    # Create an instance of Observer, which monitors file system events
    observer = Observer()
    # Schedule the observer to use the custom event handler for events in the specified path
    observer.schedule(event_handler, path='/Volumes/fd/machine-learning', recursive=True)
    # Start the observer
    observer.start()

    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # If the script is interrupted, stop the observer
        observer.stop()
    # Wait for the observer to finish
    observer.join()