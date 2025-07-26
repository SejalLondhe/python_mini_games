# battle_arena_rps.py

import random

def display_intro():
    print("Welcome to the Battle Arena!")
    print("Rock  Paper  Scissors — Only one shall win!")
    print("Type Rock, Paper, or Scissors to fight.")
    print("Type Q anytime to quit the game.\n")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def main():
    user_wins = 0
    computer_wins = 0
    rounds_played = 0

    display_intro()

    while True:
        user_input = input("👉 Your move (Rock/Paper/Scissors or Q to quit): ").lower()

        if user_input == "q":
            break
        if user_input not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 The opponent chose {computer_choice.capitalize()}.")

        result = determine_winner(user_input, computer_choice)
        rounds_played += 1

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("✅ You win this round!")
            user_wins += 1
        else:
            print("❌ You lost this round!")
            computer_wins += 1

        print(f"📊 Score — You: {user_wins} | Computer: {computer_wins}\n")

    print("🏁 Game Over!")
    print(f"Total Rounds Played: {rounds_played}")
    print(f"🎉 You won {user_wins} times.")
    print(f"🤖 The computer won {computer_wins} times.")
    print("Thanks for playing in the Battle Arena!")

if __name__ == "__main__":
    main()
