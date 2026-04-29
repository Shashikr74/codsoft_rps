# file: rps_cli.py

from rps_backend import get_computer_choice, determine_winner

def main():
    user_score = 0
    comp_score = 0

    print("=== ROCK PAPER SCISSORS (CLI) ===")

    while True:
        user = input("Enter rock/paper/scissors: ").lower()

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid input!")
            continue

        computer = get_computer_choice()
        print("Computer chose:", computer)

        winner = determine_winner(user, computer)

        if winner == "User":
            print("You Win!")
            user_score += 1
        elif winner == "Computer":
            print("You Lose!")
            comp_score += 1
        else:
            print("It's a Tie!")

        print(f"Score -> You: {user_score} | Computer: {comp_score}")

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
