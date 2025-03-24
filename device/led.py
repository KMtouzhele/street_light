from device import sense
import time

def show (msg):
    while True:
        sense.show_message(msg)
        
def clear():
    print("try to clear..")
    sense.clear(0,0,0)
    
def flash():
    print("Flashing...")
    sense.clear(255,0,0)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)