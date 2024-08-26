from tkinter import *

tk = Tk()
tk.title("To Do")

listbox = Listbox(tk, height=15, width=50)
listbox.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(tk, orient=VERTICAL, command=listbox.yview)
scrollbar.pack(side=LEFT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)

def add_task():
    task = entry.get()
    if task!="":
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index[0])

entry = Entry(tk, width=50)
entry.pack(pady=10)

add_button = Button(tk, text="Add Task", width=48, command=add_task)
add_button.pack(pady=5)

delete_button = Button(tk, text="Delete Task", width=48, command=delete_task)
delete_button.pack(pady=5)

tk.mainloop()