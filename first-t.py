import random
import string as s


with open('word', 'r+') as f:
    f.readline()
    words = list(f)

word = random.choice(words).strip()

print(word)

if __name__ == "__main__":
    print("Welcome in Hangman game")
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    char = s.ascii_uppercase
    outguessed = [lit for lit in char if lit not in word]
    count = 1 * len(word)
    print("Your total number of wrong guesses is: ", count)
    letter = input("enter your letter: ")
    while count != 0:
        if letter.upper() in outguessed:
            letter = " "
            print("This is letter is not in guessed!")
            count -= 1
            print("Now your total chaches is: ", count)
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = "_"
        else:
            print(' '.join(guessed))
            if letter != " ":
                outguessed.append(letter.upper())
            letter = input("Enter your letter: ")

        if "_" not in guessed:
            print("You Won!")
            print("Your guess word is: ", ''.join(guessed))
            break

        if count == 0:
            print("You Lost the game!")
            break
