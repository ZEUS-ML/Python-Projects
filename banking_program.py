def show_balance(balance):
    print(f"your balance is ${balance:.2f}")

def withdraw(balance):
    amt = float(input("Enter the amount you want to withdraw:"))
    if amt <= 0:
        print("invalid amount")
        return 0
    elif amt > balance:
        print("insufficient funds")
        return 0
    else:
        print("amount withdrawn successfully")
        return amt


def deposit(balance):
    amt = float(input("Enter the amount you want to deposit:"))
    if amt <= 0:
        print("enter a valid amount")
        return 0
    elif amt > 0:
        print("amount deposited successfully")
        return amt

def main():
    balance = 67
    is_running = True

    while is_running:
        print ("-----BANKING PROGRAM-----")
        print ("1.Check Balance")
        print ("2.Withdraw")
        print ("3.Deposit")
        print ("4.Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance -= withdraw(balance)
            print(f"your balance is ${balance:.2f}")
        elif choice == '3':
            balance += deposit(balance)
            print(f"your balance is ${balance:.2f}")
        elif choice == '4':
            is_running = False
        else:
            print("Please enter a valid choice")
    print("Thank you for using this program")
if __name__ == "__main__":
    main()
