""" Application config data. """

import json

class ApplicationConfigData:
    def __init__(self, config_fn):
        """ Loads the application config data from a json file.

        config_fn is the filename of a configuration json file.
        """

        self._parse_config_file(config_fn)
        self._check_config_data()

    def raspberry_anemometer_pin(self):
        """ Returns the GPIO pin that must be used as the anemometer
        input pin.
        """
        return self.anemometer_pin

    def raspberry_console_interval(self):
        """ Returns the GPIO pin that must be used as the anemometer
        input pin.
        """
        return self.console_interval

    def server_syncronization_interval(self):
        """ Returns the interval time, in milliseconds, used to send wind
        conditions to the server.
        """
        return self.sync_interval

    def _parse_config_file(self, config_fn):
        try:
            json_file = open(config_fn, "r")
            json_data = json.load(json_file)

            self.anemometer_pin   = int(json_data["raspberry"]["anemometer_pin"])
            self.console_interval = int(json_data["raspberry"]["console_report_interval"])
            self.sync_interval    = float(json_data["server"]["sync_interval"])

        except IOError:
            error_msg = "The configuration file does not exist - "
            raise InvalidConfigFileError(error_msg + config_fn)

        except (ValueError, KeyError):
            raise InvalidConfigFileError("The configuration file is not valid.")

    def _check_config_data(self):
        if not self.anemometer_pin or not self.sync_interval:
            raise InvalidConfigFileError("The configuration file is not valid.")


class InvalidConfigFileError(Exception):
    """ Class used to represent errors while loading the config file. """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.__class__.__name__ + ": " + self.msg
