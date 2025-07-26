# dice_roll_game.py

import random

def roll_dice():
    """Simulates rolling a 6-sided dice"""
    return random.randint(1, 6)

def get_player_count():
    """Prompt for valid number of players between 2 and 4"""
    while True:
        players = input(" Enter number of players (2–4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("⚠️ Please enter a number between 2 and 4.")
        else:
            print("❌ Invalid input. Please enter a number.")

def main():
    print(" Welcome to the Dice Roll Game!")
    print("First player to reach 50 points wins!\n")

    num_players = get_player_count()
    player_scores = [0 for _ in range(num_players)]
    target_score = 50

    while max(player_scores) < target_score:
        for i in range(num_players):
            print(f"\n🎮 Player {i + 1}'s turn | Total Score: {player_scores[i]}")
            current_score = 0

            while True:
                choice = input("Roll the dice? (y/n): ").lower()
                if choice != 'y':
                    break

                value = roll_dice()
                if value == 1:
                    print(" You rolled a 1! Turn over, no points earned.")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f" You rolled a {value} | Round Score: {current_score}")

            player_scores[i] += current_score
            print(f" Player {i + 1}'s Total Score: {player_scores[i]}")

            if player_scores[i] >= target_score:
                break

    winner = player_scores.index(max(player_scores)) + 1
    print(f"\n Player {winner} wins the game with {max(player_scores)} points! ")

if __name__ == "__main__":
    main()
