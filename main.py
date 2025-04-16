import time
import state
import light
import display
import collision
import power
from sense_emu import SenseHat

sense = SenseHat()
display.all_off()

while True:
    events = sense.stick.get_events()

    if state.get_collision_state() == 1:
        for event in events:
            if event.action == 'pressed' and event.direction == 'middle':
                state.set_collision_state(0)
                display.stop_flashing()
                print("Collision state cleared by center button.")

    elif state.get_setup_mode() == 1:
        threshold = state.get_threshold()
        for event in events:
            if event.action == 'pressed':
                if event.direction == 'up':
                    threshold += 1
                    state.set_threshold(threshold)
                    sense.show_message(str(threshold))
                elif event.direction == 'down':
                    threshold -= 1
                    state.set_threshold(threshold)
                    sense.show_message(str(threshold))
                elif event.direction == 'middle':
                    state.set_setup_mode(0)
                    display.all_off()
                    print("Exited setup mode")
        # Show current threshold if no button was pressed
        if not events:
            sense.show_message(str(threshold))

    else:
        # Check for entering setup mode
        for event in events:
            if event.action == 'pressed' and event.direction == 'middle':
                state.set_setup_mode(1)
                print("Entered setup mode")

        # Only check sensors if not in setup mode
        light.check_light()
        power.check_power()
        collision.check_collision()

    time.sleep(1)
