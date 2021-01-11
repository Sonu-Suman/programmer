print("Welcome in the Rock, Paper and Scissors game..")
print("1 for Rock")
print("2 for Paper")
print("3 for Scissors")

rules = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
Player_1 = input("Please enter your name: ")
Player_2 = input("and, your name: ")
print(f'Hey! {Player_1} and {Player_2}, let\'s play')


def Play():
    player_1 = input(f'Hey! {Player_1}, choose your number: ')
    player_2 = input(f'Hey! {Player_2}, choose your number: ')
    player1_Score = 0
    player2_Score = 0
    if Player_1 == Player_2:
        print("DRAW")
    elif ((player_1 == 1) == (player_2 == 3)) or ((player_1 == 2) == (player_2 == 1)) or ((player_1 == 3) ==(player_2 == 2)):
        player2_Score += 1
        print(f'{Player_2} Score:- {player2_Score}')
        print(f'{Player_2} wins!')
    else:
        player1_Score += 1
        print(f'{Player_1} Score:- {player1_Score}')
        print(f'{Player_1} wins!')


Play()