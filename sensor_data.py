""" Classes to store sensors data. """

import threading

class AnemometerData:
    """ Thread-safe Anemometer data storage. """

    def __init__(self):
        # Used to store all anemometer cycles of a day.
        self.cycles = []

        # RLock is used to let some class method to call another one.
        self.lock = threading.RLock()

    def add_cycle(self, cycle):
        """ Adds a new anemometer cycle.

        cycle must define the time when the sensor interrupt has happened.
        it must provide the number of seconds since epoch. """

        self.lock.acquire()
        self.cycles.append(cycle)
        self.lock.release()

    def add_cycles(self, cycles):
        """ Adds new anemometer cycles.

        cycles must be a list of sensor interrupts as descrided in add_cycle method.
        """

        self.lock.acquire()
        self.cycles.extend(cycles)
        self.lock.release()

    def size(self):
       """ Returns the number of anemometer cycles so far. """

       return len(self.size)
