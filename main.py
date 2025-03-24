from device import show, clear, flash, get_state, set_state

set_state(1)
state = get_state()
while state == 1:
    flash()




