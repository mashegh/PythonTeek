from tkinter import*
tk= Tk()
tk.title("Calculator")

entry =Entry(tk, width=30, bd=10, bg='gold')
entry.grid(row=0, column=0, columnspan=4)
def button_click(number):
    entry.insert(END, str (number))
def button_clear():
     entry.delete(0,END)
def button_equal():
     expression= entry.get()
     try:
          result = eval (expression)
          entry. delete(0, END)
          entry.insert(0, result)
     except Exception as e:
          entry. delete (0, END)
          entry.insert(0, 'error')
     
addition = Button ( tk,  text='+', width=7,height=2,
                    command= lambda:button_click('+')).grid(row=1, column=3)
subtraction = Button ( tk,  text='-', width=7,height=2,
                       command= lambda:button_click('-')).grid(row=2, column=3)
multiply = Button (tk, text='*', width=7, height=2,
                   command= lambda:button_click('*')).grid(row=3, column=3)
division = Button (tk, text='/', width=7, height=2,
                   command= lambda:button_click('/')).grid(row=4, column=3)     
btn7 =Button(tk, text='7', width=7, height =2,command=lambda:button_click(7) ).grid( row=1, column=0)
btn8 =Button(tk, text='8', width=7, height =2,command=lambda:button_click(8) ).grid( row=1, column=1)
btn9 =Button(tk, text='9', width=7, height =2,command=lambda:button_click(9) ).grid( row=1, column=2)
btn4 =Button(tk, text='4', width=7, height =2,command=lambda:button_click(4) ).grid( row=2, column=0)
btn5 =Button(tk, text='5', width=7, height =2,command=lambda:button_click(5) ).grid( row=2, column=1)
btn6 =Button(tk, text='6', width=7, height =2,command=lambda:button_click(6) ).grid( row=2, column=2)
btn1 =Button(tk, text='1', width=7, height =2,command=lambda:button_click(1) ).grid( row=3, column=0)
btn2 =Button(tk, text='2', width=7, height =2,command=lambda:button_click(2) ).grid( row=3, column=1)
btn3 =Button(tk, text ='3', width=7, height =2,command=lambda:button_click(3) ).grid (row=3, column=2)
btn0 =Button(tk, text ='0', width=7, height =2,command=lambda:button_click(0) ).grid (row=4, column=0)

button_clear= Button(tk,  text='c', width=7, height =2,command=button_clear).grid(row=4, column=1)    
button_equal= Button(tk,  text='=', width=7, height =2,command=button_equal).grid(row=4, column=2)    




