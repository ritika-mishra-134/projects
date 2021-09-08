from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("1525x785")
lab=Label(root,text="Choose your quiz level",font=("blades",30),fg="blue").pack(padx=10,pady=20)
MODES=[
    ("easy","easy"),
    ("medium","medium"),
    ("hard","hard")
]
var=StringVar()
var.set("None")
for text,mode in MODES:
    buttons=Radiobutton(root,text=text,variable=var,value=mode,font=("vardhana",23)).pack(anchor="w",padx=600)
def proceed(value):
    #mylabel=Label(root,text=value).pack()
    messagebox.showinfo("info box","u choose" + value )
    root.destroy()
    import converter
b=Button(root,text="Proceed",command=lambda:proceed(var.get()),font=("vardhana",23),fg="white",bg="blue").pack(padx=700,pady=50)


root.mainloop()