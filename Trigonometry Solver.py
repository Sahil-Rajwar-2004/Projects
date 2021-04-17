from tkinter import *
from tkinter import messagebox
import math

def about():
    messagebox.showinfo("Info","Tigonometry Calculator\nCreator: Sahil Rajwar")

def Exit():
    a = messagebox.askyesno("Notice","Are You Sure?!!")
    if a == True:
        exit()
    else:
        pass

def reset():
    sin_entry.delete(0,END)
    cos_entry.delete(0,END)
    tan_entry.delete(0,END)
    cosec_entry.delete(0,END)
    sec_entry.delete(0,END)
    cot_entry.delete(0,END)

def solve():
    sine = int(sin_entry.get())
    cosine = int(cos_entry.get())
    tangent = int(tan_entry.get())
    cosecant = int(cosec_entry.get())
    secant = int(sec_entry.get())
    cotangent = int(cot_entry.get())

    a = round(math.sin(sine),2)
    b = round(math.cos(cosine),2)
    c = round(math.tan(tangent),2)
    d = round(1/math.sin(cosecant),2)
    e = round(1/math.cos(secant),2)
    f = round(1/math.tan(cotangent),2)

    messagebox.showinfo("Answers",f"sin: {a}\ncos: {b}\ntan: {c}\ncosec: {d}\nsec: {e}\ncot: {f} ")
    
    """print(a)
    print(b)
    print(c)
    print(e)
    print(f)"""
    
win = Tk()
win.geometry("500x550")
win.title("Trigonometry")
win.configure(bg = "black")
win.resizable(0,0)

heading = Frame(win, bd = 6, relief = SUNKEN)
heading.pack(fill = BOTH, padx = 10, pady = 10)
heading_label = Label(heading, font = ("Comic sans ms",15,"bold","italic"), text = "Trigonometry")
heading_label.pack(fill = BOTH, padx = 10, pady = 10)

main_frame = Frame(win, bd = 6, relief = SUNKEN)
main_frame.pack(fill = BOTH, padx = 10, pady = 10)

title = Label(main_frame, text = ":Trigo Ratios:", font = ("Comic sans ms",12,"bold","italic"))
title.grid(row = 0, column = 0)
values = Label(main_frame, text = ":Angles:", font = ("Comic sans ms",12,"bold","italic"))
values.grid(row = 0, column = 1)

sin = Label(main_frame, text = "Sin: ", font = ("Comic sans ms",12))
sin.grid(row = 1, column = 0, padx = 10, pady = 10)
sin_entry = Entry(main_frame, font = ("Comic sans ms",12))
sin_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

cos = Label(main_frame, text = "Cos: ", font = ("Comic sans ms",12))
cos.grid(row = 2, column = 0, padx = 10, pady = 10)
cos_entry = Entry(main_frame, font = ("Comic sans ms",12))
cos_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

tan = Label(main_frame, text = "Tan: ", font = ("Comic sans ms",12))
tan.grid(row = 3, column = 0, padx = 10, pady = 10)
tan_entry = Entry(main_frame, font = ("Comic sans ms",12))
tan_entry.grid(row = 3, column = 1, padx = 10, pady = 10)

cosec = Label(main_frame, text = "Cosec: ", font = ("Comic sans ms",12))
cosec.grid(row = 4, column = 0, padx = 10, pady = 10)
cosec_entry = Entry(main_frame, font = ("Comic sans ms",12))
cosec_entry.grid(row = 4, column = 1, padx = 10, pady = 10)

sec = Label(main_frame, text = "Sec: ", font = ("Comic sans ms",12))
sec.grid(row = 5, column = 0, padx = 10, pady = 10)
sec_entry = Entry(main_frame, font = ("Comic sans ms",12))
sec_entry.grid(row = 5, column = 1, padx = 10, pady = 10)

cot = Label(main_frame, text = "Cot: ", font = ("Comic sans ms",12))
cot.grid(row = 6, column= 0, padx = 10, pady = 10)
cot_entry = Entry(main_frame, font = ("Comic sans ms",12))
cot_entry.grid(row = 6, column = 1, padx = 10, pady = 10)

btn_frame = Frame(win, bd = 6, relief = SUNKEN)
btn_frame.pack(fill = BOTH, padx = 10, pady = 10)
btn1 = Button(btn_frame, text = ":Solve:", font = ("Comic sans ms",12,"bold","italic"), bg = "grey", command = solve)
btn1.grid(row = 0, column = 0, padx = 10, pady = 10)
btn2 = Button(btn_frame, text = ":About:", font = ("Comic sans ms",12,"bold","italic"), bg = "grey", command = about)
btn2.grid(row = 0, column = 1, padx = 10, pady = 10)
btn3 = Button(btn_frame, text = ":Reset:", font = ("Comic sans ms",12,"bold","italic"), bg = "grey", command = reset)
btn3.grid(row = 0, column = 2, padx = 10, pady = 10)
btn4 = Button(btn_frame, text = ":Exit:", font = ("Comic sans ms",12,"bold","italic"), bg = "grey", command = Exit)
btn4.grid(row = 0, column = 3, padx = 10, pady = 10)

mainloop()
