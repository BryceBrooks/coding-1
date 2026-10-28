
from random import randint

def dice_game():
    score = 0
    choice = input("Enter 'r' to roll or 'q' to quit: ").lower()

    while choice == 'r':
        roll = randint(1, 7)
        print("You rolled:", roll)

        if roll == 7:
            score += 10
            print("You win! You earned 10 points.")
        else:
            score -= 5
            print("Sorry, you lost 5 points.")

        print("Your current score is:", score)
        choice = input("Enter 'r' to roll again or 'q' to quit: ").lower()

    print("Game over! Your final score is:", score)

dice_game()
