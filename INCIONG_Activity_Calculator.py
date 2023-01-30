from tkinter import *
win = Tk()

# add widgets from here

win.geometry("300x550+10+20")
win.title("Calculator")
win.configure(bg="White")

# add button widgets
btn = Button(win,text="C", fg="White",font=("Verdana",15),bd=5,activebackground="DarkOrange", activeforeground="White",height=2,width=4,bg="Orange",command=lambda: clear())
btn.place(x = 10,y=150)

btn2 = Button(win,text="÷", fg="White",font=("Verdana",15),bd=5, activebackground="White", activeforeground="Black",height=2,width=4,bg="Black",command=lambda: show("/"))
btn2.place(x = 80,y=150)

btn3 = Button(win,text="x", fg="White",font=("Verdana",15),bd=5,activebackground="White", activeforeground="Black",height=2,width=4,bg="Black",command=lambda: show("*"))
btn3.place(x = 150,y=150)

btn4 = Button(win,text="⌫", fg="White",font=("Verdana",15), bd=5, activebackground="White", activeforeground="Black",height=2,width=4,bg="Black",command=lambda: backspace())
btn4.place(x = 220,y=150)

btn5 = Button(win,text="7", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("7"))
btn5.place(x = 10,y=227)

btn6 = Button(win,text="8", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("8"))
btn6.place(x = 80,y=227)

btn7 = Button(win,text="9", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("9"))
btn7.place(x = 150,y=227)

btn8 = Button(win,text="-", fg="White",font=("Verdana",15), bd=5, activebackground="White", activeforeground="Black",height=2,width=4,bg="Black",command=lambda: show("-"))
btn8.place(x = 220,y=227)

btn9 = Button(win,text="4", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("4"))
btn9.place(x = 10,y=304)

btn10 = Button(win,text="5", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("5"))
btn10.place(x = 80,y=304)

btn11 = Button(win,text="6", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("6"))
btn11.place(x = 150,y=304)

btn12 = Button(win,text="+", fg="White",font=("Verdana",15), bd=5, activebackground="White", activeforeground="Black",height=2,width=4,bg="Black",command=lambda: show("+"))
btn12.place(x = 220,y=304)

btn13 = Button(win,text="1", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("1"))
btn13.place(x = 10,y=381)

btn14 = Button(win,text="2", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("2"))
btn14.place(x = 80,y=381)

btn15 = Button(win,text="3", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("3"))
btn15.place(x = 150,y=381)

btn16 = Button(win,text="=", fg="White",font=("Verdana",15), bd=5, activebackground="DarkOrange", activeforeground="White",height=5,width=4, bg="Orange",command=lambda: calculate())
btn16.place(x = 220,y=382)

btn17 = Button(win,text="%", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("%"))
btn17.place(x = 10,y=458)

btn18 = Button(win,text="0", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("0"))
btn18.place(x = 80,y=458)

btn19 = Button(win,text=".", fg="White",font=("Verdana",15), bd=5, activebackground="Grey", activeforeground="White",height=2,width=4,bg="Grey",command=lambda: show("."))
btn19.place(x = 150,y=458)

# add label widgets
label_result = Label(win,height=2,width=21,text="",font=("Verdana",15))
label_result.place(x = 10,y=3)

label_result1 = Label(win,height=3,width=21,text="",font=("Verdana",15))
label_result1.place(x = 10,y=66)

#prints,enter,and calculate values from calculator
equation = ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation, anchor='e')

def clear():
    global equation
    equation= ""
    label_result.config(text=equation)
    label_result1.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
    label_result1.config(text=result)

def backspace():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)
    label_result1.config(text="")


win.mainloop()
