import random

def play_game():
    choices = ["scissors", "paper", "rock"]
    play_again = True

    while play_again:
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (scissors, paper, rock): ")

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "rock" and computer_choice == "scissors"):
            print("You win!")
        else:
            print("Computer wins!")

        play_again_input = input("Do you want to play again? (yes/no): ")
        play_again = play_again_input.lower() == "yes"

play_game()

