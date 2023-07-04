import random
from hangman_ascii import logo, stages
from mw_word_of_the_day import your_word_for_the_day

mystery_word = your_word_for_the_day()


# print('\nComputer\'s Chosen Word:', mystery_word[0])  # UNCOMMENT WHEN NEEDED


def hang_man():
    print(logo)
    game_start = ''
    while game_start != 'Y' and game_start != 'N':
        game_start = input('\nPlay hang-man (Y/N)?: ').upper()
        if game_start == 'Y':
            play_against = ''
            while play_against != '1' and play_against != '2':
                play_against = input(
                    '\nPlease enter 1 or 2. Would you like to play against a friend (1) or against the computer (2)?: ')
                if play_against == '1':
                    your_word = ''
                    while not your_word.isalpha():
                        your_word = input('\nEnter the one word you want your friend to guess: ').lower()
                        if not your_word.isalpha():
                            print('Sorry! Please enter a word with no spaces, numbers, or special characters')
                        else:
                            print('\n' * 30)
                            print(logo)
                    chosen_word = your_word
                elif play_against == '2':
                    chosen_word = mystery_word[0]
                display = []
                for letter in chosen_word:
                    display += '_'
                lives = 7
                while '_' in display:
                    good_guess = True
                    guess = ''
                    while len(guess) != 1 and guess != chosen_word:
                        hidden_chosen_word = ' '.join(display)
                        print('\n', hidden_chosen_word)
                        print(stages[lives])
                        if lives == 0:
                            print(f'Sorry! You lose.\nThe mystery word was "{chosen_word.upper()}".')
                            if chosen_word is mystery_word[0]:
                                print('\nBelow is the definition:\n')
                                for item in mystery_word:
                                    print(item)
                            return  # END
                        guess = input("\nGuess a letter: ").lower()
                        print('\n' * 15)
                        print(logo)
                        if guess == chosen_word:
                            display = list(guess)
                            print(f'You got it! The mystery word was: {chosen_word.upper()}')
                            if chosen_word is mystery_word[0]:
                                print('\nBelow is the definition:\n')
                                for item in mystery_word:
                                    print(item)
                            return  # END
                        if len(guess) != 1:
                            print('Sorry! Please enter one letter at a time.')
                    for position in range(len(chosen_word)):
                        if guess in display[position]:
                            print(f'Please guess a different letter, the letter "{guess}" is already taken.')
                            good_guess = False
                            break
                        elif chosen_word[position] == guess:
                            display[position] = guess
                    if good_guess is True:
                        if guess in chosen_word:
                            print('Correct!')
                            print(f'Remaining lives: {lives}')
                        else:
                            lives = lives - 1
                            print(
                                f'The letter "{guess}" isn\'t in the mystery word.\n\nYou lost a life, you have {lives} remaining.')
                            if lives != 0:
                                print('Try again!')
                print(f'\nFinally! \nYou got it! The mystery word was: {chosen_word.upper()}')
                if chosen_word is mystery_word[0]:
                    print('\nBelow is the definition:\n')
                    for item in mystery_word:
                        print(item)
                return
        else:
            print('Have a nice day!')
            return


if __name__ == '__main__':
    hang_man()



