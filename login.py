from tkinter import *
from tkinter import messagebox
import smtplib
import random
import sqlite3
conn=sqlite3.connect('email_info1.db')
print("databse created")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS  information(email TEXT)""")
print("table created")
conn.commit()
conn.close()


username=StringVar
password=StringVar
root=Tk()
root.geometry("1000x500")
root.title("login page")
#otp=IntVar
txt1=Label(root,text="Enter your e-mailid",fg="blue",font=("vardhana",23))
txt1.grid(row=0,column=0)
e1=Entry(root,textvariable=username,width=80,borderwidth=10)
e1.grid(row=0,column=1)
txt2=Label(root,text="Password *",fg="blue",font=("vardhana",23))
txt2.grid(row=1,column=0)
e2=Entry(root,textvariable=password,show="*",width=80,borderwidth=10)
e2.grid(row=1,column=1)
e3=Entry(root,width=80,borderwidth=10)
e3.grid(row=5,column=1)
txt3=Label(root,text="Enter otp sent to your mail",fg="blue",font=("vardhana",23))
txt3.grid(row=4,column=1)
#global otp
def send():
    global otp
    sender_email="msuchita71@gmail.com"
    sender_password="Ritika123*"
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender_email,sender_password)
    print("login successful")
    address_info=e1.get()
    otp=random.randint(1000,9999)
    otp=str(otp)
    
    s.sendmail(sender_email,address_info,otp)
    print("otp sent")
def correctotp():
    #validation_msg=Label(root,text="enter otp verified successfully").grid()
    messagebox.showinfo("validation message","otp entered verified ")
def incorrectotp():
    #validation_msg=Label(root,text="incorrect otp,please recheck it").grid()
    messagebox.showinfo("validation message","otp entered is not corrected ")

def validate():

    if e3.get()==otp:
        correctotp()
    else:
        incorrectotp()
def login():
    conn=sqlite3.connect('email_info1.db')
    c=conn.cursor()
    c.execute("INSERT INTO information VALUES(:email)",
            {
                'email':e1.get()
            })
    c.execute("SELECT *,oid FROM information")
    records=c.fetchall()
    print(records)
    conn.commit()
    conn.close()
    
    
    root.destroy()
    import option
    
b1=Button(root,text="generateOTP",padx=20,pady=10,fg="black",bg="grey",command=send,font=("vardhana",18))
b1.grid(row=3,column=1)
b2=Button(root,text="login",padx=20,pady=10,bg="grey",command=login,font=("vardhana",18))
b3=Button(root,text="validate otp",padx=20,pady=10,bg="grey",command=validate,font=("vardhana",18))
b2.grid(row=7,column=1)
b3.grid(row=6,column=1)

root.mainloop()
#conn.commit()
#conn.close()

