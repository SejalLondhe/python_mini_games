# tech_quiz_game.py

print("Welcome to the Ultimate Tech Trivia Challenge!")

playing = input("Do you want to test your tech knowledge? (yes/no): ").lower()
if playing != "yes":
    print("No worries! Come back when you're ready to challenge your brain.")
    quit()

print("\nGreat! Let's begin the quiz.")
score = 0

# Question 1
answer = input("\n1. What does 'HTML' stand for? ").lower()
if answer == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect. It stands for 'HyperText Markup Language'.")

# Question 2
answer = input("\n2. What is the name of the brain of the computer? ").lower()
if answer == "cpu" or answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. It's called the CPU (Central Processing Unit).")

# Question 3
answer = input("\n3. What does 'SSD' stand for? ").lower()
if answer == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect. It stands for 'Solid State Drive'.")

# Question 4
answer = input("\n4. Which company developed the Windows Operating System? ").lower()
if answer == "microsoft":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Microsoft.")

# Question 5
answer = input("\n5. What does 'URL' stand for? ").lower()
if answer == "uniform resource locator":
    print("Correct!")
    score += 1
else:
    print("Incorrect. It stands for 'Uniform Resource Locator'.")

# Question 6
answer = input("\n6. What does 'RAM' stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect. It stands for 'Random Access Memory'.")

# Question 7
answer = input("\n7. What programming language is known for its snake logo? ").lower()
if answer == "python":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Python.")

# Question 8
answer = input("\n8. What does 'IP' stand for in IP address? ").lower()
if answer == "internet protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect. It stands for 'Internet Protocol'.")

# Question 9
answer = input("\n9. Which company created the Android operating system? ").lower()
if answer == "google":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Google.")

# Question 10
answer = input("\n10. What is the extension of a Python file? ").lower()
if answer == ".py":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is .py")

# Final Score
print(f"\nYou got {score} out of 10 questions correct.")
print(f"Your score: {round((score / 10) * 100)}%")

if score == 10:
    print("Excellent! You're a tech genius!")
elif score >= 7:
    print("Great job! You're on the right track.")
elif score >= 4:
    print("Not bad! A little more practice will help.")
else:
    print("Keep learning — you're just getting started!")

print("\nThanks for playing the Tech Trivia Challenge!")
