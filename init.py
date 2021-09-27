import time
import os
import appdirs
import keyboard
import requests


def main():
    startup = appdirs.user_data_dir() + "\\..\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    if os.path.exists(startup + "\\CopyN.exe") == True:
        fil = requests.get("url")
        with open(startup + "\\CopyN.exe", 'wb') as f:
            f.write(fil.content)
            f.close()
    while True:
        if keyboard.is_pressed("ctrl+alt+x"):
            keyboard.release("x")
            keyboard.release("ctrl")
            keyboard.release("alt")
            keyboard.press("ñ")
            time.sleep(.5)
        elif keyboard.is_pressed("ctrl+alt+q"):
            break


if __name__ == '__main__':
    main()