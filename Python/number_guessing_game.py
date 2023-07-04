#The Number Guessing Game
 
from random import randint
from building_blocks_module import is_int_float

logo = '''


  _____ _            _   _                 _                
 |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __  
   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ | '__| 
   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __| |    
   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    
   ____                    _                ____                          
  / ___|_   _  ___ ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___   _ 
 | |  _| | | |/ _ / __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \ (_)
 | |_| | |_| |  __\__ \__ | | | | | (_| | | |_| | (_| | | | | | |  __/  _ 
  \____|\__,_|\___|___|___|_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___| (_)
                                   |___/
'''






def guess_the_number():
    mental_num=randint(1,100)
    print(logo)

    print('Welcome to the Number Guessing Game!\
    \nGuess the (whole) number I\'m thinking of between 1 and 100.\n')

    game_difficulty=''
    while game_difficulty!='1' and game_difficulty!='2':
        game_difficulty=input('Enter the appropriate number to choose a difficulty: Easy(1) or Hard(2): ')
        if game_difficulty!='1' and game_difficulty!='2':
            print('Please enter 1 or 2\n')

    attempts_allowed=''
    if game_difficulty=='1':
        attempts_allowed=10
    else:
        attempts_allowed=5
    print(f'\nYou have {attempts_allowed} attempts to guess the number.\n\n')

    #print(mental_num)

    player_guess=''
    for _ in range(attempts_allowed):
        while is_int_float(player_guess)!=True:
            player_guess=input('Guess the number on my mind: ')
            if is_int_float(player_guess)!=True:
                print('Sorry, your guess has to be a number\n')
            elif is_int_float(player_guess)==True:
                player_guess=int(player_guess)
        if player_guess!=mental_num:
            attempts_allowed-=1
            if attempts_allowed==0:
                print(f'Sorry, you get no more chances! The number I was thinking of was {mental_num}.')
                break
            if player_guess > mental_num:
                hint='high'
            else:
                hint='low'
            print(f'Sorry! Too {hint}. Guess again, you have {attempts_allowed} attempts remaining.\n')
            player_guess=''
        else:
            print('Correct!!!')
            break
    play_again=''
    while play_again!='Y' and play_again!='N':
        play_again=input('\n\nI\'m thinking of another number between 1 and 100, would you like to guess again (Y/N): ').upper()
        if play_again!='Y' and play_again!='N':
            print('Huh? Yes or no?')
    if play_again=='Y':
        guess_the_number()
    else:
        print('Maybe later then... bye!')
        return

        
guess_the_number()            























