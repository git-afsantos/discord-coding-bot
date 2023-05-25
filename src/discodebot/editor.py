import subprocess

import pyautogui
try:
    import pygetwindow as gw
    IS_LINUX = False
except NotImplementedError:
    IS_LINUX = True

# https://github.com/jerryzhenleicai/linux-window-switcher/blob/master/window_switch.py
def shift_window_linux():
    proc = subprocess.run(
        ['xdotool', 'search', '--name', 'Atom'],
        capture_output=True,
    )
    lines = proc.stdout.decode('utf-8').splitlines()
    wins = list(sorted([entry.strip() for entry in lines if entry]))
    wins = list(filter(lambda x : not 'Defaulting to search' in x , wins))
    if not wins:
        raise KeyError('Atom')

    target_window = None
    for win in wins:
        proc = subprocess.run(
            ['xdotool', 'getwindowname', win],
            capture_output=True,
        )
        name = proc.stdout.decode('utf-8').strip()
        if name.endswith('— Atom'):
            target_window = win
            break
    else:
        raise KeyError('Atom')

    # Get the id of the active window
    proc = subprocess.run(
        ['xdotool', 'getactivewindow'],
        capture_output=True,
    )
    if proc.stdout.decode('utf-8').strip() == target_window:
        return
    proc = subprocess.run(['xdotool', 'windowactivate', target_window])


def shift_window():
    # pyautogui.keyDown('altleft')
    # pyautogui.press('\t')
    # pyautogui.keyUp('altleft')

    if IS_LINUX:
        return shift_window_linux()
    for window in gw.getAllWindows():
        if window.title.endswith('Atom'):
            # window.restore()
            window.activate()
            return
    raise KeyError('Atom')


def write_code(code):
    pyautogui.PAUSE = 2.0
    try:
        shift_window()
    except KeyError:
        return
    pyautogui.PAUSE = 0.25
    pyautogui.hotkey('ctrl', 'end')
    # pyautogui.write('\n\nHello world!', interval=0.25)
    pyautogui.write(f'\n\n{code}')
