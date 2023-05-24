import pyautogui
import pygetwindow as gw

def shift_window():
    # pyautogui.keyDown('altleft')
    # pyautogui.press('\t')
    # pyautogui.keyUp('altleft')

    for window in gw.getAllWindows():
        if window.title.endswith('Atom'):
            # window.restore()
            window.activate()
            return
    raise KeyError('Atom')


def run():
    pyautogui.PAUSE = 2.0
    try:
        shift_window()
    except KeyError:
        return
    pyautogui.PAUSE = 0.25
    pyautogui.hotkey('ctrl', 'end')
    # pyautogui.write('\n\nHello world!', interval=0.25)
    pyautogui.write('\n\nHello world!')
