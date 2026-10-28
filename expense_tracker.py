import expense

def expense_tracker():
    expense_list = []
    
    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Show summary")
        print("4. Exit")
        
        choice = int(input("Choose: "))

        if choice == 1:
            amount = float(input('Enter amount: '))
            try:
                if amount <= 0:
                    print('Amount must be greater than 0')
                else:
                    expense.add_expense(expense_list, amount)

            except ValueError:
                print('Invalid Amount')

        elif choice == 2:
            if len(expense_list) == 0:
                print('No expense yet')
            else:
                for i in range(len(expense_list)):
                    print(f'{i+1}. {expense_list[i]}')

        elif choice == "3":
            if len(expense_list) == 0:
                print("No expenses yet")
            else:
                expense.get_summary(expense_list)

        elif choice == "4":
            print("Goodbye!")
            break
        if __name__ == "__main__":
         expense_tracker()

expense_tracker()
