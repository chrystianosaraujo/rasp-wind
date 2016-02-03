import threading

class AnemometerData:
    def __init__(self):
        self.cycles = []
        self.lock = threading.RLock()

    def add_cycle (cycle):
        self.lock.acquire()
        self.cycles.append(cycle)
        self.lock.release()

    def add_cycles (cycles):
        self.lock.acquire()
        self.cycles.extend(cycles)
        self.lock.release()

    def size ():
        return len(self.size)
