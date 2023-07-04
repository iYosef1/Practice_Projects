#CALCULATOR 
 
logo = """
 ______________________________
|  __________________________  |          
| | Pythonista   0.          | |  .--------------------. .------------------. .------------------. .------------------. 
| |__________________________| |  | .----------------. | | .--------------. | | .--------------. | | .--------------. |
|  ___ ___ ___   ___ ___       |  | |     ______     | | | |      __      | | | |   _____      | | | |     ______   | |
| | 7 | 8 | 9 | | + |CLR|      |  | |   .' ___  |    | | | |     /  \     | | | |  |_   _|     | | | |   .' ___  |  | |
| |___|___|___| |___|_ _|      |  | |  / .'   \_|    | | | |    / /\ \    | | | |    | |       | | | |  / .'   \_|  | |
| | 4 | 5 | 6 | | - |(-)|      |  | |  | |           | | | |   / ____ \   | | | |    | |   _   | | | |  | |         | |
| |___|___|___| |___|___|      |  | |  \ `.___.'\    | | | | _/ /    \ \_ | | | |   _| |__/ |  | | | |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | ^ |      |  | |   `._____.'    | | | ||____|  |____|| | | |  |________|  | | | |   `._____.'  | |
| |___|___|___| |___|___|      |  | |                | | | |              | | | |              | | | |              | |
| | . | 0 | = | | / | √ |      |  | '----------------' | | '--------------' | | '--------------' | | '--------------' |
| |___|___|___| |___|___|      |  '--------------------' '------------------' '------------------' '------------------' 
|______________________________|
"""

#import building_blocks_module #to import everything from building_blocks_module

from building_blocks_module import is_int_float


print(logo)

operations_available=[' +: Addition',' -: Subtraction',' *: Multiplication',' /: Division','**: Power of',' √: Root of']
for operation in operations_available:
    print(operation)


def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def power_of(n1,n2):
    return n1 ** n2

def root(n1,n2):
    return n2 ** (1/n1) 

def clear():
    pass


def calc():
    f_number=''
    while is_int_float(f_number)==False:
        f_number=input('\nEnter your first number: ')
    
    operations={'+': add,
                '-': subtract,
                '*': multiply,
                '/': divide,
                '^': power_of,
                '√': root}
    
    continue_cancel=True
    
    while continue_cancel==True:
        operation_choice=''
        print('\nNote: Please copy & paste the root operation (alt+251) to enter it below as your input for calculation.')
        
        while operation_choice not in operations.keys(): 
            operation_choice=input('Please enter your choice of operation (+, -, *, /, ^, √): ')

        s_number=''
        while is_int_float(s_number)==False:
            s_number=input('\nEnter your next number: ')

        function=operations[operation_choice]

        answer=function(float(f_number),float(s_number))

        print(f'\nCALCULATION: {f_number} {operation_choice} {s_number} = {answer}')

        options=["Y","N","OFF"]
        while continue_cancel not in options:
            continue_cancel=input(f'\nEnter "Y" to continue calculating with {answer} or "N" to start a new calculation or "OFF" to end application: ').upper()
            if continue_cancel not in options:
                print('Please enter "Y","N", or "OFF"')
                
        if continue_cancel=='Y':
            f_number=answer
            continue_cancel=True
        elif continue_cancel=='N':
            print('\n\n---New Calculation---')
            calc()
        elif continue_cancel=='OFF':
            print('\nGoodbye.') #does not print for some strange reason
            return
calc()

















