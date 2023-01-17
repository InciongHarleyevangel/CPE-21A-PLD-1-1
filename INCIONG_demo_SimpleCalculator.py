from tkinter import *
class MyWindow:
    def __init__(self,win):

#widgets start from here
        self.lbl1 = Label(win,text="1st Number")
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text= "2nd Number")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100,y=150)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=200,y=50)
        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=200,y=100)
        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=200,y=150)
        self.btnadd = Button(win,text="Add")
        self.btnadd.place(x=100,y=200)
        self.btnsub = Button(win,text="Sub")
        self.btnsub.place(x=150,y=200)
        self.btnmul = Button(win,text="Mul")
        self.btnmul.place(x=200,y=200)
        self.btndiv = Button(win,text="Div")
        self.btndiv.place(x=250,y=200)
        self.btnclr = Button(win,text="Clear All")
        self.btnclr.place(x=300,y=200)
        self.btnadd.bind('<Button-1>',self.add)
        self.btnsub.bind('<Button-1>',self.sub)
        self.btnmul.bind('<Button-1>',self.mul)
        self.btndiv.bind('<Button-1>',self.div)
        self.btnclr.bind('<Button-1>',self.clr)

#add event-handling /bind () method

    def add(self,add):
        self.txt3.delete(0, 'end')
        num1 = float(self.txt1.get())
        num2 = float(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END,str(result))

    def sub(self,sub):
        self.txt3.delete(0, 'end')
        num1 = float(self.txt1.get())
        num2 = float(self.txt2.get())
        result = num1-num2
        self.txt3.insert(END, str(result))

    def mul(self,mul):
        self.txt3.delete(0, 'end')
        num1 = float(self.txt1.get())
        num2 = float(self.txt2.get())
        result = num1*num2
        self.txt3.insert(END, str(result))

    def div(self,div):
        self.txt3.delete(0, 'end')
        num1 = float(self.txt1.get())
        num2 = float(self.txt2.get())
        result = num1/num2
        self.txt3.insert(END, str(result))

    def clr(self,clr):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("400x400+10+10")
window.title("Simple Calculator")
window.mainloop()
