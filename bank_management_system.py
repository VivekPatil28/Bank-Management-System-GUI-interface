from tkinter import *
import time
from tkinter import messagebox


def makeTranscations(account):
    window = Tk()
    window.state('zoomed')
    window.title("Bank Management System")

    head = Label(window, text=str(account.greet()), fg="White",
                 bg="Green", padx=800, pady=25, font=("Arial", 30, "bold"))
    head.pack()

    label = Label(window, text="", font=("Arial", 20))
    label.pack()
    validate = Button(window, text="Deposit".center(30), padx=50, pady=15, font=("Arial", 25, "bold"), bg="Green", fg="White", command=account.deposit)
    validate.pack()

    label = Label(window, text="", font=("Arial", 20))
    label.pack()

    New_Account = Button(window, text="Withdraw".center(30), padx=45, pady=15, font=("Arial", 25, "bold"), bg="Green", fg="White", command=account.withdraw)
    New_Account.pack()

    label = Label(window, text="", font=("Arial", 20))
    label.pack()

    New_Account = Button(window, text="Check Balance".center(30), padx=25, pady=15, font=("Arial", 25, "bold"), bg="Green", fg="White", command=account.checkBalance)
    New_Account.pack()

    label = Label(window, text="", font=("Arial", 20))
    label.pack()

    New_Account = Button(window, text="Change Pin".center(30), padx=35, pady=15, font=("Arial", 25, "bold"), bg="Green", fg="White", command=account.changePin)
    New_Account.pack()

    label = Label(window, text="", font=("Arial", 20))
    label.pack()

    New_Account = Button(window, text="Transfer Money".center(30), padx=25, pady=15, font=("Arial", 25, "bold"), bg="Green", fg="White", command=account.transferMoney)
    New_Account.pack()

    window.mainloop()

