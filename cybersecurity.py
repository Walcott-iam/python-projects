score = 0

while True:

    password = input("Enter a password: ")


    if len(password) >= 8:
        score = score + 1

    if any(c.isupper() for c in password):
        score = score + 1

    if any(c.islower() for c in password):
        score = score + 1

    if any(c.isdigit() for c in password):
        score = score + 1

    if any(c in "!@#$%^&*" for c in password):
        score = score + 1

    print("Score:", score, "/ 5")

    if score <= 2:
        print("WEAK password")
        print('Too short use 8+ character')
    elif score <= 4:
        print("MEDIUM password")
        print('Add upper case, lower case or special character')
    else:
        print("STRONG password")
        break