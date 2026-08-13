import random

number = random.randint(1, 100)

def user_input():
    print("Welcom to the number guessing game!")
    print("Choose a diffculty.")

    difficulty_level = {
        1 : 'Easy',
        2 : 'Medium',
        3 : 'Hard'
    }

    tries_by_level = {
        1 : 10,
        2 : 7,
        3 : 5
    }

    while True:
        try:
            choice = int(input("Enter 1 (Easy), 2 (Medium), 3 (Hard): "))
            if choice in difficulty_level:
                print(f"You have chosen the {difficulty_level[choice]}. You have {tries_by_level[choice]} tries!")
                return tries_by_level[choice]
            else:
                print("Ivalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print(f"That's not a number. Please enter 1, 2, or 3")
            
user_input()
