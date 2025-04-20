from sense_emu import SenseHat
import state
import display

sense = SenseHat()

def check_power():
    temp = sense.get_temperature()
    
    if temp < 0:
        state.set_brownout_state(1)
        state.set_power_surge_state(0)
    if temp > 100:
        state.set_brownout_state(0)
        state.set_power_surge_state(1)
    if temp >= 0 and temp <=100:
        state.set_brownout_state(0)
        state.set_power_surge_state(0)
    # print("brownout ", state.get_brownout_state())
    # print("surge ", state.get_power_surge_state())