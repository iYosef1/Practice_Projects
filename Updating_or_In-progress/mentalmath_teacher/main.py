from knowledge_understanding_tester import Tester
from mental_math_mind import MentalMathMind
from math_ascii import mental_math_logo
import random

print(mental_math_logo)


def mental_math_challenge(questions_per_challenge=5):
    print(f'\nWelcome to a challenge of mental math!\n\nThere are 5 levels to choose from with level 1 being the'
          f' easiest and level 5 being the hardest. \nEach level has {questions_per_challenge} questions. You can '
          f'set a timer for your questions if you choose to.')
    continue_challenge = ''
    while continue_challenge not in ['Y', 'N']:
        continue_challenge = input('\nDo you wish to continue (Y/N)?: ').upper()
    if continue_challenge == 'N':
        print('Please come back to try the challenge later.')
        return
    else:
        timed = ''
        while timed not in ['Y', 'N']:
            timed = input('Do you wish to be timed during the challenge (Y/N)?: ').upper()
            time_limit = None
        if timed == 'N':
            pass
        else:
            while time_limit not in [5, 10, 15]:
                time_limit = int(input('Enter your time limit (5, 10, or 15 minutes) for each question: '))

    mind_of_teacher = MentalMathMind()  # object 1
    math_dictionary = (mind_of_teacher.math_element_vocab, mind_of_teacher.math_elements)
    duration_dict = {5: 300,
                     10: 600,
                     15: 900}
    if time_limit is not None:
        time_limit = duration_dict[time_limit]
    teacher = Tester(math_dictionary, time_limit)  # object 2

    whole_number = mind_of_teacher.whole_calc_num
    string_equation_calc = mind_of_teacher.solving_bedmas_string

    choose_level = ''
    while choose_level not in ['1', '2', '3', '4', '5']:
        choose_level = input('Pick level 1, 2, 3, 4, or 5 for your mental math challenge: ')
        if choose_level == '1':
            digit = 1
        elif choose_level == '2':
            digit = 2
        else:
            digit = 3
    score = 0
    score_count = []  # remove later if scoreboard function unnecessary
    for _ in range(questions_per_challenge):
        final_answer = 0.5
        while whole_number(final_answer) is False:
            two_nums = mind_of_teacher.think_two_divisible_nums(digit)
            fraction_num = mind_of_teacher.think_divisible_fraction_num(digit)
            fraction_num1 = mind_of_teacher.think_divisible_fraction_num(digit)
            root_num = mind_of_teacher.think_whole_root_num(digit)
            power_num = mind_of_teacher.think_whole_power_num(digit)

            question_numbers = [two_nums[0], two_nums[1], fraction_num[0], fraction_num1[0], root_num[0], power_num[0]]
            random.shuffle(question_numbers)

            operations = ['/', 'x', '+', '-']
            operation1 = random.choice(operations)
            operation2 = random.choice(operations)
            operation3 = random.choice(operations)

            lv_1 = f'{question_numbers[0]} {operation1} {question_numbers[1]}'  # 1 digits
            lv_2 = f'{question_numbers[0]} {operation1} {question_numbers[1]}'  # 2 digits
            lv_3 = f'{question_numbers[0]} {operation1} {question_numbers[1]}'  # 3 digits
            lv_4 = f'{question_numbers[0]} {operation1} {question_numbers[1]} {operation2} {question_numbers[2]}' #3 digits
            lv_5 = f'{question_numbers[0]} {operation1} {question_numbers[1]} {operation2} {question_numbers[2]} {operation3}' \
                   f' {question_numbers[3]}'  # 3 digits

            if choose_level == '1':
                question = lv_1
            elif choose_level == '2':
                question = lv_2
            elif choose_level == '3':
                question = lv_3
            elif choose_level == '4':
                question = lv_4
            elif choose_level == '5':
                question = lv_5
            final_answer = string_equation_calc(question)

        print('Question: ', question)
        print('Answer: ', final_answer)

        print()
        teacher.draw_question(question)
        print()
        results = teacher.check_numerical_answer(final_answer)

        teacher.scoreboard(results, score_count)

    score = sum(score_count)
    print(f'\nTotal Score: {score}/{questions_per_challenge}')

    if time_limit is not None:
        print(f'Total time taken to finish challenge: {round(results[1], 2)}')

    your_mark = (score/questions_per_challenge)*100
    if your_mark == 100:
        print('\nGreat job! You got a PERFECT SCORE in this challenge!')
    elif your_mark == 80:
        print('\nGood job, keep at it!')
    elif your_mark < 80:
        print(f'\nYou got {your_mark}% this time, but don\'t worry, just keep going.'
              f'\nYou\'ll get better!')

    try_again = ''
    while try_again not in ['Y', 'N']:
        try_again = input('\nDo you want to attempt the challenge again (Y/N)?: ').upper()
    if try_again == 'N':
        print('\nBye for now!')
        return
    else:
        print('\n')
        mental_math_challenge()
        return

# fix actual bug in calculations that have no errors: last num not included in calculations of lv_5 questions
# copy the equation as a string into the bedmas function to confirm differences of lv_5 questions


if __name__ == '__main__':
    mental_math_challenge()





