import random

guess_num = random.randint(1, 9)
num = 0
count = 0

while guess_num != int(num) and num != 'exit':
    num = input("Enter your number: ")
    if num == "exit":
        break

    if int(num) > guess_num:
        print("Your number is too high.")
    elif int(num) < guess_num:
        print("Your number is too low...")
    else:
        print("You got it.")
        print("Your guess number is right")
        print("Your total previous number of guessing: ", count)
    count += 1
