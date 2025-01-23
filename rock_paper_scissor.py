import random
# Determine the winner based on the game rules
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


choices = ["rock", "paper", "scissor"]

print("Welcome to Rock, Paper, Scissors Game!\nWinning Rules:\nRock vs Paper -> Paper wins\nRock vs Scissor -> Rock wins\nPaper vs Scissor -> Scissor wins\n")
while True:
    print("Choose one: rock, paper, scissor")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissor.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


