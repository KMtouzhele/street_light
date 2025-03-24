# 0 - regular
# 1 - collision
current_state = 0

def get_state():
    return current_state

def set_state(state):
    global current_state
    current_state = state