import random

print("Welcome to the Number Guessing Game!")
print("I will think of a number between 0 and the number you give.\n")

# Input: Top range for random number
top_of_range = input("Type a maximum number (greater than 0): ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    print("Invalid input. Please enter a number next time.")
    quit()

# Generate random number
random_number = random.randint(0, top_of_range)

# Initialize guess counter
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Invalid input. Please enter a number.")
        continue

    if user_guess == random_number:
        print("Correct! You guessed the number.")
        break
    elif user_guess > random_number:
        print("Too high.")
    else:
        print("Too low.")

print(f"You got it in {guesses} guesses.")
