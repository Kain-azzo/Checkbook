import os

keep_going = "yes"
current_balance = 0

if os.path.exists("current_balance.txt"):
    with open("current_balance.txt") as f:
        current_balance = f.read()
        current_balance = int(current_balance)
    print(f"Welcome to Stanny's Bank!\n\nAccessing current balance...\nYour current balance is ${current_balance}.")
else:
    print("\nNO CURRENT BALANCE....creating current balance sheet")
    with open('current_balance.txt', 'w') as f:
        f.write(str(current_balance))


def view_current_balance():
    print(f"Your current balance is ${current_balance}")
    return current_balance

def add_a_debit():
    debit = round(int(input(f"\nEnter the amount you want to debit\n")))
    globals()["current_balance"] -= debit
    print(f"Your current balance is ${int(current_balance)}")
    return  int(globals()["current_balance"])


def add_a_credit():
    credit = round(int(input(f"\nEnter the amount you want to credit\n")))
    globals()["current_balance"] += credit
    print(f"Your current balance is ${int(current_balance)}")
    return int(globals()["current_balance"])

def exit_program1():
   print("Thank you for being a loyal customer!\nHave a nice day!")
   with open('current_balance.txt', 'w') as f:
    f.write(str(current_balance))
   exit()

while keep_going == "yes":
    valid_entry = ["1","2","3","4"]
    user_choice=input(f"\nWelcome to Stannys Bank!\n\nWhat would you like to do today?\n \n1. View current balance\n2. Add a debit (withdrawal)\n3. add a credit (deposit)\n4. exit\n")
    if user_choice not in valid_entry:
        print("\nINVALID ENTRY!!! Choose an an option between 1 and 4.\n\n")
    elif user_choice == "1":
        view_current_balance()
    
    elif user_choice == "2":
        add_a_debit()
    elif user_choice == "3":
        add_a_credit()
    elif user_choice == "4":
        exit_program1()


keep_going == "no"
        
            
            
            
