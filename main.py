import time
import state
import light
import display
import collision
import power
import report
from sense_emu import SenseHat
from datetime import datetime

sense = SenseHat()
display.all_off()
report.report_threshold()


while True:
    events = sense.stick.get_events()

    if state.get_collision_state() == 1:
        if not state.get_collision_reported():
            report.send_report_once()
            state.set_collision_reported(True)
        for event in events:
            if event.action == 'pressed' and event.direction == 'middle':
                state.set_collision_state(0)
                state.set_collision_reported(False)
                display.stop_flashing()
                print("Collision state cleared by center button.")

    elif state.get_setup_mode() == 1:
        if 'setup_enter_time' not in globals():
            setup_enter_time = time.time()
        threshold = state.get_threshold()
        if events:
            setup_enter_time = time.time()
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
                        report.report_threshold()
                        del setup_enter_time
        else:
            sense.show_message(str(threshold))
            if time.time() - setup_enter_time > 10:
                state.set_setup_mode(0)
                display.all_off()
                print("Auto-exited setup mode after 10 seconds of inactivity")
                report.report_threshold()
                del setup_enter_time

    else:
        for event in events:
            if event.action == 'pressed' and event.direction == 'middle':
                state.set_setup_mode(1)
                print("Entered setup mode")

        power.check_power()
        light.check_light()
        display.check_display()
        collision.check_collision()
        
    if state.get_setup_mode() == 0:
        report.check_and_report()

    time.sleep(1)
