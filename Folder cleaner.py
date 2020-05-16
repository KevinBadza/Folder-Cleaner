from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
# This is the only folder that will not be moved by the script.

            if filename != 'downloads_test_file':
                new_name = filename
                file_exists = os.path.isfile(folder_destination + '/' + new_name)
# This is in the case when there is a duplicate file. To reduce overwriting the files will be renamed
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '/' + new_name)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(folder_destination + "/" + new_name)

                    src = folder_to_track + "/" + filename
                    new_name = folder_destination + "/" + new_name
                    os.rename(src, new_name)

folder_to_track = '\Downloads\download_test'
folder_destination = '\Downloads\download_test\downloads_destination'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()


