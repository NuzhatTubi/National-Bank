from tkinter import *
from tkinter import messagebox

window=Tk()

window.title("National Bank")
window.geometry("500x400")

#Functions

customer = {}

def AddCustom():
    name = Name.get()
    acc = AccNum.get()
    Prime = float(PrimBal.get())

    if acc in customer:
        messagebox.showerror("Error","User already exist")
    else:
        customer[acc]={"Name":name,"Balance":Prime}
        messagebox.showinfo("Success",f" Customer {name} added successfully with Initial Balance {Prime} BDT ")


def Withdrawal():
    pass
def Deposition():
    pass
def Check():
    pass

CustomerName=Label(text="Customer Name",font=("Arial",15,"bold")).grid(row=0,column=0,padx=5,pady=5)
AccountNumber=Label(text="Account Number",font=("Arial",15,"bold")).grid(row=1,column=0,padx=5,pady=5)
PrimaryBalance=Label(text="Primary Balance",font=("Arial",15,"bold")).grid(row=2,column=0,padx=5,pady=5)

Name=Entry(font=("Arial",15,"bold"))
Name.grid(row=0,column=1,padx=5,pady=5)
AccNum=Entry(font=("Arial",15,"bold"))
AccNum.grid(row=1,column=1,padx=5,pady=5)
PrimBal=Entry(font=("Arial",15,"bold"))
PrimBal.grid(row=2,column=1,padx=5,pady=5)

AddCust=Button(text="Add Customer",font=("Arial",15,"bold"),fg="red",command=AddCustom).grid(row=3,column=0,padx=5,pady=5)
Amount=Label(text="Amount",font=("Arial",15,"bold")).grid(row=4,column=1,padx=5,pady=5)
AmountTxt=Entry(font=("Arial",15,"bold"))
AmountTxt.grid(row=5,column=1,padx=5,pady=5)

Withdraw=Button(text="Withdraw Balance",font=("Arial",15,"bold"),fg="purple",command=Withdrawal).grid(row=4,column=0,padx=5,pady=5)
Deposit=Button(text="Deposit Balance",font=("Arial",15,"bold"),fg="purple",command=Deposition).grid(row=5,column=0,padx=5,pady=5)
CheckBalance=Button(text="Check Balance",font=("Arial",15,"bold"),fg="purple",command=Check).grid(row=6,column=0,padx=5,pady=5)



window.mainloop()