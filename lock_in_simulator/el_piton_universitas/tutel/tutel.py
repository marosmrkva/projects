import turtle

for i in range(67):
    turtle.left(5.37)
    turtle.forward(2)
turtle.up()
turtle.forward(30)
turtle.down()
for i in range(67):
    turtle.left(5.37)
    turtle.forward(2)
turtle.up()
turtle.backward(5)
turtle.down()
turtle.right(90)
turtle.forward(100)
for i in range(36):
    turtle.right(5)
    turtle.forward(1)
turtle.right(90)
turtle.forward(22)
turtle.right(90)
for i in range(36):
    turtle.right(5)
    turtle.forward(1)
turtle.forward(100)
turtle.up()
turtle.forward(1000)

from tkinter import *

def vypis(eventa):  
    print("chuj w dupe")

t=Tk()
t.geometry("800x600+50+0")
t.title("dupa")
l = Label(t, text = "chuj w dupe")
l.place(x=650, y=30)
l12 = Label(t, text = "chuj w dupe")
l12.place(x=100, y=30)
b=Button(t, text = "chuj")
b.place(x=400, y=500)
b.bind("<Button-1>", vypis)
t.mainloop()