import random
print("Welcome in Rock Paper Scissors Game....")
print(" * r for rock... \n * p for paper... \n * s for scissors... \n * k for knightriders...")

def play():
    user = input("Choose one of these from this [r, k, p, s]: ")
    computer = random.choice(['r', 'p', 's', 'k'])
    print(f'Choose from computer: {computer}')

    if user == computer:
        return "Tie"

        # r>s, s > p, p>r
    if is_win(user, computer):
        return "O maa guu truu lob, \n  you win!"

    return "You lost!"

def is_win(player, opponent):
    #return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (player == 'k' and opponent == 's'):
        return True
        
   
print(play())