class Account():
    __accounts = []
    @classmethod
    def Validate(cls):
        def getvalues():
            for account in cls.__accounts:
                if (account.__acno == acno.get() and account.__pin == pin.get()):
                    validate.destroy()
                    makeTranscations(account)
                    break
            else:
                messagebox.showwarning("Error", "Account Not Found", parent=validate)
                
        validate = Tk()
        validate.state('zoomed')
        validate.title("Bank Management System")
        head = Label(validate, text="Login", fg="White",
                     bg="Green", padx=800, pady=25, font=("Arial", 30, "bold"))
        head.pack()
        Label(validate, text="", font=("Arial", 90)).pack()
        Label(validate, text='Account Number',
              font=("Arial", 25), pady=20).pack()
        acno = Entry(validate, font=("Arial", 25))
        acno.pack()
        Label(validate, text="", font=("Arial", 20)).pack()
        Label(validate, text='PIN', font=("Arial", 25), pady=20).pack()
        pin = Entry(validate, show='*', font=("Arial", 25))
        pin.pack()
        Label(validate, text="", font=("Arial", 20)).pack()
        validateAccount = Button(validate, text="Validate", padx=45, font=(
            "Arial", 25, "bold"), bg="Green", fg="White", command=getvalues).pack()
        validate.mainloop()
        
        
        
    def __init__(self) -> None:
        def create():
            nonlocal name, acno, pin
            nameval = name.get()
            acnoval = acno.get()
            pinval = pin.get()
            isvalidname = False
            for i in nameval:
                if i.isdigit():
                    isvalidname = True
                    break
            if isvalidname:
                messagebox.showwarning(
                    "Error", "Invalid Name", parent=createNewAcc)
            elif not acnoval.isdigit():
                messagebox.showwarning(
                    "Error", "Invalid Account Number", parent=createNewAcc)
            elif not pinval.isdigit():
                messagebox.showwarning(
                    "Error", "Invalid PIN", parent=createNewAcc)
            elif len(pinval) < 4:
                messagebox.showwarning(
                    "Error", "PIN must be greater than 4 digits", parent=createNewAcc)
            else:
                self.__name = nameval.strip().title()
                self.__acno = acnoval
                self.__pin = pinval
                self.__balance = 0
                Account.__accounts.append(self)
                messagebox.showinfo(
                    "success", "Your Account was created successfully", parent=createNewAcc)
                createNewAcc.destroy()
        createNewAcc = Tk()
        createNewAcc.state('zoomed')
        createNewAcc.title("Bank Management System")
        Label(createNewAcc, text="", font=("Arial", 30)).pack()
        Label(createNewAcc, text='Enter Your Full Name',
              font=("Arial", 25), pady=20).pack()
        name = Entry(createNewAcc, font=("Arial", 25))
        name.pack()
        Label(createNewAcc, text="", font=("Arial", 30)).pack()
        Label(createNewAcc, text='Enter Account Number',
              font=("Arial", 25), pady=20).pack()
        acno = Entry(createNewAcc, font=("Arial", 25))
        acno.pack()
        Label(createNewAcc, text="", font=("Arial", 30)).pack()
        Label(createNewAcc, text='Enter a PIN', font=(
            "Arial", 25), pady=20).pack()
        pin = Entry(createNewAcc, show='*', font=("Arial", 25))
        pin.pack()
        Label(createNewAcc, text="", font=("Arial", 20)).pack()
        createAccount = Button(createNewAcc, text="Create", padx=45, font=(
            "Arial", 25, "bold"), bg="Green", fg="White", command=create).pack()
        createNewAcc.mainloop()
        
    # Humanize the Account Balance with Commas (,)
    def humanizeAmount(self):
        num = ''
        stri = str(self.__balance)[::-1]
        for i in range(len(stri)):
            if i >= 3:
                if i % 2 != 0:
                    num += ','
            num += stri[i]
        return num[::-1]
    #  Function to Greet the Account Owner When he login
    def greet(self) -> str:
        return "Welcome, " + self.__name + " choose your Transaction"
    
    def checkBalance(self):
        checkbalancewin = Tk()
        checkbalancewin.state('zoomed')
        checkbalancewin.title("Bank Management System")
        head = Label(checkbalancewin, text=str(self.greet()), fg="White",
                     bg="Green", padx=800, pady=25, font=("Arial", 30, "bold"))
        head.pack()
        Label(checkbalancewin, text="", font=("Arial", 80)).pack()
        Label(checkbalancewin, text="Available Balance ",
              font=("Arial", 20)).pack()
        Label(checkbalancewin, text="", font=("Arial", 30)).pack()
        head = Label(checkbalancewin, text=str(
            self.humanizeAmount()+"  Rs"), font=("Arial", 30, "bold"))
        head.pack()
        def checkbalanceclose():
            checkbalancewin.destroy()
        Label(checkbalancewin, text="", font=("Arial", 30)).pack()
        Button(checkbalancewin, text="Close", padx=45, font=(
            "Arial", 25, "bold"), bg="Red", fg="White", command=checkbalanceclose).pack()
        checkbalancewin.mainloop()
        
        
    def deposit(self):
        depositwindow = Tk()
        depositwindow.state('zoomed')
        depositwindow.title("Bank Management System")
        def depositAmount():
            if amount.get().isdigit():
                self.__balance += int(amount.get())
                messagebox.showinfo("success", "Amount Deposited successfully", parent=depositwindow)
                depositwindow.destroy()
            else:
                messagebox.showwarning("Error", "Enter a Valid Amount", parent=depositwindow)
                
        head = Label(depositwindow, text=str(self.greet()), fg="White",
                     bg="Green", padx=800, pady=25, font=("Arial", 30, "bold"))
        head.pack()

        Label(depositwindow, text="", font=("Arial", 100)).pack()
        
        Label(depositwindow, text='Enter Amount to Deposit',
              font=("Arial", 25), pady=20).pack()
        amount = Entry(depositwindow, font=("Arial", 25))
        amount.pack()
        Label(depositwindow, text="", font=("Arial", 30)).pack()
        createAccount = Button(depositwindow, text="Deposit", padx=45, font=(
            "Arial", 25, "bold"), bg="Green", fg="White", command=depositAmount).pack()
        depositwindow.mainloop()
        
    def withdraw(self):
        withdrawwindow = Tk()
        withdrawwindow.state('zoomed')
        withdrawwindow.title("Bank Management System")
        def withdrawAmount():    
            if amount.get().isdigit():
                if (int(amount.get()) <= self.__balance):
                    self.__balance -= int(amount.get())
                    messagebox.showinfo("success", "Amount Withdrawal Successful", parent=withdrawwindow)
                    withdrawwindow.destroy()
                else:
                    messagebox.showwarning("", "Insufficient Balance", parent=withdrawwindow)
            else:
                messagebox.showwarning(
                    "Error", "Enter a Valid Amount", parent=withdrawwindow)
                
        head = Label(withdrawwindow, text=str(self.greet()), fg="White",
                     bg="Green", padx=800, pady=25, font=("Arial", 30, "bold"))
        head.pack()
        
        Label(withdrawwindow, text="", font=("Arial", 100)).pack()
        Label(withdrawwindow, text='Enter Amount to Withdraw',
              font=("Arial", 25), pady=20).pack()
        amount = Entry(withdrawwindow, font=("Arial", 25))
        amount.pack()
        Label(withdrawwindow, text="", font=("Arial", 30)).pack()
        Button(withdrawwindow, text="Withdraw", padx=45, font=(
            "Arial", 25, "bold"), bg="Green", fg="White", command=withdrawAmount).pack()
        withdrawwindow.mainloop()
        
    def transferMoney(self):
        transferAmountWindow = Tk()
        transferAmountWindow.state('zoomed')
        transferAmountWindow.title("Bank Management System")
        
        def transfer():
            for account in Account.__accounts:
                if account.__acno == acno.get():
                    if self.__balance >= int(amount.get()):
                        self.__balance -= int(amount.get())
                        account.__balance += int(amount.get())
                        messagebox.showinfo("success", "Transaction Successful", parent=transferAmountWindow)
                        transferAmountWindow.destroy()
                        break
                    else:
                        messagebox.showwarning("Warning", "Insufficient Balance", parent=transferAmountWindow)
                else:
                    messagebox.showerror("Error", "Account Not Found", parent=transferAmountWindow)
                    
        head = Label(transferAmountWindow, text=str(self.greet()), fg="White",bg="Green", padx=800, pady=25, font=("Arial", 30, "bold"))
        head.pack()
        Label(transferAmountWindow, text="", font=("Arial", 30)).pack()
        Label(transferAmountWindow, text='Enter Receiver Account Number ',font=("Arial", 25), pady=20).pack()
        acno = Entry(transferAmountWindow, font=("Arial", 25))
        acno.pack()
        Label(transferAmountWindow, text="", font=("Arial", 30)).pack()
        
        Label(transferAmountWindow, text='Enter Amount For Tranfer', font=("Arial", 25), pady=20).pack()
        amount = Entry(transferAmountWindow, font=("Arial", 25))
        amount.pack()
        
        
        Label(transferAmountWindow, text="", font=("Arial", 30)).pack()
        
        Button(transferAmountWindow, text="Transfer Money", padx=45, font=("Arial", 25, "bold"), bg="Green", fg="White", command=transfer).pack()
        transferAmountWindow.mainloop()
        
        
    def changePin(self):
        changepinwindow = Tk()
        changepinwindow.state('zoomed')
        changepinwindow.title("Bank Management System")

        def changepin():
            for account in Account.__accounts:
                if account.__pin == oldpin.get():
                    if oldpin.get() == newpin.get():
                        messagebox.showwarning("Warning", "This PIN is already in use", parent=changepinwindow)
                    else:
                        if not newpin.get().isdigit():
                            messagebox.showwarning("Error", "Invalid PIN", parent=changepinwindow)
                        elif len(newpin.get()) < 4:
                            messagebox.showwarning("Error", "PIN must be greater than 4 digits", parent=changepinwindow)
                        else:
                            account.__pin=newpin.get()
                            messagebox.showinfo("Success", "PIN changed Successfully", parent=changepinwindow)
                            changepinwindow.destroy()
                            break 
                else:
                    messagebox.showerror(
                        "Error", "Invalid PIN", parent=changepinwindow)

        head = Label(changepinwindow, text=str(self.greet()), fg="White",
                     bg="Green", padx=800, pady=25, font=("Arial", 30, "bold"))
        head.pack()
        
        Label(changepinwindow, text="", font=("Arial", 30)).pack()
        Label(changepinwindow, text='Enter your Old PIN',
              font=("Arial", 25), pady=20).pack()
        oldpin = Entry(changepinwindow, font=("Arial", 25))
        oldpin.pack()
        Label(changepinwindow, text="", font=("Arial", 30)).pack()

        Label(changepinwindow, text='Enter Your New PIN',
              font=("Arial", 25), pady=20).pack()
        newpin = Entry(changepinwindow, font=("Arial", 25))
        newpin.pack()

        Label(changepinwindow, text="", font=("Arial", 30)).pack()

        Button(changepinwindow, text="Change PIN", padx=45, font=(
            "Arial", 25, "bold"), bg="Green", fg="White", command=changepin).pack()
        changepinwindow.mainloop()

    
    
    def __str__(self) -> str:
        return str(self.__acno)



# Driver Code


window = Tk()
head = Label(window, text=" WELCOME TO MGB ", fg="White",
             bg="Green", padx=800, pady=25, font=("Arial", 30, "bold"))
head.pack()
window.state('zoomed')
window.title("Bank Management System")
label = Label(window, text="", font=("Arial", 90))
label.pack()
validate = Button(window, text="Make Transactions".center(30), padx=35, pady=15, font=("Arial", 25, "bold"), bg="Green", fg="White", command=Account.Validate)
validate.pack()
label = Label(window, text="", font=("Arial", 30))
label.pack()
New_Account = Button(window, text="Create a New Account".center(30), padx=25, pady=15, font=("Arial", 25, "bold"), bg="Green", fg="White", command=Account)
New_Account.pack()
window.mainloop()
