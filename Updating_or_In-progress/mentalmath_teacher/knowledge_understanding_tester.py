from adjacent_print_cls import AdjacentPrint
from threading import Timer
from pynput.keyboard import Key, Controller
import time


class Tester:
    def __init__(self, dictionary=('list of names of arts go here', 'list of ascii arts go here'),
                 time_limit=None, name='Helper'):
        self.dictionary = dictionary
        self.time_limit = time_limit
        self.name = name

    def draw_question(self, equation_string):
        black_board = AdjacentPrint(' ')
        # equation_elements = equation_string.split(' ')
        equation_elements = [x for x in list(equation_string) if x != ' ']
        if isinstance(self.dictionary[1], list) == isinstance(self.dictionary[0], list) is True:
            black_board.draw_ascii(self.dictionary[1], self.dictionary[0], equation_elements)
        else:
            print('Please make sure your dictionary attribute has a list of names and a list of ascii arts')
            return

    def check_numerical_answer(self, actual_answer):
        """
        Compares your answer with actual answer,Your 5 minutes are up!
         with or without a timer
        :return:
        """
        if self.time_limit is not None:
            def times_up():
                keyboard = Controller()
                keyboard.type(f'Your {self.time_limit} minutes are up!')
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

            input('Press ENTER to start your timer.')
            t = Timer(self.time_limit, times_up)  # Timer from threading module
            start_time_count = time.perf_counter()
            t.start()
            answer = input('Answer: ')
            if int(answer) == actual_answer:
                t.cancel()
                finish_time_count = time.perf_counter()
                score = 1
                print('Correct!\n')
            elif answer == f'Your {self.time_limit} minutes are up!':
                finish_time_count = time.perf_counter()
                print(f'The answer was {actual_answer}.')
                score = 0
            else:
                t.cancel()
                finish_time_count = time.perf_counter()
                print(f'The correct answer was {actual_answer}.')
                score = 0
                print('Sorry, better luck next time!')
            time_per_question = finish_time_count - start_time_count
            results = score, time_per_question
            return results
        else:
            answer = input('Answer: ')
            if int(answer) == actual_answer:
                score = 1
                print('Correct!\n')
            else:
                score = 0
                print('Sorry, better luck next time!')
            results = score
            return results

    def scoreboard(self, results=0, pt_count='list variable'):
        """
        This function requires an empty list in an earlier line of code to catch the score of each answer.
        The results parameter must contain the results of the function, check_numerical_answer(self, actual_answer).
        After the last question is answered, this function will have collected a list of the scores at the end
        of the test. You can use a sum function on the list to get the total score.
        :return: list of scores, 0s and 1s.
        """
        if isinstance(results, tuple):
            score = results[0]
        else:
            score = results
        pt_count.append(score)





# God = Teacher('Hi', '0', 3, '10min')

# print(God.name)

# start building game