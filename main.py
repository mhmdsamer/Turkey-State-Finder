import turtle
from tkinter import messagebox
import pandas as pd
import time
import csv

window = turtle.Screen()
turtle.getscreen()._root.state('zoomed') # to maximize the picture size
# window.setup(width= 1200, height= 600)
window.title("Turkey States Game")
image = "unnamed.gif"          # empty map
window.addshape(image)
turtle.shape(image)

turkiyeMap = pd.read_csv("DS.csv")
named = []
unnamed = []


while len(named) < 80:
    Map = turkiyeMap.Name.to_list()
    specificState = window.textinput(title=f"{len(named)}/81 States Correct", prompt="Name a State").title()
    if specificState == "Solve":
        for i in Map:
            data = turkiyeMap[turkiyeMap.Name == i]
            featherPen = turtle.Turtle()
            featherPen.hideturtle()
            featherPen.penup()
            featherPen.goto(int(data.X), int(data.Y))
            featherPen.write(i)
    specificState.title()
    if (specificState in Map):
        if specificState in named:
            messagebox.showinfo("Error", "The State has been chosen")  # warning message.

        else:
         named.append(specificState)
         print(named[0])
         featherPen = turtle.Turtle()
         featherPen.hideturtle()
         featherPen.penup()


         answerdata = turkiyeMap[turkiyeMap.Name == specificState]
         featherPen.goto(int(answerdata.X), int(answerdata.Y))
         featherPen.write(specificState.title())

    else:
        messagebox.showinfo("error","this state is not in turkey") # warning massege
