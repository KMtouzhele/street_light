from datetime import datetime
import time
import state
import requests
from sense_emu import SenseHat

sense = SenseHat()
immediate_report = False
server = 'http://iotserver.com/report.php'
server2 = 'http://iotserver.com/threshold.php'

def check_and_report():
    last_report_time = state.get_last_report_time()
    current_time = time.time()
    
    if current_time - last_report_time >= 5:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        payload = {
            'l': sense.get_humidity(),
            'p': sense.get_temperature(),
            'c': state.get_collision_state(),
            'ts': timestamp
            }
        r = requests.get(server, params = payload)
        print(f"[{timestamp}] Report - Light: {state.get_light_state()}, "
              f"Power - Brownout: {state.get_brownout_state()}, Surge: {state.get_power_surge_state()}, "
              f"Collision: {state.get_collision_state()}")
        state.set_last_report_time(current_time)

def send_report_once():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payload = {
            'l': sense.get_humidity(),
            'p': sense.get_temperature(),
            'c': state.get_collision_state(),
            'ts': timestamp
            }
    r = requests.get(server, params = payload)
    print(f"[{timestamp}] Immediate Report - Light: {state.get_light_state()}, "
          f"Power - Brownout: {state.get_brownout_state()}, Surge: {state.get_power_surge_state()}, "
          f"Collision: {state.get_collision_state()}")
    
def report_threshold():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payload = {
            't': state.get_threshold(),
            'ts': timestamp
            }
    r = requests.get(server2, params = payload)
    print(f"Threshold updated: {state.get_threshold()}")