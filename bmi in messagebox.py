#abcdefghijklmnopqrstuvwxyz
#importing the things we need
from tkinter import*
from tkinter import messagebox
# making a def to ro calculate bmi
def calculate_bmi():
   # making the height and the weight
    height = float(entry1.get())
    weight = float(entry2.get())
  # calculating your bmi
    bmi = weight / (height / 100) ** 2
    print (bmi)
    if bmi < 18.5:
        messagebox.showinfo('bmi',f"Your BMI is:{bmi:.2f}\n under weight")  
    elif 18.5 <= bmi < 24.9:
       messagebox.showinfo('bmi',f"Your BMI is:{bmi:.2f}\n normal weight")
    else :
        messagebox.showinfo('bmi',f"Your BMI is:{bmi:.2f}\n over  weight")  
# making tkinter as tk
tk=Tk()
#making theb first label
label=Label(tk,text='height(m)')
label.pack()
# making the first entry
entry1=Entry(tk,bg='yellow',bd=3)
entry1.pack()
# making a second label
label=Label(tk,text='weight(m)')
label.pack()
#making the second entry
entry2=Entry(tk,bg='gold',bd=3)
entry2.pack()
# making a button for you to press
button=Button(tk,text='sandy will tell your bmi with a sand storm',command=calculate_bmi)
button.pack()
#and finaly making the third label 
label_masiha=Label(tk,text=' ')
label_masiha.pack()
# and voala
# sandy wrote this
# writer masiha ashegh
#creator sandy
#director sandy  
#words from masiha
#i realy liked this code its greate that i got to
#create this its very use full ijust love it





































































































































































































































































































































































































