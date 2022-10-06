import time
from pynput import keyboard
import keyboard as kb
import os
from sys import exit
import webbrowser

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift_l, keyboard.Key.enter},
    {keyboard.Key.shift_l, keyboard.KeyCode(char='w')},
    {keyboard.Key.shift_l, keyboard.KeyCode(char='W')},
    {keyboard.Key.shift_l, keyboard.KeyCode(char='x')},
    {keyboard.Key.shift_l, keyboard.KeyCode(char='X')}
]  

# The currently active modifiers
current = set()

def open_terminal():
    os.system(f'start C:\\Users\\Jesus\\AppData\Local\\Microsoft\\WindowsApps\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\wt.exe')
    time.sleep(1)
    kb.write('python .\\tasker.py')
    time.sleep(1)
    
def open_opera():
     webbrowser.open(f'https://you.com/code')
     time.sleep(2)

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)

        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            if current.__contains__(keyboard.Key.shift_l) and current.__contains__(keyboard.Key.enter):
                open_terminal()
            elif current.__contains__(keyboard.Key.shift_l) and (current.__contains__(keyboard.KeyCode(char='w')) or current.__contains__(keyboard.KeyCode(char='W'))):
                open_opera()
            elif current.__contains__(keyboard.Key.shift_l) and (current.__contains__(keyboard.KeyCode(char='x')) or current.__contains__(keyboard.KeyCode(char='X'))):
                exit()
            current.clear()
            time.sleep(1)
            
def on_release(key):
    try:
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)
    except:
        print("Excepción controlada")
        
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()