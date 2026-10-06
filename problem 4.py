password = input('Enter password: ')
while not password == 'python123':
    print('Incorrect password. Please try again.')
    password = input('Enter password: ')
print('Password accepted.')