# <======This is the first type of A.T.M. code=======>

this = " l.S. Bank"
name = input("Enter your name.\nWho is using this card please enter your name:  ")

print(f'Welcome to {this} bank A.T.M')
restart = 'y'
chance = 3
balance = 100000000000

while chance >= 0:
    pin = int(input("Please Entered you 4 Digit input: "))
    if pin == 4598:
        print(f'Welcome {name}')
        print(f'your entered pin Correctly, Thank you for using {this} ATM')
        while restart not in ('n', 'NO', 'N', 'no'):
            print("Please Press 1 for your balance..")
            print("Please Press 2 for withdrawal your entered money...")
            print("Please Press 3 to pay in...")
            print("Please Press 4 to return card..")
            option = int(input("What would you like to choose?:  "))
            if option == 1:
                print(f'Your balance is ${balance}')
                restart = input('Would you like to go back?: ')
                if restart in ('n', 'NO', 'N', 'no'):
                    print("Thank you for using this ATM")
                    break
            elif option == 2:
                option2 = 'y'
                withdrawal = float(input("How Much Would you like to withdrawal? 100, 500, 1000, 5000, 10000,"
                                         " 50000, for other enter 1: "))
                if withdrawal in [100, 500, 1000, 5000, 10000, 50000]:
                    balance = balance - withdrawal
                    restart = input(f'\n Your Balance is now ${balance}\nWhat would you like to go back: ')
                    if restart in ('n', 'NO', 'N', 'no'):
                        print("Thank you!")
                        break
                elif withdrawal != [100, 500, 1000, 5000, 10000, 50000]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = 'y'
                elif withdrawal == 1:
                    withdrawal = float(input("Please Entre desired Amount: "))

            elif option == 3:
                pay_in = float(input("How much would you like to pay in? "))
                balance += pay_in
                print(f'\nYour Balance is now ${balance}')
                restart = input('Would you like to go back?: ')
                if restart in ('n', 'NO', 'N', 'no'):
                    print("Thank you")
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print("Thank you for using this service")
                break
            else:
                print("Please Enter a correct number...\n")
                restart = 'y'
    elif pin != 4598:
        print("This is incorrect pin....")
        chance = chance - 1
        if chance == 0:
            print("\nNo more tries")
    break


# <=======This is second type of A.T.M. code=======>

Bank_name = "L.S. Bank"

name = input("What's your name: ")
print(f'Hi {name}, Thank you for using {Bank_name}')

count = 0
Balance = 100000000

while count < 3:
    password = 4598
    while count < 3:
        passu = input("Enter your password: ")
        if int(passu) == password:
            print("Thank you")
            print("You Enter for: ")
            print("Checking for balance:  1")
            print("Withdraw money:  2")
            print("Deposit cash:  3")
            print("Collecting your card:  4(>3)")

            try:
                enter = int(input("Enter your choosing number: "))

                if enter == 1:
                    print(f'Your balance in bank account:\n  {Balance}$')

                elif enter == 2:
                    try:
                        money = int(input("Hi sir!\n Please, Enter your withdrawal money: "))
                        if money < Balance:
                            print(f'Thank you {name}, You currently collect {money}$')
                            Balance -= money
                            print(f'{name} currently balance: {Balance}$')
                        else:
                            print(f'Sorry sir, Your total amount is less than {money}$')
                            print("Thank you sir")
                    except:
                        print("Please! Enter valid money")

                elif enter == 3:
                    try:
                        deposit = int(input("Enter your deposit money: "))
                        Balance += deposit
                    except:
                        print("Please! Enter valid money")
                    print(f'Hello {name}, Your currently balance: {Balance}$')

                elif enter > 3:
                    print(f'Thanks for using {Bank_name}')
                    break
            except:
                print("Please, Enter your valid input")

        else:
            print("You typed answer is incorrect")
            print("Please, Enter a valid password")
        count += 1
    break