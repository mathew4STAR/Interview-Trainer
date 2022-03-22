import eyedetector
from tkinter import *
import cv2
from PIL import Image, ImageTk

root = Tk()
title = Label(root, text="Interview Trainer")
title.pack()
question = Label(root, text= "Question 1 this is very cool who are you?")
question.pack()
nxtquestion = Button(root)
nxtquestion.pack()
screen1 = LabelFrame(root)
screen1.pack()
screen2 = Label(screen1)
screen2.pack()
focus = Label(root, text="starting")
iris = Label(root, text="starting")
focus.pack()
iris.pack()

while True:
    tracker = eyedetector.track(False)
    cam = cv2.cvtColor(tracker[2], cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(cam))
    screen2["image"] = img
    focus["text"] = tracker[0]
    iris["text"] = tracker[1]
    root.update()
cv2.destroyAllWindows()
