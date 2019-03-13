from tkinter import *




def input_window():
    root = Tk()
    b = 0
    for i in range(3):
        for j in range(3):
            b = (i*3 + j +1)
            Button(root, text = str(b), borderwidth = 1 ).grid(row = 4-i, column = j)
    root.mainloop()
print("hi")

input_window()