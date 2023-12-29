from tkinter import *

def button_press(num):
    exp = input_text.get()
    exp = exp + str(num)
    input_text.set(exp)
    print(num)

def button_oper(oper):
    exp = input_text.get()
    exp = exp + oper
    input_text.set(exp)
    print(oper)

def equal():
    exp = input_text.get()
    ans = eval(exp)
    input_text.set(ans)
    print("equal")
win = Tk()
win.title("Calculator")
win.resizable(False,False)
display_frame = LabelFrame(win, text="Tkinter Calculator", relief=SUNKEN,padx=2, pady=2)
display_frame.grid(row=0, column=0, columnspan=4, padx=2, pady=4)

input_text = StringVar()


display = Entry(display_frame,textvariable=input_text,width=22)
display.pack(ipadx=12)
b0 = Button(win,text="0",padx=30,pady=30,command=lambda : button_press(0))
b1 = Button(win,text="1",padx=30,pady=30,command=lambda : button_press(1))
b2 = Button(win,text="2",padx=30,pady=30,command=lambda : button_press(2))
b3 = Button(win,text="3",padx=30,pady=30,command=lambda : button_press(3))
b4 = Button(win,text="4",padx=30,pady=30,command=lambda : button_press(4))
b5 = Button(win,text="5",padx=30,pady=30,command=lambda : button_press(5))
b6 = Button(win,text="6",padx=30,pady=30,command=lambda : button_press(6))
b7 = Button(win,text="7",padx=30,pady=30,command=lambda : button_press(7))
b8 = Button(win,text="8",padx=30,pady=30,command=lambda : button_press(8))
b9 = Button(win,text="9",padx=30,pady=30,command=lambda : button_press(9))
o1 = Button(win,text="+",padx=30,pady=30,command=lambda : button_oper('+'))
o2 = Button(win,text="-",padx=30,pady=30,command=lambda : button_oper('-'))
o3 = Button(win,text="*",padx=30,pady=30,command=lambda : button_oper('*'))
o4 = Button(win,text="/",padx=30,pady=30,command=lambda : button_oper('/'))
eq = Button(win,text="=",padx=30,pady=30,command=lambda : equal())
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
o1.grid(row=1,column=3)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
o2.grid(row=2,column=3)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
o3.grid(row=3,column=3)
o4.grid(row=4,column=0)
b0.grid(row=4,column=1)
eq.grid(row=4,column=2)


win.mainloop()