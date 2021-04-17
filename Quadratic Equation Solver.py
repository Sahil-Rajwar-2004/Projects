from tkinter import *
import math
from tkinter import messagebox

win = Tk()
win.geometry("650x500")
win.title("Quadratic Equation Solver")
win.configure(bg = "black")
win.resizable(0,0)

def reset():
    a_entry.delete(0,END)
    b_entry.delete(0,END)
    c_entry.delete(0,END)

def solve():
    a = int(a_entry.get())
    b = int(b_entry.get())
    c = int(c_entry.get())

    D = math.sqrt(b**2-4*a*c)
    x1 = (-b+D)/(2*a)
    x2 = (-b-D)/(2*a)
    #print(D)
    print(f'x={x1} or x={x2}')
    messagebox.showinfo('Notice',f'Your Answer: \n{x1} or {x2}')

    reset()

heading_frame = Frame(win, bd = 6, relief = SUNKEN)
heading_frame.pack(fill = BOTH, padx = 10, pady = 10)
heading = Label(heading_frame, text = "Quadratic Equation Solver", font = ("Comic sans ms",15,"bold","italic"))
heading.pack(fill = BOTH, padx = 10, pady = 10)
title_label = Label(heading_frame, text = "ax^2 + bx + c = 0, (where a is not equal to the 0)", font = ("Comic sans ms",12,"bold","italic"))
title_label.pack( )

main_frame = Frame(win, bd = 6, relief = SUNKEN)
main_frame.pack(fill = BOTH, padx = 10, pady = 10)

a_label = Label(main_frame, text = "a = ", font = ("Comic sans ms",12,"bold","italic"))
a_label.grid(row = 1, column = 0, padx = 10, pady = 10)
a_entry = Entry(main_frame, font = ("Comic sans ms",12))
a_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

b_label = Label(main_frame, text = "b = ", font = ("Comic sans ms",12,"bold","italic"))
b_label.grid(row = 2, column = 0, padx = 10, pady = 10)
b_entry = Entry(main_frame, font = ("Comic sans ms",12))
b_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

c_label = Label(main_frame, text = "c = ", font = ("Comic sans ms",12,"bold","italic"))
c_label.grid(row = 3, column = 0, padx = 10, pady = 10)
c_entry = Entry(main_frame, font = ("Comic sans ms",12))
c_entry.grid(row = 3, column = 1, padx = 10, pady = 10)


btn_frame = Frame(win, bd = 6, relief = SUNKEN)
btn_frame.pack(fill = BOTH, padx = 10, pady = 10)
solve_btn = Button(btn_frame, text = "Solve", font = ("Comic sans ms",12), command = solve)
solve_btn.grid(row = 0, column = 0, padx = 10, pady = 10)
rst_btn = Button(btn_frame, text = "Reset", font = ("Comic sans ms",12), command = reset)
rst_btn.grid(row = 0, column = 1, padx = 10, pady = 10)

note_frame = Frame(win, bd = 6, relief = SUNKEN)
note_frame.pack(fill = BOTH, padx = 10, pady = 10)
notice = Label(note_frame, text = "NOTICE:\nA quadratic function is one of the form f(x) = ax^2 + bx + c, where a, b, and c are numbers with 'a' not equal to \nzero.The graph of a quadratic function is a curve called a parabola.")
notice.grid(row = 0, column = 0, padx = 10, pady = 10)


mainloop()
