# Higher Lower Game


# Use functions for the following reasons:
# systematic thinking
# to display your ability to break down big problems to smaller ones
# to show you can see the bigger picture from afar wrt the roles of smaller-details up close
# to create more custom functions that are easily reusable for later projects


# element symbol
# element name
# groups: alkali metal, alkaline earth metals, lanthanides, transition metals, post-transition metals,
# metalloids, other non-metals, halogens, noble gases


# Higher-lower game comparisons:
# 1) atomic number = number of protons = number of electrons
# 2) atomic weight = number of protons + number of neutrons (+ number of electrons: very low almost non-exist mass)
# 3) neutrons = atomic weight - number of protons (atomic number)
# 4) boiling point
# 5) melting point
# 6) electronegativity





#print(periodic_table)
#print(periodic_table[0])
#print(len(periodic_table))
    

from scraped_periodic_table_elements import sample_periodic_table_16_07_2021

from periodic_table_dictionary import periodic_table
from building_blocks_module import find_all_nums
import random
from random import randint
import math

# print(sample_periodic_table_16_07_2021)

version_logo = '''
             ____           _           _ _ 
            |  _ \ ___ _ __(_) ___   __| (_) ___                             
 _          | |_) / _ | '__| |/ _ \ / _` | |/ __|              _               
|_|_        |  __|  __| |  | | (_) | (_| | | (__     _ _ _ _ _|_|
|_|_|       |_|   \___|_|  |_|\___/ \__,_|_|\___|   |_|_|_|_|_|_|  
|_|_|                            _ _ _ _ _ _ _ _ _ _|_|_|_|_|_|_|  
|_|_|                           |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_| 
|_|_|_ _ _ _ _ _ _ _ _ _ _ _ _ _|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|  
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|  
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_| 
                         __   _____ _ __ 
                         \ \ / / _ | '__|              
                          \ V |  __| | _         
                           \_/ \___|_|(_)
'''

game_logo = '''
                    __  ___       __             
                   / / / (_)___ _/ /_  ___  _____
                  / /_/ / / __ `/ __ \/ _ \/ ___/
                 / __  / / /_/ / / / /  __/ /    
                /_/ ///_/\__, /_/ /_/\___/_/     
                   / /  /____/_      _____  _____
                  / /   / __ \ | /| / / _ \/ ___/
                 / /___/ /_/ / |/ |/ /  __/ /    
                /_____/\____/|__/|__/\___/_/    

'''

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""


'''   
'atomic number': '1'
'atomic weight': '1.008 g/mol'
'boiling point': '20.271 K'
'electronegativity': '2.20'
'element symbol': 'H'
'group': 'Other nonmetals'
'melting point': '13.99 K'
'name': 'Hydrogen'
'''


# melting point, boiling point, electronegativity

def bp_for_comparison(element_a_or_b):
    boiling_pt_for_comparison = float(find_all_nums(sample_periodic_table_16_07_2021[element_a_or_b]
                                                    ['boiling point'])[0])
    return boiling_pt_for_comparison


def mp_for_comparison(element_a_or_b):
    melting_pt_for_comparison = float(find_all_nums(sample_periodic_table_16_07_2021[element_a_or_b]
                                                    ['melting point'])[0])
    return melting_pt_for_comparison


def aw_for_comparison(element_a_or_b):
    atomic_weight_for_comparison = math.ceil(float(find_all_nums(sample_periodic_table_16_07_2021[element_a_or_b]
                                                                 ['atomic weight'])[0]))
    return atomic_weight_for_comparison


def neutrons(element_a_or_b):
    neutron_count = aw_for_comparison(element_a_or_b) - \
                    sample_periodic_table_16_07_2021[element_a_or_b]['atomic number']
    return neutron_count


question_answer = {
          'It\'s number of protons': 'atomic number',
          'It\'s number of electrons': 'atomic number',
          'It\'s number of neutrons': 'neutrons',
          'It\'s atomic weight in g/mol': 'atomic weight',
          'It\'s boiling point in Kelvin': 'boiling point',
          'It\'s melting point in Kelvin': 'melting point',
          'It\'s electronegativity': 'electronegativity'
          }

questions_list = list(question_answer.keys())


