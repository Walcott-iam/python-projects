def add_expense(expenses, amount):
    expenses.append(amount)
    print('expense added')

def get_summary(expenses):
    total = sum(expenses)
    average = total/len(expenses)
    print(f'Total:{total}')
    print(f'Average:{average}')