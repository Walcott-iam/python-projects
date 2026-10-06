balance = 10000

while True:
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Please select an option: ")

    if choice == '1':
        print(f"Your current balance is: ${balance}")
    elif choice == '2':
        deposit_amount = float(input("Enter amount to deposit: "))
        balance += deposit_amount
        print(f"${deposit_amount} deposited. New balance is: ${balance}")
    elif choice == '3':
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient funds.")
        else:
            balance -= withdraw_amount
            print(f"${withdraw_amount} withdrawn. New balance is: ${balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option selected. Please try again.")