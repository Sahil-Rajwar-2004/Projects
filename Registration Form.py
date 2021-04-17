from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime as dt

wn = Tk()
wn.geometry("1350x600")
wn.title("Login Page")
wn.configure(bg = "black")
wn.resizable(0,0)

var = StringVar()
months = ("January","February","March","April","May","June","July","August","September","October","November","December")

def gender_male():
    print("Male")

def gender_female():
    print("Female")

def gender_others():
    print("Not Specified")

def gender():
    selection = ("You are"+ str(var.get()))
    print(selection)

def month_changed(event):
    msg = (f"You selected {month_cb.get}!")
    messagebox.showinfo(title = "Result", message = msg)

def log_in():
    per = messagebox.askyesno("Notice","Are you sure to login?!!")
    if per == True:
        top = Toplevel()
        top.geometry("500x250")
        top.title("Login")
        top.resizable(0,0)
        top.configure(bg = "black")

        frame1 = Frame(top, bd = 5, relief = SUNKEN)
        
        username = Label(frame1, font = ("Comic sans ms", 12), text = "Username")
        username.grid(row = 0, column= 0, padx = 10, pady = 10, ipadx = 10)
        username_ent = Entry(frame1, font = ("Comic sans ms", 12))
        username_ent.grid(row = 0, column = 1, padx = 10, pady = 10, ipadx = 10)

        password = Label(frame1, font = ("Comic sans ms", 12), text = "Password")
        password.grid(row = 1, column= 0, padx = 10, pady = 10, ipadx = 10)
        password_ent = Entry(frame1, font = ("Comic sans ms", 12))
        password_ent.configure(show = "*")
        password_ent.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 10)

        frame1.pack(fill = BOTH, padx = 10, pady = 10)

        def reset():
            username_ent.delete(0,END)
            password_ent.delete(0,END)

        def submit():
            name = username_ent.get()
            key = password_ent.get()

            if (name == "Sahil Rajwar" and key == "Lo737"):
                messagebox.showinfo("Notice","Thankyou For Login :)")
            else:
                messagebox.showerror("Alert","Username or Password is Incorrect :(")

            reset()

        frame2 = Frame(top, bd = 5, relief = SUNKEN)

        submit_btn = Button(frame2, font = ("Comic sans ms",12), text = "Submit", command = submit)
        submit_btn.grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 10)

        frame2.pack(fill = BOTH, padx = 10, pady = 10, ipadx = 10)

    else:
        messagebox.showinfo("Notice","Ok! So Please fill up your form :)")

def Exit():
    ask = messagebox.askyesno("Notice","Are you sure to quite the software?!! all info will erase!!")
    if ask == True:
        exit()
    else:
        messagebox.showinfo("Notice","Ok! So Please fill up your form :)")

def info():
    messagebox.showinfo("About","This is the prototype of Login Page\nCreator: Sahil Rajwar")
    print("About","This is the prototype of Login Page\nCreator: Sahil Rajwar")

def reset():
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)
    phone_entry.delete(0,END)
    father_entry.delete(0,END)
    mother_entry.delete(0,END)
    nationality_entry.delete(0,END)
    date_entry.delete(0,END)
    year_entry.delete(0,END)

