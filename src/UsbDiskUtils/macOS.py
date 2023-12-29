import sys
import subprocess
from threading import Thread
from datetime import datetime

class UsbDiskUtils:
    def __init__(self, *args, **kwds):
        self.name = kwds.get('name') or None
        self.path = kwds.get('path') or None
        self.kind = kwds.get('kind') or None
        self.__thread = Thread(target=self.__monitoring, daemon=True)
        self.event_handler = args
        self.marker = "YOUR_UNIQUE_MARKER"  # Set a unique marker for events after program start
        self.started_marker_found = False  # Flag to indicate whether the marker is found

    def log_callback(self, log_line):
        print('\r\033[K%s' % log_line, end='', flush=True)

    def __monitoring(self):
        DISKUTIL = ["/usr/sbin/diskutil", "activity"]
        try:
            with subprocess.Popen(DISKUTIL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as diskutil:
                while True:
                    line = diskutil.stdout.readline()
                    if not line:
                        break
                    self.handle_event(line)
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_event(self, line):
        if line.startswith("***DiskDisappeared") or line.startswith("***DiskAppeared"):
            # Extract the time from the log entry
            log_time_str = line.split('Time=')[1].split()[0].replace('-', '').replace('.', '').replace(':', '')
            log_time = datetime.strptime(log_time_str, "%Y%m%d%H%M%S%f")

            # Add conditions for specific events
            if (self.name and self.name in line) or \
                (self.path and self.path in line) or \
                (self.kind and self.kind in line):
                self.log_callback(line)
                for event_handler in self.event_handler:
                    event_handler(log_time)

        elif not any([self.name, self.path, self.kind]):
            # Process other events after the marker is found
            print(line)
            for event_handler in self.event_handler:
                event_handler

    def run_monitoring(self):
        try:
            launch_time = datetime.now()
            print("Disk activity log started at... ", launch_time)

            # Start monitoring in a separate thread
            if not self.__thread.is_alive():
                self.__thread.start()
            self.__thread.join()
        except KeyboardInterrupt:
            # Exit with error code 1 if the user presses Ctrl-C to interrupt the program.
            sys.exit(1)




