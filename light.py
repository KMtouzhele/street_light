from sense_emu import SenseHat
import state
import display

sense = SenseHat()

def check_light():
    humidity = sense.get_humidity()
    threshold = state.get_threshold()

    if humidity > threshold:
        if state.get_light_state() != 0:
            state.set_light_state(0)
            display.all_off()
    else:
        if state.get_light_state() != 1:
            state.set_light_state(1)
            display.all_on()
    print("Current light state ", state.get_light_state())
    return humidity