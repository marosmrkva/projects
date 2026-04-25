import tkinter as tk

m = tk.Tk()


rovnica = ""

def print1():
    global rovnica

    rovnica += "1" #"" + "1" = "1"
    text1.config(text=rovnica)

def print2():
    global rovnica

    rovnica += "2" #"" + "1" = "1"
    text1.config(text=rovnica)

def print3():
    global rovnica

    rovnica += "3" #"" + "1" = "1"
    text1.config(text=rovnica)

text1 = tk.Label(m, text="0", font="comicsans 30")
text1.grid(row = 1, column = 2)

button1 = tk.Button(m, text="1", command=print1)
button1.grid(row = 2, column = 1)

button2 = tk.Button(m, text="2", command=print2)
button2.grid(row = 2, column = 2)

button3 = tk.Button(m, text="3", command=print3)
button3.grid(row = 2, column = 3)
m.mainloop()