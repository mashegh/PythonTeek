from tkinter import*
def fornownothing():
    filewin = Toplevel(tk)
    button = Button(filewin, text='do nothing button')
    button.pack()
tk=Tk()
menuber = Menu(tk)
tk.config(menu=menuber)



filemenu = Menu(menuber, tearoff=0)
menuber.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='save', command=fornownothing)
filemenu.add_command(label='recent files', command=fornownothing)
filemenu.add_command(label='open', command=fornownothing)
filemenu.add_command(label='exit', command=tk.quit)
filemenu.add_command(label='close', command=fornownothing)
filemenu.add_command(label='print window', command=fornownothing)
filemenu.add_command(label='save copy as', command=fornownothing)
filemenu.add_command(label='ope module', command=fornownothing)
filemenu.add_command(label='path browser', command=fornownothing)
filemenu.add_command(label='module browser', command=fornownothing)

































































































































































