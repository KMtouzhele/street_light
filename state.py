import time

setup_state = 0
collision_state = 0
light_state = 0
brownout_state = 0
power_surge_state = 0
threshold = 40
collision_reported = False
last_report_time = time.time()

def get_last_report_time():
    return last_report_time

def set_last_report_time(time):
    global last_report_time
    last_report_time = time

def set_setup_mode(state: int):
    global setup_state
    setup_state = state

def get_setup_mode():
    return setup_state

def set_light_state(state: int):
    global light_state
    light_state = state

def get_light_state():
    return light_state

def set_collision_state(state: int):
    global collision_state
    collision_state = state
    
def get_collision_state():
    return collision_state

def set_brownout_state(state: int):
    global brownout_state
    brownout_state = state
    
def get_brownout_state():
    return brownout_state

def set_power_surge_state(state: int):
    global power_surge_state
    power_surge_state = state
    
def get_power_surge_state():
    return power_surge_state

def get_threshold():
    return threshold

def set_threshold(new_threshold: int):
    global threshold
    threshold = new_threshold
    
def set_collision_reported(flag: bool):
    global collision_reported
    collision_reported = flag

def get_collision_reported():
    return collision_reported
