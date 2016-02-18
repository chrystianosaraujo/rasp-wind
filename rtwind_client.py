import requests


class RealTimeWindAPI:
    """ This class provides an API to interface with the RealtimeWind restful server.
    """

    def __init__(self, server, port = None):
        """ server - server base url
            port   - port which the server is running
        """
        self.server = server
        self.port = port
        self.url = self.server

        if self.port:
            self.url = "%s:%s" % (self.url, str(self.port))

    def send_wind_conditions(self, anemometer_cycles, measure_interval):
        """ Send realtime wind conditions to the server.

            anemometer_cycles - list of anemometer cycles. Each cycle must define the
                                number of seconds since epoch.
            measure_interval  - it must be a tuple defining the interval time (seconds since epoch)
                                on which the data have been collected. It will rarely be equal to the
                                first and last anemometer cycles, remember that there will be intervals
                                with no wind.

            Returns false if it was not possible to reach the server and true if everything was ok.
        """
        url = self._url("/sync_data/")
        data_as_json = {
            "interval": measure_interval,
            "anemometer_cycles": anemometer_cycles
        }

        resp = requests.put(url, json = data_as_json)
        return resp.status_code != 404

    def _url(self, tail):
        return self.url + tail
