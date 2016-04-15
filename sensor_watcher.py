import RPi.GPIO as GPIO
import time

PIN_LED_OUT = 27

class AnemometerWatcher:
    def __init__(self, sensor_input_pin, data):
        self.sensor_pin = sensor_input_pin
        self.data = data

        # The anemometer sensor generates one pulse for each
        # half cycle. This flag is used to verify if the last
        # pulse is related to an whole anemometer cycle.
        self.whole_cycle = True

    def start_watching(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(PIN_LED_OUT, GPIO.OUT)
      GPIO.setup(self.sensor_pin, GPIO.IN, GPIO.PUD_UP)

      # Turn LED ON
      GPIO.output(PIN_LED_OUT, GPIO.HIGH)

      self.initial_state = GPIO.input(self.sensor_pin)
      self.last_state = self.initial_state

      event_cb = lambda channel: self._new_cycle(channel)
      GPIO.add_event_detect(self.sensor_pin,
                            GPIO.RISING,
                            callback = event_cb)

      while True:
          pass

    @staticmethod
    def clean_gpio():
        GPIO.cleanup()

    def _new_cycle(self, ch):
        new_state = GPIO.input(self.sensor_pin)

        state_changed = new_state != self.last_state
        if state_changed:
            if new_state == self.initial_state:
                self.whole_cycle = not self.whole_cycle

                if self.whole_cycle:
                    self.data.add_cycle(time.time())

        self.last_state = new_state
