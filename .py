wallet_balance = 5000

while True:
    print('\n1.Check wallet balance')
    print('2.Buy airtime')
    print('3.Buy data')
    print('4.Exit')
    choice = input('Your option: ')
    if choice == '1':
        print(f'Your wallet balance is {wallet_balance}')
    elif choice == '2':
        Airtime_amount = float(input('Airtime amount: '))
        if Airtime_amount > 2000.0:
            print(f'{Airtime_amount} is more than daily limit')
        else:
            wallet_balance = wallet_balance - Airtime_amount
            print(f'Succesfully bought {Airtime_amount} Airtime, your balance is {wallet_balance} ')
    elif choice == '3':
        Data_amount =float(input('Data amount: '))
        if Data_amount > 2000.0:
            print(f'{Data_amount} Data amount exceed daily limit ')
        else:
            wallet_balance = Data_amount - wallet_balance
            print(f'Successfully bought {Data_amount} data amount, your balance is {wallet_balance}')
    elif choice == '4':
        print('Thank you for banking with us')
        break
