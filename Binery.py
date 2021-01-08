this = "Surendra singh bank"
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
