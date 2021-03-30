import random

name = input("What's your name: ")

print(f'Hey, {name}! This is guessing game ')
print("Do you want to play this game")

answer = input("Enter you answer(y/n)?: ")

if answer == "y":
    print("let's play!")
else:
    print("OK, We meet again")
    quit()

n = 0
computer = random.randint(1, 10)

while n <= 3:
    num = int(input("Enter your guessing number: "))

    if computer < num:
        print("you might choosing big number from computer")
    elif computer > num:
        print("you might choosing small number from computer")
    n += 1

    if computer == num:
        print("You guess the correct number")
        break
