
import random

def rock_paper_scissors():
    player_score = 0
    cpu_score = 0
    rounds_played = 0

    choices = {
        1: "rock",
        2: "paper",
        3: "scissors"
    }

    print("Welcome to Rock, Paper, Scissors!")
    print("Enter r for rock, p for paper, s for scissors.")
    print("Enter q to quit the game.")

    while rounds_played < 3:
        player = input("Enter your choice: ").lower().strip()

        if player == "q":
            print("You quit the game.")
            break

        if player not in ["r", "p", "s"]:
            print("Invalid choice. Please enter r, p, s, or q.")
            continue

        # Generate the computer's random choice
        cpu_number = random.randint(1, 3)
        cpu = choices[cpu_number]

        # Convert the player's input into a full word
        if player == "r":
            player_choice = "rock"
        elif player == "p":
            player_choice = "paper"
        else:
            player_choice = "scissors"

        rounds_played += 1

        print("You chose:", player_choice)
        print("CPU chose:", cpu)

        # Determine the winner of the round
        if player_choice == cpu:
            print("This round is a tie!")
        elif (
            (player_choice == "rock" and cpu == "scissors")
            or (player_choice == "paper" and cpu == "rock")
            or (player_choice == "scissors" and cpu == "paper")
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("The CPU wins this round!")
            cpu_score += 1

        print("Player score:", player_score)
        print("CPU score:", cpu_score)
        print("Rounds played:", rounds_played)
        print()

    # Display the final scores
    print("Game over!")
    print("Final player score:", player_score)
    print("Final CPU score:", cpu_score)

    if player_score > cpu_score:
        print("Congratulations! You won the game!")
    elif cpu_score > player_score:
        print("The CPU won the game!")
    else:
        print("The game ended in a tie!")


rock_paper_scissors()
