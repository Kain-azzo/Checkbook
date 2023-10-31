import os

keep_going = "yes"
current_balance = 0

if os.path.exists("current_balance.txt"): #Checks for balance file and writes it with current balance of zero, if it doesnt exist. Otherwise it imports and reads in its balance as current balance.
    with open("current_balance.txt") as f:
        current_balance = f.read()
        current_balance = int(current_balance)
    print(f"Welcome to Stanny's Bank!\n\nAccessing current balance...\nYour current balance is ${current_balance}.")
else:

    print("\nNO CURRENT BALANCE....creating current balance sheet")
    with open('current_balance.txt', 'w') as f:
        f.write(str(current_balance))


def view_current_balance(): # References current balance variable and prints out current balance.
    print(f"Your current balance is ${current_balance}")
    return current_balance

def add_a_debit(): # Takes an int and subtracts it from current balance, then prints out new current balance.
    valid_entry = range(0,10000000000000000)
    debit = input(f"\nEnter the amount you want to debit\n")
    if debit.isdigit():
        debit = int(debit)
        if debit in valid_entry: 
            debit = int(debit)
            globals()["current_balance"] -= debit
            print(f"Your current balance is ${int(current_balance)}")
            return  int(globals()["current_balance"])
        else:
            print(f"\nINVALID ENTRY FOR DEBIT! Please enter a valid number!")
    else:
        print(f"\nINVALID ENTRY FOR DEBIT! Please enter a valid number!")


def add_a_credit(): #Takes an int and adds it to current balance, then prints out new current balance.
    valid_entry = range(0,100000000000000000)
    credit = input(f"\nEnter the amount you want to credit\n")
    if credit.isdigit(): 
        credit = int(credit)
        if credit in valid_entry:
            globals()["current_balance"] += credit
            print(f"Your current balance is ${int(current_balance)}")
            return int(globals()["current_balance"])
        else:
            print(f"\nINVALID ENTRY FOR CREDIT! Please enter a valid number!")   
    else:
        print(f"\nINVALID ENTRY FOR CREDIT! Please enter a valid number!")

def exit_program1(): #Exits the program.
   print("Thank you for being a loyal customer!\nHave a nice day!")
   with open('current_balance.txt', 'w') as f:
    f.write(str(current_balance))
   exit()

while keep_going == "yes": #Runs loop for user data entry.
    valid_entry = ["1","2","3","4"]
    user_choice=input(f"\nWelcome to Stanny's Bank!\n\nWhat would you like to do today?\n \n1. View current balance\n2. Add a debit (withdrawal)\n3. add a credit (deposit)\n4. exit\n")
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
        
            
            
            
