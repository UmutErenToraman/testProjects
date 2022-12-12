from tkinter import *
from tkinter import messagebox
import string
import random
import Function



s1 = string.ascii_letters
s2 = "1234567890"
s3 = "._!&"
def write(a):
    entry.insert(0, a)

def recommended_password():
    a = ""
    for i in range(3):
        b = random.choice(s1)
        c = random.choice(s2)
        d = random.choice(s3)
        a = a + b + c + d

    recommended_button= Button(window,
                              text="Use the recommended password "+a,
                              font=("Consolas", 15, "bold"),
                              bg="black",
                              fg="green",
                              command=lambda: write(a)
                               )
    recommended_button.place(x=200, y=160)

def check():
    passw=list(entry.get())
    if len(passw)<8:
        messagebox.showwarning(title="WARNING",
                               message="Your password must contain at least 8 characters",
                               )
        return 0

    x=Function.list_contains(passw,s1)
    if x==0:
        messagebox.showwarning(title="WARNING",
                               message="Your password must contain letters")
        return 0
    x = Function.list_contains(passw, s2)
    if x == 0:
        messagebox.showwarning(title="WARNING",
                               message="Your password must contain numbers")
        return 0
    x = Function.list_contains(passw, s3)
    if x == 0:
        messagebox.showwarning(title="WARNING",
                               message="Your password must contain characters such as '._!&' ")
        return 0

    else:
        messagebox.showinfo(title="INFO",
                               message="Your password has been saved.",
                            )

        return 1

def visible():

    if entry.cget('show')=='*':
        entry.config(show='')
    else:
        entry.config(show='*')

app_height=350
app_width=750

window = Tk()

window.title("Password Suggester")
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(app_width/2))
y=int((screen_height/2)-(app_height/2))
window.geometry(f"{app_width}x{app_height}+{x}+{y}")
window.config(background="black")

recommended_password()

label=Label(window,
            text="Password Suggester",
            font=("Consolas",17,"bold"),
            bg="black",
            fg="green",
            )
label.place(x=280, y=25)

label2=Label(window,
            text="Enter a password which contains at least 8 characters (number,punctuation mark and letter)",
            font=("Consolas",10,"bold"),
            bg="black",
            fg="green"
)
label2.place(x=80,y=60)


entry=Entry(window,
            font=("Consolas",18,"bold"),
            bg="black",
            fg="green",
            show="*")
entry.place(x=270,y=90)

button=Button(window,
              text="SUBMIT",
              font=("Consolas",12,"bold"),
              fg="green",
              bg="black",
              activeforeground="green",
              activebackground="black",
              command=check)
button.place(x=380, y=230)


check_button=Checkbutton(window,
                         text="Show Text",
                          font=("Consolas",12,"bold"),
                          fg="green",
                          bg="black",
                          activeforeground="green",
                          activebackground="black",
                         command=visible)
check_button.place(x=270,y=130)

window.mainloop()

