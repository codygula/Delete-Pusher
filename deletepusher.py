import keyboard
import time

time.sleep(2)
x = 0
while True:
    keyboard.press("delete")
    print(f"delete pressed {x} times")
    time.sleep(2)
    x += 1
