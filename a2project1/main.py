class Icon:
    def __init__(self):
        self.icon = ""
        self.number1 = 1
        self.number2 = 2
        self.numner3 = 3
        self.number4 = 4
        self.number5 = 5
        self.number6 = 6
        self.number7 = 7
        self.number8 = 8
        self.number9 = 9
        self.number0 = 0

from tkinter import *
import easygui 
import math


master = Tk()

frame = Frame(master)  #framework construction
 
frame.pack(padx = 20,pady = 20)

a=''
v1=StringVar()
Entry(frame,width=15,textvariable=v1,validate='key',\
           validatecommand=('%p')).grid(row=0,column=3)

def num1():
    global a
    global v1
    a=str(v1.get())+str(1)
    v1.set(a)
    f
    f.seek(1000,1)
    
def num2():
    global a
    global v1
    a=str(v1.get())+str(2)
    v1.set(a)
   
def num3():
    global a
    global v1
    a=str(v1.get())+str(3)
    v1.set(a)
   
def num4():
    global a
    global v1
    a=str(v1.get())+str(4)
    v1.set(a)
    
def num5():
    global a
    global v1
    a=str(v1.get())+str(5)
    v1.set(a)
   
def num6():
    global a
    global v1
    a=str(v1.get())+str(6)
    v1.set(a)
    
def num7():
    global a
    global v1
    a=str(v1.get())+str(7)
    v1.set(a)
   
def num8():
    global a
    global v1
    a=str(v1.get())+str(8)
    v1.set(a)
    
def num9():
    global a
    global v1
    a=str(v1.get())+str(9)
    v1.set(a)
    
def num0():
    global a
    global v1
    a=str(v1.get())+str(0)
    v1.set(a)
    
def dot():
    global a
    global v1
    a=str(v1.get())+'.'
    v1.set(a)
    
def plus():
    global a
    global v1
    a=str(v1.get())+'+'
    v1.set(a)
    
def sub():
    global a
    global v1
    a=str(v1.get())+'-'
    v1.set(a)
  
def multi():
    global a
    global v1
    a=str(v1.get())+'*'
    v1.set(a)
    
def div():
    global a
    global v1
    a=str(v1.get())+'/'
    v1.set(a)
def sin():
    global a
    global v1
    a=str(v1.get())+'math.sin()'
    v1.set(a)
def cos():
    global a
    global v1
    a=str(v1.get())+'math.cos()'
    v1.set(a)
def tan():
    global a
    global v1
    a=str(v1.get())+'math.tan()'
    v1.set(a)
def square():
    global a
    global v1
    a=str(v1.get())+'**2'
    v1.set(a)
def cube():
    global a
    global v1
    a=str(v1.get())+'**3'
    v1.set(a)
def power():
    global a
    global v1
    a=str(v1.get())+'**'
    v1.set(a)
def sqrt():
    global a
    global v1
    a=str(v1.get())+'math.sqrt()'
    v1.set(a)
def pi():
    global a
    global v1
    a=str(v1.get())+'math.pi'
    v1.set(a)
def e():
    global a
    global v1
    a=str(v1.get())+'math.e'
    v1.set(a)
def log():
    global a
    global v1
    a=str(v1.get())+'math.log()'
    v1.set(a)
def reciprocal():
    global a
    global v1
    a=str(v1.get())+'**-1'
    v1.set(a)
def clear():
    global a
    global v1
    a=''
    v1.set(a)
def calc():
    global a
    global v1
    a=str(v1.get())
    a=str(eval(a))
    v1.set(a)
Button(frame,text='  ㏒   ',command=log).grid(row=1,column=0,pady=5) 
Button(frame,text='  1/X  ',command=reciprocal).grid(row=2,column=0,pady=5)
Button(frame,text='  X³  ',command=cube).grid(row=3,column=0,pady=5)
Button(frame,text='  X²  ',command=square).grid(row=4,column=0,pady=5)
Button(frame,text='  Xⁿ  ',command=power).grid(row=1,column=1,padx=40,pady=5) 
Button(frame,text='  √  ',command=sqrt).grid(row=2,column=1,pady=5)
Button(frame,text='  e  ',command=e).grid(row=3,column=1,pady=5)
Button(frame,text='  π  ',command=pi).grid(row=4,column=1,pady=5)
Button(frame,text='   C   ',command=clear).grid(row=1,column=2,pady=5) 
Button(frame,text='  sin  ',command=sin).grid(row=2,column=2,pady=5)
Button(frame,text='  cos  ',command=cos).grid(row=3,column=2,pady=5)
Button(frame,text='  tan  ',command=tan).grid(row=4,column=2,pady=5)
Button(frame,text='  7  ',command=num7).grid(row=1,column=3,padx=40,pady=5) 
Button(frame,text='  4  ',command=num4).grid(row=2,column=3,pady=5)
Button(frame,text='  1  ',command=num1).grid(row=3,column=3,pady=5)
Button(frame,text='  0  ',command=num0).grid(row=4,column=3,pady=5)
Button(frame,text='  8  ',command=num8).grid(row=1,column=4,pady=5)
Button(frame,text='  5  ',command=num5).grid(row=2,column=4,pady=5)
Button(frame,text='  2  ',command=num2).grid(row=3,column=4,pady=5)
Button(frame,text='  .  ',command=dot).grid(row=4,column=4,pady=5)
Button(frame,text='  9  ',command=num9).grid(row=1,column=5,padx=40,pady=5)
Button(frame,text='  6  ',command=num6).grid(row=2,column=5,pady=5)
Button(frame,text='  3  ',command=num3).grid(row=3,column=5,pady=5)
Button(frame,text='  ÷  ',command=div).grid(row=4,column=5,pady=5)
Button(frame,text='  +  ',command=plus).grid(row=1,column=6,pady=5)
Button(frame,text='  -  ',command=sub).grid(row=2,column=6,pady=5)
Button(frame,text='  ×  ',command=multi).grid(row=3,column=6,pady=5)
Button(frame,text='  =  ',command=calc).grid(row=4,column=6,pady=5)

mainloop()
