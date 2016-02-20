import threading
import time
import sys

#TODO: Move this class to a new file
class CSI_CODE:
    """This class provides an easy API to use ANSI console scape sequences.

       https://en.wikipedia.org/wiki/ANSI_escape_code
    """

    # /033 stands for ASCII Escape (Esc)
    csi_code = "\033["

    @staticmethod
    def GO_UP_N_LINES(n):
        """Moves the cursor to the beginning of the line N lines up"""
        return CSI_CODE.csi_code + str(n) + "F"

    @staticmethod
    def GO_BEGIN_LINE():
        """Moves the cursor to the first column of the current line"""
        return CSI_CODE.csi_code + "1G"

    @staticmethod
    def CLEAR_LINE():
        """Clears the whole line"""
        return CSI_CODE.csi_code + "K"

    @staticmethod
    def CLEAR_SCREEN():
        """Clears the whole screen"""
        return CSI_CODE.csi_code + "2J"

    @staticmethod
    def GO_BEGIN_SCREEN():
        """Moves the cursor to the first row and column of the screen"""
        return CSI_CODE.csi_code + "f"


class WindDataConsoleReporter(threading.Thread):
    """This class provides a way to report realtime wind conditions through
       raspberry console.
    """

    def __init__(self, anemometer_data, interval):
        """anemometer_data - AnemometerData object which contains all sensor data.
           interval        - Interval (seconds) between each report.
        """
        super(WindDataConsoleReporter, self).__init__()

        self.daemon = True
        self.anemometer_data = anemometer_data
        self.interval = interval
        self.counter = 1

        self._prepare_console()

    def run(self):
        while True:
            time.sleep(self.interval)
            self._print_report()

    def _print_report(self):
        msg_lines = self._get_header_lines()

        # Clear last output
        self._clear_output(len(msg_lines))

        # Print new lines
        for line in msg_lines:
          self._print_message(line, True)

    def _get_header_lines(self):
        return [self._header_msg(),
                self._server_status_msg(),
                self._wind_conditions_msg()]

    def _header_msg(self):
        header_width = 50
        return " Realtime wind conditions ".center(header_width, "-")

    def _server_status_msg(self):
        status = self._get_server_status()
        status_str = status and "Online" or "Offline"

        return self._format_two_columns_msg("Server", status_str)

    def _wind_conditions_msg(self):
        speed, unit = self._get_wind_speed()
        speed_str = "{} {}".format(str(speed), unit)

        return self._format_two_columns_msg("Wind Speed", speed_str)

    def _format_two_columns_msg(self, first_col, second_col):
        first_column_width = 10
        return "{}: {}".format(first_col.ljust(first_column_width), second_col)

    def _clear_output(self, num_lines):
        for i in xrange(num_lines):
            sys.stdout.write(CSI_CODE.GO_BEGIN_LINE())
            sys.stdout.write(CSI_CODE.CLEAR_LINE())
            sys.stdout.write(CSI_CODE.GO_UP_N_LINES(1))

    def _print_message(self, msg, endline = False):
        sys.stdout.write(msg)
        if endline:
            sys.stdout.write("\n")

    def _prepare_console(self):
        self._print_message(CSI_CODE.CLEAR_SCREEN())
        self._print_message(CSI_CODE.GO_BEGIN_SCREEN())

    def _flush(self):
        sys.stdout.flush()

    def _get_server_status(self):
        return False

    def _get_wind_speed(self):
        self.counter += 1
        return float(self.counter), "Km"
