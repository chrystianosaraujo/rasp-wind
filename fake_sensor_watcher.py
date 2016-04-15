class FakeAnemometerWatcher:
    def __init__(self, data, target_wind_speed):
        """ This class cannot be directly instantiate from here. It must be created
            using SensorWatcherFactory API.
        """
        self.data = data
        self.target_speed = target_wind_speed

    def start_watching(self):
        while True:
            pass

    def get_sensor_description(self):
        return "Fake anemometer sensor used in test environment."

    @staticmethod
    def clean_gpio():
        # TODO(caraujo): this method must be removed
        pass
