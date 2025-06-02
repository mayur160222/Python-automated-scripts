import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Create a keyboard object
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Give time for OS to recognize the device
time.sleep(3)

# Press Win + R to open Run dialog
keyboard.press(Keycode.WINDOWS, Keycode.R)
keyboard.release_all()
time.sleep(1)

# Type 'notepad' and press Enter
layout.write("brave")
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(2)

keyboard.press(Keycode.CRTL, Keycode.N)
keyboard.release_all()

#keyboard.press(Keycode.WINDOWS, Keycode.UP_ARROW)
#keyboard.release_all()

# Type a message in Notepad
layout.write("youtube.com")
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(7)

layout.write("/")
time.sleep(1)

layout.write("he as pahil SONG")
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(5)

for _ in range(53):
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.05)  # Small delay between keypresses

keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(1)












