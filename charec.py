import random

word_dictionary = ["KALI", "ABANDONING", "ABANDONMENT", "ABANDONMENTS", "ABANDONS", "ABANDONWARE", "ABANDONWARES",
                   "ABBREVIATORS", "ABBREVIATORY", "ABBREVIATURE", "ABBREVIATURES", "ABCEES", "ABCOULOMB", "ABCOULOMBS",
                   "ABDABS", "ABDICABLE", "ABDICANT", "ABDICATE", "ABDICATED", "ABDICATES", "ABDICATING", "ABDICATION",
                   "ABDICATIONS", "ADDICTIVE", "ABDUCTOR", "ABDICATORS"]

computer = random.choice(word_dictionary)

if __name__ == "__main__":
    print("Welcome to Hangman Game")
    guessed = "_" * len(computer)
    computer = list(computer)
    guessed = list(guessed)
    Outguessed = []
    letter = input("Guess letter: ")
    count = 0
    while count < 6:
        if letter.upper() in Outguessed:
            letter = " "
            print("Already guessed")
            count += 1
        elif letter.upper() in computer:
            index = computer.index(letter.upper())
            guessed[index] = letter.upper()
            computer[index] = "_"
        else:
            print(''.join(guessed))
            if letter != '':
                Outguessed.append(letter.upper())
            letter = input("Enter your guess: ")

        if '_' not in guessed:
            print("You Won!")
            break
