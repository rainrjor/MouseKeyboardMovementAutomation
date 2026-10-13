
import pyautogui
import keyboard
import math
import time

# Settings
radius = 15
steps = 60
delay = 0.03
word = "Hello mr robot"
typing_interval = 3

print("Automation started.")
print("Press ESC to stop.")

center_x, center_y = pyautogui.position()
angle = 0
last_type_time = time.time()
last_x, last_y = pyautogui.position()

try:
    while True:
        if keyboard.is_pressed("esc"):
            print("Automation stopped.")
            break

        # Detect manual mouse movement
        current_x, current_y = pyautogui.position()

        if math.hypot(current_x - last_x, current_y - last_y) > 5:
            center_x = current_x
            center_y = current_y

        # Calculate circular movement
        x = round(center_x + radius * math.cos(angle))
        y = round(center_y + radius * math.sin(angle))

        pyautogui.moveTo(x, y, duration=0)

        # Update angle
        angle += 2 * math.pi / steps
        if angle >= 2 * math.pi:
            angle = 0

        # Remember the expected position
        last_x, last_y = x, y

        # Type periodically
        if time.time() - last_type_time >= typing_interval:
            pyautogui.write(word, interval=0.1)
            print("Typed:", word)  # this can be removed if you don't want to see the output in the console
            last_type_time = time.time()

        time.sleep(delay)

except KeyboardInterrupt:
    print("Automation stopped.")

except pyautogui.FailSafeException:
    print("Mouse failsafe triggered.")

# pyautogui and keyboard libraries are used for mouse and keyboard automation. 
# The script moves the mouse in a circular pattern around its initial position and types a specified word at regular intervals. 
# It also detects manual mouse movement to adjust the center of the circular motion. 
# The automation can be stopped by pressing the ESC key.
#py "\\wsl.localhost\Ubuntu\home\ramas\PythonScripts\MouseKeyboardMov.py"