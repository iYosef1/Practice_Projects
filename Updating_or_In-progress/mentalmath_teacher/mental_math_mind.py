import random
import math
from math_ascii import math_ascii, math_ascii_names

rt_superscript = {'2': '²',
                  '3': '³',
                  '4': '⁴'}
pw_superscript = {'1': '',
                  '2': '²',
                  '3': '³',
                  '4': '⁴'}


def whole_calc_num(number):
    """
    This function returns False if the argument is not a whole number.
    """
    no_string = str(number)
    index_after_decimal = int(no_string.index('.') + 1)
    for digit in no_string[index_after_decimal:]:
        if digit == '0':
            pass
        else:
            return False

# change str_num_value function so (num/num) also works just like num/num for all num types of this function
def str_num_value(num_string):
    """
    This function type casts the string of a number with a
    fraction bar, factorial, radical sign and/or exponent (²|³|⁴)
    into its numerical float value
    """
    pwsuperscript_ = {'²': '2',
                      '³': '3',
                      '⁴': '4'}
    if isinstance(num_string, str):
        if num_string[0] == '(' and num_string[-1] == ')':
            num_string = num_string[1: -1]
        else:
            pass
    try:
        num = float(num_string)
        return num
    except ValueError:
        if '/' in num_string:
            num = num_string.split('/')
            num = float(num[0]) / float(num[1])
            return num
        if '!' in num_string:
            num = num_string.split('!')
            num = math.factorial(int(num[0]))
            return num
        if '√' in num_string:
            num = num_string.split('√')
            if num[0] in pwsuperscript_:
                denominator = int(pwsuperscript_[num[0]])
            else:
                denominator = 2
            if num[1][-1] in pwsuperscript_:
                numerator = int(pwsuperscript_[num[1][-1]])
                num = float(num[1].split(num[1][-1])[0])
            else:
                numerator = 1
                num = float(num[1])
            power_of = numerator / denominator
            num = pow(num, power_of)
            return num
        for exponent in list(pwsuperscript_.keys()):
            if exponent in num_string:
                num_list = num_string.split(exponent)
                num = float(num_list[0])
                exponent = int(pwsuperscript_[exponent])
                num = pow(num, exponent)
                return num  #


