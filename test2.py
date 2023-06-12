from tkinter import *

keys = set()


def keyReleaseHandler(event):
    if event.keycode in keys:
        keys.remove(event.keycode)


def keyPressHandler(event):
    keys.add(event.keycode)


window = Tk()
window.geometry("640x480")

window.bind("<KeyPress>", keyPressHandler)
window.bind("<KeyRelease>", keyReleaseHandler)

while True:
    #
    if (len(keys) > 0):
        print("Key: ", keys)
    #
    window.after(33)
    window.update()