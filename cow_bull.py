import random

# let's define a function
def compare_numbers(number, guess):
    cow = 0  # cows
    bull = 0  # bulls
    for i in range(len(number)):
        if number[i] == guess[i]:
            cow += 1
        else:
            bull += 1
    return cow, bull


if __name__ == "__main__":
    playing = True  # gotta play the game
    number = str(random.randrange(1000, 9999))
    guesses = 0

    # Game rule
    print("Let's play a game of cow-bull!")  # explanation
    print("I will generate a number, and you have to guess the number")
    print("For every number in the wrong place, you get a bull! nad every right place, you get a cow")
    print("The game ends when you get 4 bull")
    print("Type exit at any prompt to exit.")

    while playing:
        guess = input("Give me your best guess: ")
        if guess == "exit":
            break  # break the  loop if user input exit

        # Lat's call the function
        cowbullcount = compare_numbers(number, guess)
        guesses += 1

        print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls!")
        if cowbullcount[0] == 4:
            playing = False  # Break the loop
            print("You win the game after " + str(guess) + "! The number was " + str(number))
            break  # Redundant exit
        else:
            print("Your guess isn't quit right, try again")
