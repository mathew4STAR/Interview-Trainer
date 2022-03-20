import eyedetector
from tkinter import *
import cv2
from PIL import Image, ImageTk
from serial import Serial
import random

def getQuestions():
    sub = subject.get()
    path = "data/Questions/" + sub + ".txt"
    data = open(path, "r")
    val = data.read()
    val = val.split("\n")
    qnum = random.randint(0,10)
    question["text"] = val[qnum]


root = Tk()
title = Label(root, text="Interview Trainer")
title.pack()
question = Label(root, text= "Can you name the four types of @media properties?")
question.pack()
subject = Entry(root, text="Subject")
subject.pack()
nxtquestion = Button(root, command=getQuestions, text="Next Question")
nxtquestion.pack()
screen1 = LabelFrame(root)
screen1.pack()
screen2 = Label(screen1)
screen2.pack()
focus = Label(root, text="Back is straight")
iris = Label(root, text="Looking Straight")
focus.pack()
iris.pack()


while True:
    tracker = eyedetector.track(False)
    img = ImageTk.PhotoImage(Image.fromarray(tracker[2]))
    screen2["image"] = img
    focus["text"] = tracker[0]
    iris["text"] = tracker[1]
    root.update()
cv2.destroyAllWindows()
