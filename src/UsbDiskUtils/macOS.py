import sys
import subprocess
from threading import Thread
from datetime import datetime

class UsbDiskUtils:
    def __init__(self):
        self.workers = {}

    def start_worker(self, name=None, path=None, kind=None, callback=None):
        worker = Worker(name, path, kind, callback)
        self.workers[id(worker)] = worker
        worker.start()
        return id(worker)

    def stop_worker(self, worker_id):
        worker = self.workers.pop(worker_id, None)
        if worker:
            worker.stop()

class Worker(Thread):
    def __init__(self, name=None, path=None, kind=None, callback=None):
        super().__init__(target=self.__monitoring, daemon=True)
        self.name = name
        self.path = path
        self.kind = kind
        self.callback = callback
        self.running = True

    def stop(self):
        self.running = False

    def __monitoring(self):
        DISKUTIL = ["/usr/sbin/diskutil", "activity"]
        try:
            with subprocess.Popen(
                DISKUTIL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            ) as diskutil:
                while self.running:
                    line = diskutil.stdout.readline()
                    if not line or not self.running:
                        break
                    self.handle_event(line)
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_event(self, line):
        if line.startswith("***DiskDisappeared") or line.startswith("***DiskAppeared"):
            log_time_str = (
                line.split("Time=")[1]
                .split()[0]
                .replace("-", "")
                .replace(".", "")
                .replace(":", "")
            )
            log_time = datetime.strptime(log_time_str, "%Y%m%d%H%M%S%f")

            if (
                (self.name and self.name in line)
                or (self.path and self.path in line)
                or (self.kind and self.kind in line)
            ):
                self.callback(line)
