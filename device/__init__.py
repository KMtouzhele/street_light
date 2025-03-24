from sense_emu import SenseHat

sense = SenseHat()

LIGHT_THRESHOLD = 40
REPORT_INTERNAL = 60

from .led import show, clear, flash
from .state import get_state, set_state