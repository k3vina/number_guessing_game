import random


def user_input():
    print("Welcome to the number guessing game!")
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


def give_feedback(number, tries):

    

    while tries > 0:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess == number:
            print("Congratulations! You have won!")
            return 
        elif guess < number:
            print("Too low")
        else:
            print("Too high")

        tries -= 1
        print(f"You have {tries} tries remaining")

    if tries == 0:
        print(f"You have lost.The number is {number}.")
        return 0

def save_high_score(username, score):
    with open("high_scores.txt", "a") as f:
        f.write(f"{username},{score}\n")


def show_leaderboard():
    try:
        with open("high_scores.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No scores yet.")
        return

    scores = []
    for line in lines:
        name, score_str = line.strip().split(",")
        scores.append((name, int(score_str)))

    scores.sort(key=lambda entry: entry[1], reverse=True)

    print("--- LEADERBOARD ---")
    for name, score in scores[:5]:
        print(f"{name} - {score}")


number = random.randint(1, 100)
tries = user_input()
give_feedback(number, tries)

save_high_score(username, score)
show_leaderboard()