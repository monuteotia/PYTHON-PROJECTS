#CALCULATOR
#INTERMEDIATE PROJECT

from tkinter import *

screen =Tk()  #making a screen
screen.title('My Calculator')   #title of the screen
screen.geometry('365x490')  #size of the window created


tex = StringVar()
operator = ''


def click(number):
    global operator
    operator += str(number)
    tex.set(operator)


def clear():
    global operator
    operator = ''
    tex.set(operator)
    

def equal():
    global operator
    result = eval(operator)
    operator = str(result)
    tex.set(result)
    


entry1 = Entry(screen,bg='red',font=('arial',20,'italic bold'),bd=30,justify='right',textvariable=tex)   #blank creation
entry1.grid(row=0,columnspan=4)


btn7 = Button(screen,text='7',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7),activebackground='yellow',activeforeground='red',bg='powder blue')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8),activebackground='yellow',activeforeground='red',bg='powder blue')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9),activebackground='yellow',activeforeground='red',bg='powder blue')
btn9.grid(row=1,column=2)

btnadd = Button(screen,text='+',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+'),activebackground='yellow',activeforeground='red',bg='powder blue')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4),activebackground='yellow',activeforeground='red',bg='powder blue')
btn4.grid(row=2,column=2)

btn5 = Button(screen,text='5',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5),activebackground='yellow',activeforeground='red',bg='powder blue')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text='6',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6),activebackground='yellow',activeforeground='red',bg='powder blue')
btn6.grid(row=2,column=0)

btnsub = Button(screen,text='-',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('-'),activebackground='yellow',activeforeground='red',bg='powder blue')
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text='1',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1),activebackground='yellow',activeforeground='red',bg='powder blue')
btn1.grid(row=3,column=0)

btn2 = Button(screen,text='2',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2),activebackground='yellow',activeforeground='red',bg='powder blue')
btn2.grid(row=3,column=1)

btn3 = Button(screen,text='3',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3),activebackground='yellow',activeforeground='red',bg='powder blue')
btn3.grid(row=3,column=2)

btnmul = Button(screen,text='*',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('*'),activebackground='yellow',activeforeground='red',bg='powder blue')
btnmul.grid(row=3,column=3)

btn0 = Button(screen,text='0',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0),activebackground='yellow',activeforeground='red',bg='powder blue')
btn0.grid(row=4,column=0)

btnclear = Button(screen,text='C',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:clear(),activebackground='yellow',activeforeground='red',bg='powder blue')
btnclear.grid(row=4,column=1)

btnequal = Button(screen,text='=',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=equal,activebackground='yellow',activeforeground='red',bg='powder blue')
btnequal.grid(row=4,column=2)

btndiv = Button(screen,text='/',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('/'),activebackground='yellow',activeforeground='red',bg='powder blue')
btndiv.grid(row=4,column=3)


screen.mainloop()   #making run the loop again and again