from tkinter import *
root=Tk()
root.title("currency converter")
root.geometry("400x400+250+250")
lab=Label(root,text="WELCOME TO CURRENCY CONVERTER",fg="blue")
lab.grid(row=0,column=1)
lab1=Label(root,text="ENTER VALUE IN DOLLAR")
lab1.grid(row=1,column=1)
num=IntVar()
e=Entry(root,textvariable=num,width=60,borderwidth=10)
e.grid(row=2,column=0,columnspan=3)
def con_rupees():
    num_1=num.get()
    final=num_1*74.34
    value=Label(root,text=("Rs")+str(final)).grid()
def con_euro():
    num_1=num.get()
    final=num_1*0.85
    value=Label(root,text=(str(final)+"euro")).grid()
def clear():
    e.delete(0,END)
b_1=Button(root,text="RUPEES",padx=20,pady=10,bg="pink",command=con_rupees).grid(row=4,column=0)
b_2=Button(root,text="EURO",padx=20,pady=10,bg="pink",command=con_euro).grid(row=4,column=1)
b_3=Button(root,text="CLEAR",padx=20,pady=10,bg="pink",command=clear).grid(row=4,column=2)
root.mainloop()
