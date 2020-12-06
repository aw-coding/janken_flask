class Player():

    def __init__(self, name):
        self.name = name
        self.choice = "blank_choice"





def player_make_choice(player, choice):
    player.choice = choice

def play_janken(first_player, second_player):
    if first_player.choice == 'rock' and second_player.choice == 'scissors':
        return f'{first_player.name} has defeated {second_player.name}!'

    elif first_player.choice == 'paper' and second_player.choice == 'rock':
        return f'{first_player.name} has defeated {second_player.name}!'

    elif first_player.choice == 'scissors' and second_player.choice == 'paper':
        return f'{first_player.name} has defeated {second_player.name}!'
    
    elif second_player.choice == 'rock' and first_player.choice == 'scissors':
        return f'{second_player.name} has defeated {first_player.name}!'

    elif second_player.choice == 'paper' and first_player.choice == 'rock':
        return f'{second_player.name} has defeated {first_player.name}!'

    elif second_player.choice == 'scissors' and first_player.choice == 'paper':
        return f'{second_player.name} has defeated {first_player.name}!'

    elif first_player.choice == second_player.choice:
        return f'It\'s a draw! Play again.'    
    
    else:
        return "Error. Please only enter /'rock/', \'paper\' or \'scissors\'."