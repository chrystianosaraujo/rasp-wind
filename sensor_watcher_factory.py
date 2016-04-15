try:
    from sensor_watcher import AnemometerWatcher
except ImportError:
    from fake_sensor_watcher import FakeAnemometerWatcher as AnemometerWatcher

class SensorWatcherFactory:
    @staticmethod
    def create_anemometer_watcher(*args, **kwargs):
        return AnemometerWatcher(*args, **kwargs)