def higher_lower_game():
    print(version_logo)
    print(game_logo)
    print('Instructions: This is the periodic table version of the Higher Lower Game. You will be given\
\n2 random elements, A and B, and random 1 characteristic for each of these elements.\
\nTo score a point, you have to keep guessing which has a higher numerical value, A or B.')
    
    continue_game = ''
    while continue_game != 'Y' and continue_game != 'N':
        continue_game = input('\nWould you like to continue? (Y/N): ').upper()
        if continue_game != 'Y' and continue_game != 'N':
            print('Please enter Y or N.')
    if continue_game == 'Y':
        score = 0
        round_no = 1
        game_on = True
        
        a = randint(1, 127)  # element number of A
        while game_on:
            print('\n\n')
            print(game_logo)
            print('\nROUND: ', round_no)
            round_no += 1

            b = randint(1, 127)  # element number of B

            # element A:
            print('\nCompare element A: ' + sample_periodic_table_16_07_2021[a]['name'] +
                  ', it\'s symbol is ' + sample_periodic_table_16_07_2021[a]['element symbol'] +
                  ', and it belongs in the group of ' + sample_periodic_table_16_07_2021[a]['group']+'.')
            a_comparing_property = random.choice(questions_list)  # random property
            print(a_comparing_property + '...')

            if question_answer[a_comparing_property] == 'neutrons':
                answer_A = neutrons(a)
            elif question_answer[a_comparing_property] == 'boiling point':
                answer_A = bp_for_comparison(a)
            elif question_answer[a_comparing_property] == 'melting point':
                answer_A = mp_for_comparison(a)
            elif question_answer[a_comparing_property] == 'atomic_weight':
                answer_A = aw_for_comparison(a)
            else:
                answer_A = sample_periodic_table_16_07_2021[a][question_answer[a_comparing_property]]
            # print(answer_A)  # uncomment to show answer in console

            print(vs)

            # element B:
            print('Against element B: ' + sample_periodic_table_16_07_2021[b]['name'] +
                  ', it\'s symbol is ' + sample_periodic_table_16_07_2021[b]['element symbol'] +
                  ', and it belongs in the group of ' + sample_periodic_table_16_07_2021[b]['group'] + '.')
            b_comparing_property = random.choice(questions_list)  # random property
            print(b_comparing_property + '...')

            if question_answer[b_comparing_property] == 'neutrons':
                answer_B = neutrons(b)
            elif question_answer[b_comparing_property] == 'boiling point':
                answer_B = bp_for_comparison(b)
            elif question_answer[b_comparing_property] == 'melting point':
                answer_B = mp_for_comparison(b)
            elif question_answer[b_comparing_property] == 'atomic_weight':
                answer_B = aw_for_comparison(b)
            # print(answer_B)  # uncomment to show answer in console

            # Question:
            higher_lower = ''
            while higher_lower != 'A' and higher_lower != 'B' and higher_lower != 'EXIT':
                higher_lower = input(f'\nWhich is higher? A\'s {a_comparing_property[5:]} or '
                                     f'B\'s {b_comparing_property[5:]}: ').upper()
                if higher_lower != 'A' and higher_lower != 'B' and higher_lower != 'EXIT':
                    print('Please enter A or B. You may enter "EXIT" to quit the game.')

            # Answer:
            if answer_A >= answer_B:
                winning_element = 'A'
                element = sample_periodic_table_16_07_2021[a]['name']
                q = a_comparing_property[5:]
                show_answer = answer_A
            elif answer_A <= answer_B:
                winning_element = 'B'
                element = sample_periodic_table_16_07_2021[b]['name']
                q = b_comparing_property[5:]
                show_answer = answer_B

            # Won a goal!
            if higher_lower == winning_element:
                if winning_element == 'A':
                    pass
                elif winning_element == 'B':
                    a = b
                score += 1
                print('Correct! \nCurrent Score:', score)
                clear = input('\nPress enter for the next round: ')
                # clear screen function goes here

            elif higher_lower == 'EXIT':
                print('Goodbye')
                return
                
            # Lost the game!
            else:
                print(f"\n\nSorry! {winning_element} was higher, {element}'s {q} is {show_answer}. "
                      f"Your total score was {score}.\nBetter luck next time!")
                game_on = False
                play_again = ''
                while play_again != 'Y' and play_again != 'N':
                    play_again = input('\nWould you like to try again? (Y/N): ').upper()
                    if play_again != 'Y' and play_again != 'N':
                        print('Please enter Y or N.')
                if play_again == 'Y':
                    higher_lower_game()
                else:
                    print('\nGoodbye.')
                    return              
    else:
        print('\nMaybe next time, bye!')
        return


higher_lower_game()


