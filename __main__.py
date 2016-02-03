from sensor_data import AnemometerData
from sensor_watcher import AnemometerWatcher
from data_sync import WindServerSynchronizer
import threading

# Raspberry input pin
# TODO(CARAUJO): read this info from a configuration file
INPUT_ANEMOMETER_PIN = 27

# 3 seconds. This value must just be used in test environment
# TODO(CARAUJO): read this info from a configuration file
SYNC_INTERVAL = 3

def main():
    print("... RealtimeWind has been started")

    speed_data   = AnemometerData()
    speed_sensor = AnemometerWatcher(INPUT_ANEMOMETER_PIN, speed_data)

    # The threading.Event is used to signal non-daemon threads that the 
    # main thread has died.
    stop_event  = threading.Event()
    server_sync = WindServerSynchronizer(speed_data, SYNC_INTERVAL, stop_event)

    try:
        server_sync.run()

        # The main thread will keep watching sensors for its whole
        # life cycle.
        speed_sensor.start_watching()

    except(KeyboardInterrupt, SystemExit):
        cleanup(stop_event)

def cleanup(stop_event):
  print("\n... Shutting down RealtimeWind application")

  # Signal non-daemon threads to finish their jobs
  stop_event.set()
  while threading.active_count() > 1:
      pass

  print("... RealtimeWind has been closed")

if __name__ == '__main__':
    main()
