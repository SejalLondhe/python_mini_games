# legends_of_eldoria.py

def adventure_game():
    name = input("What is your name, adventurer? ")
    print(f"\nWelcome, {name}, to the enchanted world of Eldoria!")

    answer = input(
        "\nYou awaken at the edge of a mystical forest. The path splits in two — "
        "one glows with golden light, the other is shrouded in mist. "
        "Do you choose the glowing path or the misty path? (glow/mist): "
    ).lower()

    if answer == "glow":
        answer = input(
            "\nThe golden path leads you to a clearing guarded by a majestic unicorn. "
            "It looks at you curiously. Do you approach or stay back? (approach/back): "
        ).lower()

        if answer == "approach":
            print(
                "\nThe unicorn recognizes your pure heart and gifts you a crystal amulet. "
                "You are teleported to a hidden treasure chamber. You win!"
            )
        elif answer == "back":
            print(
                "\nYou step away cautiously, but a hidden snare catches your foot. "
                "You're trapped by forest spirits. Game over."
            )
        else:
            print("\nThat’s not a valid option. You are lost to the forest. Game over.")

    elif answer == "mist":
        answer = input(
            "\nAs you walk into the mist, eerie whispers surround you. "
            "A shadowy figure offers you a glowing potion. Do you drink it or refuse? (drink/refuse): "
        ).lower()

        if answer == "drink":
            print(
                "\nThe potion grants you the ability to speak to forest creatures. "
                "A wise owl guides you safely to a magical library. You gain ancient knowledge. You win!"
            )
        elif answer == "refuse":
            print(
                "\nThe figure vanishes and the mist thickens. You lose your way and are never seen again. Game over."
            )
        else:
            print("\nThat’s not a valid choice. You vanish into the mist. Game over.")
    else:
        print("\nThat’s not a valid path. You stand still until the forest consumes you. Game over.")

    print(f"\nThank you for playing, {name}! May your next quest be even more legendary.")

if __name__ == "__main__":
    adventure_game()
