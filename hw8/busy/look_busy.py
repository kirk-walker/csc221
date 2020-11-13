import pyautogui
import time

def look_busy():

    print('Press CTRL-C to quit.')
    try:
        while True:
            pyautogui.moveRel(5, 0, .5)
            pyautogui.moveRel(-5, 0, .5)
            time.sleep(10)

    except KeyboardInterrupt:
            print('Process quit.')

if __name__ == "__main__":
    look_busy()