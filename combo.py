from tkinter import *
from tkinter import ttk
tk=Tk()
tk.title('mas')
label=Label(tk, text='your year')
label.grid(row=0,column=0)
combomasiha=[2015,2016, 2017,1000000]
combo=ttk.Combobox(tk,values=combomasiha)
combo.grid(row=0,column=1)
label=Label(tk, text='your month')
label.grid(row=1,column=0)
month=['july', 'june']
combo1=ttk.Combobox(tk,values=month)
combo1.grid(row=1,column=1)
label=Label(tk, text='your day')
label.grid(row=2,column=0)
month=[1,2,3,4,5,9 ,31]
combo2=ttk.Combobox(tk,values=month)
combo2.grid(row=2,column=1)
def birthday():
    selected_years=combo.get()
    selected_months=combo1.get()
    selected_days=combo2.get()
    if selected_months and selected_days and selected_years:
        result_label.config (text=f'your birthday is {selected_years} {selected_months} {selected_days}')
button=Button(tk, text='check', command=birthday)
button.grid(row=3,column=1)
result_label=Label(tk,text='')
result_label.grid(pady=10)
mainloop()
        

    
    
    
