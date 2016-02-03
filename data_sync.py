import threading
import time

class WindServerSynchronizer(threading.Thread):
    def __init__(self, speed_data, interval, stop_event):
        self.speed_data = speed_data
        self.interval   = interval
        self.stop_event = stop_event

    def run(self):
        print("... WindServerSynchronizer has started")
        while not self.stop_event.is_set():
            time.sleep(self.interval)
            self._sync_data()

    def _sync_data(self):
        print("... WindServerSynchronizer:sync_data")

