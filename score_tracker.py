scores = []

while True:
#menu
    print("\n--- Score Tracker ---")
    print("1. Add score")
    print("2. View scores")
    print("3. Show statistics")
    print("4. Exit")

    choice = input('Choose option: ')
    #Conditions
    if choice == '1':
        add = float(input('Add score: '))
        scores.append(add)
        print('Score added')

    if choice == '2':
        if len(scores) == 0:
            print('No score added yet')
        else:
            for i, s in enumerate(scores, 1):
                print(f'{i}. {s}')

    elif choice == '3':
        if not scores:
            print("No scores yet")
        else:
            highest = max(scores)
            lowest = min(scores)
            total = sum(scores)
            average = total / len(scores)
            
            print(f"Highest: {highest}")
            print(f"Lowest: {lowest}")
            print(f"Total: {total}")
            print(f"Average: {average}")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print('Invalid input')