class MentalMathMind:

    def __init__(self):
        """
        The first 2 attributes are a list of ascii arts of math elements
        and a list of the keys representing each ascii art, respectively.
        The last 6 attributes of this class by default have no useful value.
        A class method must be applied before each attribute is called
        for the attribute to have a purposeful value.
        """
        self.math_elements = math_ascii
        self.math_element_vocab = math_ascii_names
        self.two_divisible_numbers = 0
        self.divisible_fraction = 0
        self.whole_root_number = 0
        self.whole_power_number = 0
        self.solve_number_value = 'Thinking...'
        self.solve_math_string_equation = 'Still thinking...'

    def think_two_divisible_nums(self, digit=1):
        """
        The function returns 2 random divisible numbers and divisibility is in the order
        :param digit: by default the return tuples will be 1 digit numbers; pass in 2 to return 1-2
        digits numbers or pass in 3 to return 1-3 digit numbers
        :return: tuple of 2 divisible numbers
        """
        num1 = 5
        num2 = 3
        if digit == 1:
            upper_limit = 9
            lower_limit = -9
        elif digit == 2:
            upper_limit = 99
            lower_limit = -99
        elif digit == 3:
            upper_limit = 999
            lower_limit = -999
        while (num1 % num2) != 0:
            # print('Try Again')
            above_zero = random.randint(1, upper_limit)
            below_zero = random.randint(lower_limit, -1)
            random_num1 = [below_zero, above_zero]
            above_zero = random.randint(1, upper_limit)
            below_zero = random.randint(lower_limit, -1)
            random_num2 = [below_zero, above_zero]
            num1 = random.choice(random_num1)
            num2 = random.choice(random_num2)
        # print(num1, num2)
        self.two_divisible_numbers = str(num1), str(num2)
        return self.two_divisible_numbers

    def think_divisible_fraction_num(self, digit=1):
        """
        The function returns a fraction of mod 0 as a string and its numerical value
        :param digit: by default the numerator & denominator will be 1-digit but this can
        be adjusted by passing in 2 or 3 for 2 or 3-digit numbers
        :return: a tuple containing a string equivalent and its float value
        """
        numerator = 5
        denominator = 3
        if digit == 1:
            pos_boundary = 9
            neg_boundary = -9
        elif digit == 2:
            pos_boundary = 99
            neg_boundary = -99
        elif digit == 3:
            pos_boundary = 999
            neg_boundary = -999
        while (numerator % denominator) != 0:
            above_zero = random.randint(1, pos_boundary)
            below_zero = random.randint(neg_boundary, -1)
            random_num1 = [below_zero, above_zero]
            above_zero = random.randint(1, pos_boundary)
            below_zero = random.randint(neg_boundary, -1)
            random_num2 = [below_zero, above_zero]
            numerator = random.choice(random_num1)
            denominator = random.choice(random_num2)
        fraction = f'({numerator}/{denominator})'
        fraction_answer = int(numerator / denominator)
        # print('Question:',fraction)
        # print('Answer:',fraction_answer)
        self.divisible_fraction = fraction, fraction_answer
        return self.divisible_fraction

    def think_whole_root_num(self, digit=1):
        """
        This function finds a random number as the radicand with
        an index and/or exponent from 1 to 4
        :param digit: by default the base number will be 1-digit but this can
        be adjusted by passing in 2 or 3 for 2 or 3-digit numbers as the base
        :return: a tuple containing a string equivalent and its float value
        """
        base_number = 0.1
        root = 0.1
        root_options = [1 / 2, 1 / 3, 2 / 3, 1 / 4, 3 / 4]
        root_answer = pow(base_number, root)
        while whole_calc_num(root_answer) is False:
            if digit == 1:
                base_number = random.randint(1, 9)
            elif digit == 2:
                base_number = random.randint(1, 99)
            elif digit == 3:
                base_number = random.randint(1, 999)
            root = random.choice(root_options)
            root_answer = pow(base_number, root)
            # print(root_answer)
        root_fraction = root.as_integer_ratio()
        root_fraction = f'{root_fraction[0]}/{root_fraction[1]}'
        if root_fraction == '6004799503160661/18014398509481984':
            root_fraction = '1/3'
        if root_fraction == '6004799503160661/9007199254740992':
            root_fraction = '2/3'
        # print('POSSIBLE STRANGE ERROR:',root_fraction[2], root_fraction)
        rt = rt_superscript[root_fraction[2]]
        if root == 1 / 2:
            rt = ''
        pw = pw_superscript[root_fraction[0]]
        if root == 1 / 2 or root == 1 / 3 or root == 1 / 4:
            pw = ''
        # print('scripts:', rt, pw)
        rooted_number = f'{rt}√{base_number}{pw}'
        root_answer = pow(base_number, root)
        if whole_calc_num(root_answer) is not False:
            # print('Question:',rooted_number)
            # print('Answer:',root_answer)
            self.whole_root_number = rooted_number, root_answer
            return self.whole_root_number

    def think_whole_power_num(self, digit=1):
        """
        This function finds random number to the power of 2, 3, or 4
        :param digit: by default the base number will be 1-digit but this can
        be adjusted by passing in 2 or 3 for 2 or 3-digit numbers as the base
        :return: a tuple containing a string equivalent and its float value
        """
        if digit == 1:
            base_number = random.randint(1, 9)
        elif digit == 2:
            base_number = random.randint(1, 99)
        elif digit == 3:
            base_number = random.randint(1, 999)
        pwr_options = [2, 3, 4]
        power = random.choice(pwr_options)
        power_number = f'{base_number}{pw_superscript[str(power)]}'
        power_answer = pow(base_number, power)
        # print('Question:', power_number)
        # print('Answer:',power_answer)
        self.whole_power_number = power_number, power_answer
        return self.whole_power_number

    def solving_str_num(self, num_string):
        """
        This function type casts the string of a number with a
        fraction bar, factorial, radical sign and/or exponent (²|³|⁴)
        into its numerical float value
        :param num_string: the string of a single number
        :return: the float value of the number
        """
        superscript_pw = {'²': '2',
                          '³': '3',
                          '⁴': '4'}
        if isinstance(num_string, str):
            if num_string[0] == '(' and num_string[-1] == ')':
                num_string = num_string[1: -1]
            else:
                pass
        try:
            self.solve_number_value = float(num_string)
            return self.solve_number_value
        except ValueError:
            if '/' in num_string:
                num = num_string.split('/')
                self.solve_number_value = float(num[0]) / float(num[1])
                return self.solve_number_value
            if '!' in num_string:
                num = num_string.split('!')
                self.solve_number_value = math.factorial(int(num[0]))
                return self.solve_number_value
            if '√' in num_string:
                num = num_string.split('√')
                if num[0] in superscript_pw:
                    denominator = int(superscript_pw[num[0]])
                else:
                    denominator = 2
                if num[1][-1] in superscript_pw:
                    numerator = int(superscript_pw[num[1][-1]])
                    num = float(num[1].split(num[1][-1])[0])
                else:
                    numerator = 1
                    num = float(num[1])
                power_of = numerator / denominator
                self.solve_number_value = pow(num, power_of)
                return self.solve_number_value
            for exponent in list(superscript_pw.keys()):
                if exponent in num_string:
                    num_list = num_string.split(exponent)
                    num = float(num_list[0])
                    exponent = int(superscript_pw[exponent])
                    self.solve_number_value = pow(num, exponent)
                    return self.solve_number_value

    def solving_bedmas_string(self, string_equation):
        """
        This function takes a string-equation that starts and ends with a number,
        along with operations (/, x, +, -) in between the numbers
        :param string_equation: argument will be the string of an equation
        :return: float value of solved equation
        """
        if not isinstance(string_equation, str):
            print('Please pass in a string equation as an argument')
            return
        equation_elements = string_equation.split(' ')
        for operation in ['/', 'x', '+', '-']:
            for element in equation_elements:
                if element == operation:
                    operator_index = equation_elements.index(element)
                    str_before_operator = equation_elements[operator_index - 1]
                    str_after_operator = equation_elements[operator_index + 1]
                    before_operator = str_num_value(str_before_operator)
                    after_operator = str_num_value(str_after_operator)
                    if element == '/':
                        answer = before_operator / after_operator
                    elif element == 'x':
                        answer = before_operator * after_operator
                    elif element == '+':
                        answer = before_operator + after_operator
                    elif element == '-':
                        answer = before_operator - after_operator
                    equation_elements[equation_elements.index(element)] = answer
                    equation_elements.remove(str_before_operator)
                    equation_elements.remove(str_after_operator)
                else:
                    pass
        self.solve_math_string_equation = equation_elements[0]
        return self.solve_math_string_equation

    def whole_calc_num(self, number):
        """
        This function returns False if the argument is not a whole number.
        :return: False or None
        """
        no_string = str(number)
        index_after_decimal = int(no_string.index('.') + 1)
        for digit in no_string[index_after_decimal:]:
            if digit == '0':
                pass
            else:
                return False


'''
Amanda = MentalMathMind()
Amanda.think_two_divisible_nums(3)
print(Amanda.two_divisible_numbers)
Amanda.solving_bedmas_string('5 - 7')
print(Amanda.solve_math_string_equation)
'''

''' 
print(str_num_value('(3/5)'))
Amanda = MentalMathMind()
print('AMANDA:', Amanda.solving_str_num('(3/5)'))
'''