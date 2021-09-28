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
        keyboard.add_hotkey('ctrl+alt+x', lambda: write("ñ"))
        keyboard.add_hotkey('ctrl+alt+q', lambda: byebye())
        keyboard.add_hotkey('ctrl+alt+u', lambda: remove())
        keyboard.wait()
def remove():
    print("removing")
    os.remove(appdirs.user_data_dir() + "\\..\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\CopyN.exe")
    quit()
def write(string):
    print(string)
    time.sleep(.15)
    keyboard.write("ñ")

def byebye():
    quit()
if __name__ == '__main__':
    main()