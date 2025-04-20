from sense_emu import SenseHat
import time
import threading
import state

sense = SenseHat()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

_flashing = False
_flash_thread = None

def check_display():
    light = state.get_light_state()
    brownout = state.get_brownout_state()
    surge = state.get_power_surge_state()
    if brownout + surge != 0:
        all_off()
    elif light == 0:
        all_off()
    else:
        all_on()

def all_on(color=WHITE):
    sense.clear(color)

def all_off():
    sense.clear(BLACK)

def _flashing_loop(interval=0.5):
    while _flashing:
        all_on()
        time.sleep(interval)
        all_off()
        time.sleep(interval)

def flash_all_leds(interval=0.5):
    global _flashing, _flash_thread
    if not _flashing:
        _flashing = True
        _flash_thread = threading.Thread(target=_flashing_loop, args=(interval,))
        _flash_thread.daemon = True
        _flash_thread.start()

def stop_flashing():
    global _flashing
    _flashing = False
    time.sleep(0.1)
    all_off()