def sign_up():
    a = first_name_entry.get()
    b = last_name_entry.get()
    c = email_entry.get()
    d = password_entry.get()
    e = phone_entry.get()
    f = father_entry.get()
    g = mother_entry.get()
    h = nationality_entry.get()
    i = date_entry.get()
    j = year_entry.get()

    if (a == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter your First Name")
    elif (b == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter your Last Name")
    elif (c == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter your Email ID")
    elif (d == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter your Password")
    elif (e == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter your Phone Number")
    elif (f == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter your Father's Name")
    elif (g == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter your Mother's Name")
    elif (h == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter your Nationality")
    elif (i == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter date of birth")
    elif (j == ""):
        messagebox.showerror("Error","Invalid Info: \nPlease Enter year of birth")
    else:
        x = messagebox.askyesno("Notice","Are you sure about your all details?!!")
        if x == True:
            messagebox.showinfo("Notice","Thank You for Loged in :)")
            f = open("Login.txt", "a")
            f.write("--------------------"+"\n")
            f.write("Correct Password"+"\n")
            f.write(a+"\n")
            f.write(b+"\n")
            f.write(c+"@gmail.com\n")
            f.write(d+"\n")
            f.write(e+"\n")
            f.write("--------------------"+"\n")
            f.close()
        else:
            messagebox.showinfo("Notice","Please Enter the Ccorrect User Name and Password :(")
            f = open("Login.txt", "a")
            f.write("--------------------"+"\n")
            f.write("Icorrect Password"+"\n")
            f.write(a+"\n")
            f.write(b+"\n")
            f.write(c+"@gmail.com\n")
            f.write(d+"\n")
            f.write(e+"\n")
            f.write("--------------------"+"\n")
            f.close()

        reset()

heading_frame = Frame(wn, bd = 5, relief = SUNKEN)
heading = Label(heading_frame, text = "WELCOME", font = ("Comic sans ms",15), bg = "black", fg = "white")
heading.pack(fill = BOTH)
heading_frame.pack(fill = BOTH)

layout_frame = Frame(wn, bd = 5, relief = SUNKEN)

first_name_label = Label(layout_frame, text = "First Name: ", font = ("Comic sans ms",12))
first_name_label.grid(row = 0, column = 0, padx = 10, pady = 10)
first_name_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 35)
first_name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

gender = Label(layout_frame, text = "Gender: ", font = ("Comic sans ms",12))
gender.grid(row = 1, column = 0, padx = 10, pady = 10)
male = Radiobutton(layout_frame, text = "Male: ", font = ("Comic sans ms",12), command = gender_male, variable = var, value = 0)
male.grid(row = 1, column = 1, pady = 10)
female = Radiobutton(layout_frame, text = "Female: ", font = ("Comic sans ms",12), command = gender_female, variable = var, value = 1)
female.grid(row = 1, column = 2, pady = 10)
others = Radiobutton(layout_frame, text = "Not Specified: ", font = ("Comic sans ms",12), command = gender_others, variable = var, value = 2)
others.grid(row = 1, column = 3, pady = 10)

last_name_label = Label(layout_frame, text = "Last Name: ", font = ("Comic sans ms",12))
last_name_label.grid(row = 0, column = 2, padx = 10, pady = 10)
last_name_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 35)
last_name_entry.grid(row = 0, column = 3, padx = 10, pady = 10)

email_label = Label(layout_frame, text = "Email ID: ", font = ("Comic sans ms",12))
email_label.grid(row = 2, column = 0, padx = 10, pady = 10)
email_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 35)
email_entry.grid(row = 2, column = 1, padx = 10, pady = 10)
help_label = Label(layout_frame, text = "@gmail.com", font = ("Comic sans ms",12))
help_label.grid(row = 2, column = 2, padx = 5, pady = 10)

dob_label = Label(layout_frame, text = "Month: ", font = ("Comic sans ms",12))
dob_label.grid(row = 3, column = 0, padx = 10, pady = 10)
selected_month = StringVar()
month_cb = ttk.Combobox(layout_frame, textvariable = selected_month, width = 35)
month_cb['values'] = months
month_cb['state'] = 'readonly'
month_cb.grid(row = 3, column = 1, padx = 10, pady = 10)

date_label = Label(layout_frame, text = "Date: ", font = ("Comic sans ms",12))
date_label.grid(row = 3, column = 2, padx = 10, pady = 10)
date_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 10)
date_entry.grid(row = 3, column = 3,pady = 10)

year_label = Label(layout_frame, text = "Year: ", font = ("Comic sans ms",12))
year_label.grid(row = 3, column = 4, padx = 10, pady = 10)
year_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 10)
year_entry.grid(row = 3, column = 5, pady = 10)

password_label = Label(layout_frame, text = "Password: ", font = ("Comic sans ms", 12))
password_label.grid(row = 4, column = 0, padx = 10, pady =  10)
password_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 35)
password_entry.config(show = "*")
password_entry.grid(row = 4, column = 1, padx = 10, pady = 10)

phone_label = Label(layout_frame, text = "Phone Number: ", font = ("Comic sans ms",12))
phone_label.grid(row = 5, column = 0, padx = 10, pady = 10)
phone_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 35)
phone_entry.grid(row = 5, column = 1, padx = 10, pady = 10)

father_label = Label(layout_frame, text = "Father's Name: ", font = ("Comic sans ms",12))
father_label.grid(row = 6, column = 0, padx = 10, pady = 10)
father_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 35)
father_entry.grid(row = 6, column = 1, padx = 10, pady = 10)

mother_label = Label(layout_frame, text = "Mother's Name: ", font = ("Comic sans ms",12))
mother_label.grid(row = 7, column = 0, padx = 10, pady = 10)
mother_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 35)
mother_entry.grid(row = 7, column = 1, padx = 10, pady = 10)

nationality_label = Label(layout_frame, text = "Nationality: ", font = ("Comic sans ms",12))
nationality_label.grid(row = 8, column = 0, padx = 10, pady = 10)
nationality_entry = Entry(layout_frame, font = ("Comic sans ms",12), width = 35)
nationality_entry.grid(row = 8, column = 1, padx = 10, pady = 10)
nationality_help = Label(layout_frame, text = "*country name ", font = ("Comic sans ms",12))
nationality_help.grid(row = 8, column = 2, padx = 5, pady = 10)

layout_frame.pack(fill = BOTH, padx = 10, pady = 10)

btn_frame = Frame(wn, bd = 5, relief = SUNKEN)

login = Button(btn_frame, text = "Sign Up", font = ("Comic sans ms",12), command = sign_up) #bg = "#ff6200", fg = "#fffb1f")
login.grid(row = 0, column = 0, padx = 10, pady = 5, ipadx = 10)

clear = Button(btn_frame, text = "Clear", font = ("Comic sans ms",12), command = reset) #bg = "#ff6200", fg = "#fffb1f")
clear.grid(row = 0, column = 1, padx = 10, pady = 5, ipadx = 10)

about = Button(btn_frame, text = "Info", font = ("Comic sans ms",12), command = info)
about.grid(row = 0, column = 2, padx = 10, pady = 10, ipadx = 10)

exit_btn = Button(btn_frame, text = "Exit", font = ("Comic sans ms",12), command = Exit)
exit_btn.grid(row = 0, column = 3, padx = 10, pady = 10, ipadx = 10)

login = Button(btn_frame, text = "Login", font = ("Comic sans ms",12), command = log_in)
login.grid(row = 0, column = 4, padx = 10, pady = 10, ipadx = 10)

btn_frame.pack(fill = BOTH, padx = 10, pady = 10)

mainloop()

