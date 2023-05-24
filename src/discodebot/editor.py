import pyautogui


def shift_window():
    # pyautogui.hotkey('altleft', '\t')
    pyautogui.keyDown('altleft')
    pyautogui.press('\t')
    pyautogui.keyUp('altleft')


def run():
    pyautogui.PAUSE = 2.0
    shift_window()
    pyautogui.PAUSE = 0.25
    pyautogui.hotkey('ctrl', 'end')
    # pyautogui.write('\n\nHello world!', interval=0.25)
    pyautogui.write('\n\nHello world!')
