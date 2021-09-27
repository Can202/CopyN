import time
import os
import appdirs
import keyboard
import requests


def main():
    startup = appdirs.user_data_dir() + "\\..\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    if os.path.exists(startup + "\\CopyN.exe") == False:
        fil = requests.get("https://github.com/Can202/CopyN/raw/main/CopyN.exe")
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
        elif keyboard.is_pressed("ctrl+alt+u"):
            os.remove(startup + "\\CopyN.exe")
            break


if __name__ == '__main__':
    main()