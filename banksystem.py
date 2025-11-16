import os
import json
bank={}
filename="accinfo.txt"
r=os.popen(f"type {filename}").read()
#print(r)
#def update():
a=json.loads(r)
#print(type(a))
#print(a)
bank.update(a)
#print(bank)
def account():
    acc=input("Enter your account number=")
    if acc.startswith("0"):
        print("invalid account number.. Account number dosen't starts with zero")
    else:    
        if acc in bank:
            print("Account is already created")
        if acc not in bank:    
            nm=input("Enter your name=")
            mn=int(input("Enter your mobile number="))
            bal=int(input("Enter amount to deposit=")) 
            bank[acc]={"name":nm,"Contact_no":mn,"balance":bal}
            #os.system(f"echo {acc}:{bank[acc]} >> {filename} \n")
            os.system(f"break > {filename}")
            #b=json.dumps(bank)
            os.system(f"echo {json.dumps(bank)} >> {filename}\n")  
            print("Account created Successfully...")
def update():
    os.system(f"break > {filename}")
    os.system(f"echo {json.dumps(bank)}> {filename}")
def deposit():
    for keys in bank[ac_no]:
        if keys == "balance":
            cbal=bank[ac_no]['balance']
            t=cbal+depo
            bank[ac_no]['balance']=t
            print("Do you want to check balance..?\n 1.Yes \n 2.No")
            c=int(input("Enter your Choice="))
            if c == 1:
                print("Total balance=",t)
            if c >= 2:
                print("Thank you..")
            update()
            print("Amount deposited successfully..")
def withdraw():
    for keys in bank[ac_no]:
        if keys == "balance":
            cbal=bank[ac_no]['balance']
            if witd <= cbal and witd > 0:
                t=cbal-witd
                bank[ac_no]['balance']=t
                print("Do you want to check balance..?\n 1.Yes \n 2.No")
                c=int(input("Enter your choice="))
                if c == 1:
                    print("Total balance=",t)
                if c >= 2:
                    print("Thank you..")
                update()
                print("Amount withdraw successfully..")
            if witd > cbal:
                print("Insufficient balance")
            if witd <= 0:
                print("Invalid amount..")
               
def check_bal():
    cbal=bank[ac_no]['balance']
    print("Total balance=",cbal)
def acc_details():
    for keys,values in bank.items():
        print(f"{keys}:{values}")
def acc_det():
    #print(ac_no,":",bank[ac_no])
    print(bank[ac_no])
while True:
    print("Welcome.. you are user or admin ?\n 1.User \n 2.Admin \n 3.Exit")
    ch = int(input("Enter your choice="))
    if ch == 1:
        while True:
            print("What you want to do..? \n 1.Create new account \n 2.Deposit \n 3.Withdraw \n 4.Check balance \n 5.Exit")
            c = int(input("Enter your choice="))
            if c == 1:
                account()
                print("_________________________________________")
            if c == 2:
                ac_no=input("Enter your account number=")
                if ac_no in bank:
                    depo=int(input("Enter amount to deposit="))
                    if depo > 0:
                        deposit()
                    if depo <= 0:
                        print("Invalid amount...")
                if ac_no not in bank:
                    print("Account not found.. Please Enter valid account number")
                print("_________________________________________")
            if c == 3:
                ac_no=input("Enter your account number=")
                if ac_no in bank:
                    witd=int(input("Enter amount to withdraw="))
                    withdraw()
                if ac_no not in bank:
                    print("Account not found.. Please Enter valid account number")
                print("_________________________________________")
            if c == 4:
                ac_no=input("Enter your account number=")
                if ac_no in bank:
                    check_bal()
                if ac_no not in bank:
                    print("Account not found.. Please Enter valid account number")
                print("_________________________________________")
            if c == 5:
                print("Thank you..")
                print("_________________________________________")
                break
            if c >= 6:
                print("Invalid choice.. Please Enter valid choice")
                print("_________________________________________")
    if ch == 2:
        while True:
            print("What you want to do..? \n 1.Check list of all accounts \n 2.Check details of particular account \n 3.Exit")
            c = int(input("Enter your choice="))
            if c == 1:
                print("***List of account details***")
                acc_details()
                print("_________________________________________")
            if c == 2:
                ac_no=input("Enter your account number=")
                if ac_no in bank:
                    acc_det()
                if ac_no not in bank:
                    print("Account not found.. Please Enter valid Account number")
                print("_________________________________________")
            if c == 3:
                print("Thank you..")
                print("_________________________________________")
                break
            if c >=4:
                print("Invalid choice.. please Enter valid choice")
    if ch == 3:
        print("Thank you for visiting.. visit again..")
        break
    if ch >= 4:
        print("Invalid choice..Please enter valid choice")
        print("_________________________________________")