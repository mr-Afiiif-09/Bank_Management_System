import json

accounts = []

try:
    with open("bank.json",'r') as f:
        accounts = json.load(f)
except FileNotFoundError:
    accounts = []

def save_acc():
    with open("bank.json",'w') as f:
        json.dump(accounts,f,indent=4)

while True:
    print("======Bank Management System ======")
    print("1. Create Account")
    print("2. View Account")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Check Balance")
    print("7. Delete Account")
    print("8. Exit")
    
    choice = input("Enter your choice:")

    if choice == '1':
        Acc_no = int(input("Enter Account Number:"))
        Name = input("Enter Account Holder Name:")
        Balance = float(input("Enter Balance:"))

        account = {
            "Acc_no": Acc_no,
            "Name": Name,
            "Balance": Balance
        }
        accounts.append(account)
        save_acc()
        print("Account Created Successfully !!!")

    elif choice == '2':
        if len(accounts) == 0:
            print("Account not found !!")
        else:
            for account in accounts:
                print(
                    f"Acc_no:{account['Acc_no']}",
                    f"Name:{account['Name']}",
                    f"Balance:{account['Balance']}"
                )

    elif choice == '3':
        Acc_no = int(input("Enter Account Number to Search:"))
        Found = False

        for account in accounts:
            if account['Acc_no'] == Acc_no:
                print(
                    f"Acc_no:{account['Acc_no']}",
                    f"Name:{account['Name']}",
                    f"Balance:{account['Balance']}"
                )
                Found = True
                break
            if not Found:
                print("Account not found !! ")
    
    elif choice == '4':
        Acc_no = int(input("Enter Account number to deposit Money:"))
        Found = False

        for account in accounts:
            if account['Acc_no'] == Acc_no:
                amount = float(input("Enter Amount to deposit:"))
                account['Balance'] += amount
                save_acc()
                print(f"Money deposited Successfully !!")
                print(f"New Balance is: {account['Balance']}")
                Found = True
                break
            if not Found:
                print("Account not found !!")

    elif choice == '5':
        Acc_no = int(input("Enter Account number to withdraw Money from:"))
        Found = False

        for account in accounts:
            if account['Acc_no'] == Acc_no:
                amount = float(input("Enter Amount to withdraw:"))
                if account['Balance'] >= amount:
                    account["Balance"] -= amount
                    save_acc()
                    print(f"Money withdrawn Successfully !!!")
                    print(f"New Balance is: {account['Balance']}")
                Found = True
                break
            if not Found:
                print("Account not found !!")

    elif choice == '6':
        Acc_no = int(input("Enter Account number to check Balance:"))
        Found = False

        for account in accounts:
            if account['Acc_no'] == Acc_no:
                print(f"Balance is :{account['Balance']}")
                Found = True
                break 
            if not Found:
                print(f"Account not found")

    elif choice == '7':
        Acc_no = int(input("Enter Account number to Delete the Account:"))
        Found = False

        for account in accounts:
            if account['Acc_no'] == Acc_no:
                accounts.remove(account)
                save_acc()
                print("Account Deleted Successfully !!")
            if not Found:
                print(f"Account not Found !!")

    elif choice == '8':
        print("Thank you for visting !!")
        print("Closing the Bank !!")
        break

    else:
        print("Invalid choice !!")



                
                


    

                

    

