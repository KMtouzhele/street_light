from sense_emu import SenseHat
import state
import display

sense = SenseHat()
prev_x, prev_y, prev_z = 0.0, 0.0, 0.0
initialized = False

def check_collision():
    global prev_x, prev_y, prev_z, initialized
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'],2)
    y = round(acceleration['y'],2)
    z = round(acceleration['z'],2)
    if not initialized:
        prev_x, prev_y, prev_z = x, y, z
        initialized = True
        return
    dx = x - prev_x
    dy = y - prev_y
    dz = z - prev_z
    movement = (dx**2 + dy**2 + dz**2) ** 0.5
    if movement >= 0.2:
        if state.get_collision_state() != 1:
            state.set_collision_state(1)
            display.flash_all_leds()
    print("Collision State ", state.get_collision_state())
    prev_x, prev_y, prev_z = x, y, z
