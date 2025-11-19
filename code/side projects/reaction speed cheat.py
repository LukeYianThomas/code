import pyautogui, pydirectinput
pydirectinput.pause= 0.01
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        if pyautogui.pixel(928,300) == (75, 219, 106):pydirectinput.click(928, 300)
except KeyboardInterrupt:
    print('\n')

    #928 300