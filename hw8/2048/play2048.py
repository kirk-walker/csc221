import webbrowser
import pyautogui

page = webbrowser.open('https://gabrielecirulli.github.io/2048/')

fw = pyautogui.getActiveWindow()
if fw.isMaximized == False:
    fw.maximize()
    print('is not maximized')
else:
    print('is maximized')
    None
while fw == page:
    pyautogui.write('up')
    pyautogui.write('right')
    pyautogui.write('down')
    pyautogui.write('left')
    pyautogui.sleep(3)

