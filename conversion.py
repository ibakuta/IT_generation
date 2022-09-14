from tkinter import *
import tkinter.messagebox as mb

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")


def conversion():
   t1=a.get()
   t2=b.get()
   if t1.isdigit() == True and t2.isdigit()== True and int(t1) >0 and int(t2)>0:
      value = (1/int(t1))*int(t2)
      label.config(text=round(value, 7))
   else:
      msg = "It's not a positive number!"
      mb.showerror("Ошибка", msg)

# Create an Entry widget
Label(win, text="What is Bitcoin price today?", font=('Calibri 10')).pack()
a=Entry(win, width=35)
a.pack()
Label(win, text="How much $ do you have?", font=('Calibri 10')).pack()
b=Entry(win, width=35)
b.pack()

label=Label(win, text="You can buy (BTC) : ", font=('Calibri 15'))
label.pack(pady=20)

Button(win, text="Conversion", command=conversion).pack()

win.mainloop()