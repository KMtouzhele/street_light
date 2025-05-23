from sense_emu import SenseHat
import state
import display

sense = SenseHat()

def check_light():
    humidity = sense.get_humidity()
    threshold = state.get_threshold()

    if humidity > threshold:
        state.set_light_state(0)
    else:
        state.set_light_state(1)
    # print("Current light state ", state.get_light_state())
    return humidity
