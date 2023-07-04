print('Note: functions and/or classes from building_blocks_module.py is in use\n\n\n') #TO SHOW IN MAIN.PY FILE

#Imported:
import re, math, pprint
import os
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' #connects to tesseract program

#back_slash = None
#print(symbols)
#symbols does not contain single backslash, fix later

#Other:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '*', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', "'", '<', '>', ',', '.', '\\', '/', '?']



#print('============================Personal CLasses & Functions============================')

             
#pyperclip.copy('yes')
#pyperclip.paste()

#create a list function that returns NOT ONLY the first index or first item respectively by the item name or index number passed in as arguement.
#such is the case when there are duplicates in a list
#above and below
#for iterations especially function that will point to next index (second, third, fourth, etc.) of duplicate items is needed
#rather than have function point to same/first index of first item (second, third, fourth, etc. times)

#create function that removes all items of name/value x from list with custom-remove method


def keyboard_preference(code=None):
    '''This function will return a list of your preferred combination of keys for your keyboard.
    The list can contain a combination of letters, numbers, and/or symbols.'''
    preferred_keyboard=[]
    letters_opt=''
    numbers_opt=''
    symbols_opt=''
    if code==None:
        print('Enter 1 for YES or 0 for NO.')
        while letters_opt!='1' and letters_opt!='0':
            letters_opt=input('Would you like your keyboard to have letters (1/0)?: ') 
            if letters_opt=='1':
                preferred_keyboard=preferred_keyboard+letters
        while numbers_opt!='1' and numbers_opt!='0':
            numbers_opt=input('Would you like your keyboard to have numbers (1/0)?: ') 
            if numbers_opt=='1':
                preferred_keyboard=preferred_keyboard+numbers
        while symbols_opt!='1' and symbols_opt!='0':        
            symbols_opt=input('Would you like your keyboard to have symbols (1/0)?: ') 
            if symbols_opt=='1':
                preferred_keyboard=preferred_keyboard+symbols
        if letters_opt+numbers_opt+symbols_opt=='000':
            print('There is no keyboard available for 000.')
            return
    elif code in ['111','100','010','001','110','011','101']:
        #for _ in code:
        if code[0]=='1':
            preferred_keyboard=preferred_keyboard+letters
        if code[1]=='1':
            preferred_keyboard=preferred_keyboard+numbers            
        if code[2]=='1':
            preferred_keyboard=preferred_keyboard+symbols
    else:
        print('Please enter a valid 3-digit code of 1s and 0s to return a keyboard.')
    return preferred_keyboard

#print(keyboard_preference('100'))
#print(keyboard_preference())







def txt_from_image(img_name, img_size = 3, show_image = False, error_notice = False):
    """
    This function scrapes the text from an image and returns a string. The
    parameters for this function include image's name & it's extension. The
    size can be readjusted for the accuracy of the text scraped returned but
    preset size of 3 works fairly well.
    """
    split_tup = os.path.splitext(img_name)
    if split_tup[1] in ['.png', '.PNG', '.jpeg', '.JPEG', '.jpg', '.JPG']:
        img = img_name
    else:
        if error_notice == True:
            print('Enter appropriate file name and/or extension.')
        return
    img = cv2.imread(img, 0)
    img = cv2.resize(img, (0, 0), fx = img_size, fy = img_size) #proportional size change
    threshold_value = 169
    _, th1 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(th1)
    if show_image == True:
        show_img = cv2.imshow('original image', img)
        show_updated_img = cv2.imshow('updated', th1)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return text

#print(txt_from_image('test_image.png'))







def func_on_dir(funcs_tup, directory = None, target = False, dir_check = False):
    """
    This function runs through every folder and/or file in it's cwd and applies the
    function(s) in the tuple parameter, funcs_tup. The 1st function will be applied
    on files, the 2nd function on folders. If only 1 function is passed into parameter,
    then only 1 function will run on either files alone (target = True) or both files
    and folders (target = False). If a directory consists of both files & folders BUT
    a function is required to be performed on ONLY folders, then pass in a null function
    for files (target = True).
    """
    if directory == None:
        cwd = os.getcwd()
    else:
        cwd = os.chdir(directory)

    directory_content = os.listdir(cwd)
    #print(directory_content)
    results = []
    if target == True:
        for item in directory_content:
            file_check = os.path.isfile(item)
            if file_check == True:
                if type(funcs_tup) != type(()):
                    action = (item, funcs_tup(item))   
                elif type(funcs_tup) == type(()):
                    action = (item, funcs_tup[0](item))
            elif file_check == False:
                if type(funcs_tup) == type(()):
                    action = (item, funcs_tup[1](item))
                else:
                    action = (item, None)
            results.append(action)
    else:
        for item in directory_content:
            action = (item, funcs_tup(item))
            results.append(action)
    return results

#results = func_on_dir(funcs_tup = (txt_from_image), target = True)
#print(results)








def null_func(x):
    pass

def dir_walk_transform(funcs = (null_func, null_func)):
    """
    This function transforms every file and/or folder with the tupe of
    2 functions passed in as the parameter.
    """
    for folder_name, subfolders, filenames in os.walk('.\\'):
        if os.path.basename(folder_name) in os.listdir('.\\'):
            folder_name = folder_name.upper()
            print('\n\n')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('Folder: ', folder_name)
        
        if subfolders != []:
            print('Subfolders in', folder_name, 'are:', subfolders)
            for folder in subfolders:
                print('\n------------------------------------------------------------------------------------------------')
                print('FOLDER NAME:', folder)
                print(funcs[0](folder_name + '\\' + folder))
                print('------------------------------------------------------------------------------------------------\n')
        else:
            print('Subfolders: N/A')
            
        if filenames != []:
            print('Filenames in', folder_name, 'are:', filenames)
            for file in filenames:
                print('\n------------------------------------------------------------------------------------------------')
                print('FILE NAME:', file)
                print(funcs[1](folder_name + '\\' + file))
                print('------------------------------------------------------------------------------------------------\n')
        else:
            print('Files: N/A')
            
        print('')
        
    print('\n\n\nFINISHED.')

#dir_walk_transform(funcs = (null_func, txt_from_image))








def find_page_in_dictionary_book(dictionary_book, \
                                 search_by = None, \
                                 page_no = False, \
                                 key_query = 'Enter the term you want to search for: ', \
                                 value_query = 'Enter the definition you want to find: '):
    """
    This function takes a list of dictionary items and treats the list as a
    'book'. Each dictionary item in the list is a 'page' or 'section' from the
    'book'. You can search for a key-value pair within any dictionary by 'term',
    i.e., key, or by 'meaning', i.e., value. A search for an item within a
    dictionary will return an entire dictionary or 'page(s)' of the 'book'.
    Make page_no parameter True to add a dictionary title at first index of list.
    You can change the key and value query for your program as per context.
    """
    if page_no == True:
        book_title = input('Enter a name for your dictionary: ')
        dictionary_book.insert(0, book_title)
        dictionary_book = dictionary_book[1:] 
    all_terms = []
    all_definitions = []
    for page in dictionary_book:
        for term, meaning in zip(page.keys(),page.values()):
            term = term.lower()
            meaning = meaning.lower()
            page[term] = meaning
            all_terms.append(term)
            all_definitions.append(meaning)  
    all_terms = list(set(all_terms))
    all_definitions = list(set(all_definitions))    
    #print(all_terms)
    #print(all_definitions)
    if search_by == 'term':
        print('Use a comma followed by a space (, ) to seperate more than one item for your search.')
        find_term = input(key_query)
        search_items = find_term.split(', ')
        find_term = []
        find_term = [item.lower() for item in search_items]
        if set(all_terms).isdisjoint(find_term):
            print('\nNo results found\n\nPlease make sure a space follows your comma if more than 1 item was listed.\n')
            return
        print('\n\nSearch Results: \n')
        for search_item in find_term:
            if search_item in all_terms:
                for page in dictionary_book:
                    for word in page.keys():
                        if word == search_item:
                            pprint.pprint(page)
                            print('\n')
            else:
                print(f'\n{search_item} not found.\n')
        
    elif search_by == 'meaning':
        print('Use a comma followed by a space (, ) to seperate more than one item for your search.')
        find_definition = input(value_query)
        search_items = find_definition.split(', ')
        find_definition = []
        find_definition = [item.lower() for item in search_items]
        if set(all_definitions).isdisjoint(find_definition):
            print('\nNo results found\n\nPlease make sure a space follows your comma if more than 1 item was listed.\n')
            return
        print('\n\nSearch Results: \n')
        for search_item in find_definition:
            if search_item in all_definitions:
                for page in dictionary_book:
                    for meaning in page.values():
                        if meaning == search_item:
                            pprint.pprint(page)
                            print('\n')
            else:
                print(f'\n{search_item} not found.\n')

#imported sample_periodic_table_16_07_2021 needs to be uncommented first
#from scraped_periodic_table_elements import sample_periodic_table_16_07_2021
#find_page_in_dictionary_book(sample_periodic_table_16_07_2021[1:], search_by = 'meaning', page_no = False)




                


def find_all_nums(string,convert=None):
    '''This function takes a string as an argument and returns a
    list of all the integers and floats in the strings. Pass in
    integer 1 as the second paramenter to return list of floats'''
    results=re.findall(r"\d{1,}.?\d{0,}",string)
    if convert==1:
        for _ in range(len(results)):
            results[_]=float(results[_])
    return results

#message='I became an Orthodox in August 2019 so I\'m 1.58 year old.'
#print(find_all_nums(message))
#print(find_all_nums(message,1))





def is_int_float(number):
    '''This functions returns True if the arguement is an integer or float, and False if otherwise.
    Fractions and any other forms of numbers cannot be passed in as an argument within this function.'''
    try:
        number=float(number)
        return True
    except:
        return False

'''
print(is_int_float(.598))
print(is_int_float('.598'))
print(is_int_float(0.598))
print(is_int_float('0.598'))
print(is_int_float(0))
print(is_int_float('0'))
print(is_int_float(5.6))
print(is_int_float('5.6'))
print(is_int_float(7))
print(is_int_float('7'))
print(is_int_float(10.0))
print(is_int_float('10.0'))
print('')
print(is_int_float(-5.6))
print(is_int_float('-5.6'))
print(is_int_float(-7))
print(is_int_float('-7'))
print(is_int_float(-10.0))
print(is_int_float('-10.0'))
print(is_int_float('not a -1'))
'''






def is_decimal(number):
    '''This functions returns True if the arguement is a decimal, and False if it's not.
    Fractions and any other forms of numbers cannot be passed in as an argument within this function.'''
    if is_int_float(number)==True:
        number=float(number)
        if number>0:
            while True:
                number-=1
                if number==0:
                    return False
                elif number<0:
                    return True
        elif number==0:
            return False
        else:
            while True:
                number+=1
                if number==0:
                    return False
                elif number>0:
                    return True
    else:
        return False

'''
print(is_decimal(5.6))
print(is_decimal('5.6'))
print(is_decimal(-5.6))
print(is_decimal('-5.6'))
print('')
print(is_decimal(0))
print(is_decimal(5))
print(is_decimal('5'))
print(is_decimal(5.0))
print(is_decimal('5.0'))
print(is_decimal(-5.0))
print(is_decimal('-5.0'))
print(is_decimal(-5))
print(is_decimal('-5'))
'''





#both functions below will include zero
#is_positive_integer
#is_negative_integer

def is_integer(number):
    '''This functions returns True if the arguement is an integer, and False if it's a float.
    Fractions and any other forms of numbers cannot be passed in as an argument within this function.'''
    if is_int_float(number)==True:
        number=float(number)
        if number>0:
            while True:
                number-=1
                if number==0:
                    return True
                elif number<0:
                    return False
        elif number==0:
            return True
        else:
            while True:
                number+=1
                if number==0:
                    return True
                elif number>0:
                    return False
    else:
        return False

'''
print(is_integer(5.6))
print(is_integer('5.6'))
print(is_integer(-5.6))
print(is_integer('-5.6'))
print('')
print(is_integer(0))  
print(is_integer(5))
print(is_integer('5'))
print(is_integer(5.0))
print(is_integer('5.0'))
print(is_integer(-5.0))
print(is_integer('-5.0'))
print(is_integer(-5))
print(is_integer('-5'))
'''




def is_natural(number):
    '''This functions returns True if the arguement is a natural number (1 <= whole number), and False if otherwise.
    Fractions and any other forms of numbers cannot be passed in as an argument within this function.'''
    if is_int_float(number)==True:
        number=float(number)
        if number>0:
            while True:
                number-=1
                if number==0:
                    return True
                elif number<0:
                    return False
        else:
            return False
    else:
        return False
    
'''
print(is_natural(5))
print(is_natural('5'))
print(is_natural(5.0))
print(is_natural('5.0'))
print('')
print(is_natural(5.6))
print(is_natural('5.6'))
print(is_natural(-5.6))
print(is_natural('-5.6'))
print(is_natural(-5.0))
print(is_natural('-5.0'))
print(is_natural(-5))
print(is_natural('-5'))
'''




def is_estimated_number(number):
    """
    This functions returns True & the first number in a string that is
    an approximation, range, and/or uncertainty. If no such number exists,
    this function returns False & "N/A".
    """
    estimated_num_regex = re.compile(r'''
    ~\s?\d+             #approximate number: tilde in front

    |                   #OR-operator

    \d+\s?–\s?\d+       #range number: long dash in middle and 1 or 0 space before & after dash

    |                   #OR-operator

    \d+\s?-\s?\d+       #range number: shorter dash in middle and 1 or 0 space before & after dash

    |                   #OR-operator

    \d+\s?±\s?\d+       #uncertainty number: uncertainty number in middle and 1 or 0 space before & after uncertainty symbol
    ''', re.VERBOSE)

    estimated_number = estimated_num_regex.findall(number)
    try:
        estimated_number = estimated_number[0]
        #print(estimated_number)
        return True, estimated_number
    except:
        return False
        
#print(is_estimated_number('45-555'))






def item_by_any_index(a_list,index):
    '''This function takes a list and an index number for its parameters. The items of the
    list passed into this function can be called by any index number outside its range.
    This functions returns an item according to the index argument passed in. It's useful
    for shifting a list's items by a value while continuing the list on repeat, an example
    case of its usefulness would be for a caesar cipher'''
    if index>=len(a_list) or index<-len(a_list):
        index=index%len(a_list)
    return a_list[index]

#endless_index_list=[0, 'yes', 'Ioan', 30]
#repeating_list=item_by_any_index
#print(repeating_list(endless_index_list,6)) 
#print(repeating_list(endless_index_list,-30)) 




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

#print(whole_calc_num(5.00001))




def str_num_value(num_string):
    """
    This function type casts the string of a number with a
    fraction bar, factorial, radical sign and/or exponent (²|³|⁴)
    into its numerical float value
    """
    pwsuperscript = {'²': '2',
                     '³': '3',
                     '⁴': '4'}
    try:
        num = float(num_string)
        #print(num)
        return num
    except ValueError:
        if '/' in num_string:
            num = num_string.split('/')
            num = float(num[0])/float(num[1])
            #print(num)
            return num
        if '!' in num_string:
            num = num_string.split('!')
            num = math.factorial(int(num[0]))
            #print(num)
            return num
        if '√' in num_string:
            num = num_string.split('√')
            if num[0] in pwsuperscript:
                denom = int(pwsuperscript[num[0]])
            else:
                denom = 2
            if num[1][-1] in pwsuperscript:
                numer = int(pwsuperscript[num[1][-1]])
                num = float(num[1].split(num[1][-1])[0])
            else:
                numer = 1
                num = float(num[1])
            power_of = numer/denom
            num = pow(num, power_of)
            #print(num)
            return num
        for exponent in list(pwsuperscript.keys()):
            if exponent in num_string:
                num_list = num_string.split(exponent)
                num = float(num_list[0])
                exponent = int(pwsuperscript[exponent])
                num = pow(num, exponent)
                #print(num)
                return num
        
#str_num_value('²√100⁴')




def bedmas_string_calc(string_equation):
    """
    This function takes a string-equation of any length that starts and ends
    with a number, along with operations (/, x, +, -) in between the numbers.
    The string-equation must contain the radical sign for root numbers and
    superscripts for indices and/or exponents.
    :param string_equation: argument will be a string-equation
    :return: float value of solved equation
    """
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
                    answer = before_operator/after_operator
                elif element == 'x':
                    answer = before_operator * after_operator
                elif element == '+':
                    answer = before_operator + after_operator
                elif element == '-':
                    answer = before_operator - after_operator
                equation_elements[equation_elements.index(element)] = answer
                equation_elements.remove(str_before_operator)
                equation_elements.remove(str_after_operator)
    final_answer = equation_elements[0]
    #print('Final Answer:', final_answer)
    return final_answer

#bedmas_string_calc('4/1 + √7⁴ / 433/45 - 8² x ³√125 + ²√100⁴ - 4/2')






###################################### PRINTING ASCII ART ADJACENTLY ######################################



def ascii_parts_only(art):
    '''
    Removes empty strings from an ascii art and breaks each line of art into
    string items and returns list of string items--NOTE: you must ensure that
    original ascii art is printed in console the way in which you intended
    before using this function on an ascii art.
    '''
    ascii_parts = art.split('\n')
    temp = []
    for part in ascii_parts:
        if part != '':
            temp.append(part)
            ascii_parts = temp
    return ascii_parts



def resize_arts_data(list_of_arts_after_ascii_parts_only):
    #data collecting
    depth = []
    length = []
    length_lists = []
    for art in list_of_arts_after_ascii_parts_only:
        no_of_pieces = 0
        for piece in art:
            no_of_pieces+=1
            #print('PIECE: ',piece, len(piece)) #don't delete, just comment out
            length.append(len(piece))
        length_lists.append(tuple(length))
        length.clear()
        depth.append(no_of_pieces)

    #number of extra rows needed for each art    
    xtra_rows_list = []
    for num in depth:
        shorter_art = max(depth) - num
        if shorter_art < max(depth):
            xtra_rows_list.append(shorter_art)

    #max space count of line for lengthening shorter art(s)  
    list_max = []
    for num in range(len(length_lists)):
        elem_counts_per_row_of_art = length_lists[num]
        max_count = max(elem_counts_per_row_of_art)
        list_max.append(max_count)
    final_art_length = max(depth) + 1
    #print(final_art_length)
    #print(xtra_rows_list)
    #print(list_max)
    return xtra_rows_list, list_max, final_art_length 
        


#VERSION FOR DICTIONARY STORAGE
def ascii_art_storage(art_list, names_list = False):
    '''
    All ascii arts placed into art_list will be returned as a dictionary
    variable, with each key representing a list (value) containing the
    ascii art's parts. By default names_list is a False boolean but if else,
    names_list must contain a list of your preferred names for your arts
    and be passed in as an argument.
    '''
    ascii_arts_list = []
    for ascii_art in map(ascii_parts_only, art_list):
        ascii_arts_list.append(ascii_art) 
    ascii_art_gallery = {}
    if names_list == False: 
        for ascii_art in ascii_arts_list:
            for each_piece in ascii_art:
                print(each_piece)
            art_name = input('Enter the your preferred name of the ascii art above: ')
            ascii_art_gallery[art_name] = ascii_art
    elif (type(names_list) == type([])) and (len(names_list) == len(ascii_arts_list)):
        for name, ascii_art in zip(names_list,ascii_arts_list):
            ascii_art_gallery[name] = ascii_art
    else:
        print('\nError: you did not pass in a list or the list does not contain the correct number of items.\n')
        return
    return ascii_art_gallery

#X = [a, b, c] #a, b, and c are all ascii arts, X is a list containing ascii arts
#print(ascii_art_storage(X))
#print(ascii_art_storage(X,['XXXXXXXXXX','YYYYYYYYY']))
#print(ascii_art_storage(X,'7'))



#VERSION FOR ADJACENT PRINTING
def ascii_art_dictionary(art_list, names_list = False):
    '''
    All ascii arts placed into art_list will be returned as a dictionary
    variable, with each key representing a list (value) containing the
    ascii art's parts. By default names_list is a False boolean but if else,
    names_list must contain a list of your preferred names for your arts
    and be passed in as an argument.
    '''
    ascii_arts_list = []    #Equivalent to X = [ascii_parts_only(a), ascii_parts_only(b), ascii_parts_only(c), ascii_parts_only(d)]
    for ascii_art in map(ascii_parts_only, art_list):
        ascii_arts_list.append(ascii_art)

    #code to add more rows for each art
    a, b, final_art_length = resize_arts_data(ascii_arts_list)
    zipped = zip(ascii_arts_list, a, b)
    for art, row, space_count in zipped:
        if row == 0:
            space = ' '*space_count
            art.append(space)
        else:
            for num in range(row + 1):
                space = ' '*space_count
                art.append(space)
                
    ascii_art_gallery = {}
    if names_list == False: 
        for ascii_art in ascii_arts_list:
            for each_piece in ascii_art:
                print(each_piece)
            art_name = input('Enter the your preferred name of the ascii art above: ')
            ascii_art_gallery[art_name] = ascii_art
    elif (type(names_list) == type([])) and (len(names_list) == len(ascii_arts_list)):
        for name, ascii_art in zip(names_list,ascii_arts_list):
            ascii_art_gallery[name] = ascii_art
    else:
        print('\nError: you did not pass in a list or the list does not contain the correct number of items.\n')
        return
    return ascii_art_gallery, final_art_length



def adjacent_ascii_print(art_gallery, filler_space, names_list, chosen_arts = False):
    if type(art_gallery) == type([ ]):
        dicti = ascii_art_dictionary(art_gallery, names_list)
        art_dicti = dicti[0]
        final_art_length = dicti[1]
        if type(chosen_arts) == type([]):
            for line in range(final_art_length):
                for art in chosen_arts:
                    print(art_dicti[art][line], end = filler_space)
                print('')
            return     
        for line in range(final_art_length):
            for item in art_dicti:
                print(art_dicti[item][line], end = filler_space)
            print('')
        return
    else:
        print('Please pass in a list of ascii arts as your argument.')
        return


#ascii_arts = [a, b, c]
#names = ['Card1', 'Card2','Card3']
#chosen = ['Card1', 'Card3']

#adjacent_ascii_print(ascii_arts, 'OOOOOO', names)
#adjacent_ascii_print(ascii_arts, 'OOOOOO', names, chosen)

###########################################################################################################


'''
while your_word.isalpha()!=True: 
    your_word=input('\nEnter the one word you want your friend to guess: ').lower() 
    if your_word.isalpha()==False:
        print('Sorry! Please enter a word with no spaces, numbers, or special characters')
    else:
        print('\n'*30)
        print(logo)


#WHILE NOT CORRECT INPUT--INPUT FUNCTION

#and, or
#==, !=, >, <, >= (greater than or equal to), <= (less than or equal to)
#checking variable types: .isdigit(), .isnumeric(), .isalpha(), .isalphanumeric(), .isinstance(object,type), len(object), etc.

'''




#input_constraints: list of specifics, bools, numbers, alphabet-only strings, custom-regexes (for phone number?), etc.
#return: bools, or if many options available then return input itself for further condition checks

def check_input(request,input_constraints,hint='off',hint_message=None):
    '''This function has 4 parameters. The 1st parameter is the input question
    as a string, the 2nd parameter's arguement will determine the constraints
    limiting your input options, the 3rd parameter requires the string "on"
    for the 4th arguement to be printed when user fails to enter a valid input.
    Constraints for the input include the following: list of specific/custom
    options, integer, natural'''
    check=''
    if type(input_constraints)==type([]):
        #for list of desired input options
        #converts list elements to strings
        for constraint,num in zip(input_constraints,range(len(input_constraints))):
            input_constraints[num]=str(constraint)
        while check not in input_constraints:
            check=input(request)
            if hint=='on':
                if check not in input_constraints:
                    print(hint_message)                 
        return check
    elif input_constraints=='integer':
        #for integers
        while is_integer(check)==False:
            check=input(request)
            if hint=='on':
                if is_integer(check)==False:
                    print(hint_message)
        return check
    elif input_constraints=='natural':
        #for natural numbers
        while is_natural(check)==False:
            check=input(request)
            if hint=='on':
                if is_natural(check)==False:
                    print(hint_message)
        return check    



#print(check_input("Please enter 0 or 1: ",[0,1])) #list of items, specifics

#print(check_input("Please enter any integer: ",'integer','on','Sorry, must be an integer!')) #integer input

#print(check_input("Please enter any natural number: ",'natural')) #integer input

    
###################################################################







#print(results.group()) #for re.search syntax result only










'''
#2--overcomplicated version of is_int_float

def is_int_float(input_string):
    if input_string.find('.')==-1:
        if input_string.isdigit()==True:
            return True
        else:
            return False
    else:
        decimal_index=input_string.find('.')
        whole_part=input_string[0:decimal_index]
        decimal_part=input_string[decimal_index+1:]
        if (whole_part.isdigit()==True or (whole_part.isspace()==True or len(whole_part)==0)) and\
           (decimal_part.isdigit()==True or (decimal_part.isspace()==True or len(decimal_part)==0)):
            return True
        else:
            return False
'''

'''
number=''
while is_int_float(number)==False:
    number=input('ENTER: ')
'''











#5, 5/10 or 5*10 and other operations, 5.9, 5
#Later add to mod: super/subscript for powers of number, (square) root numbers
#Return Boolean


#print('-------------------DONE--------------------')





#type_casting strings with int(): int strings can be converted to int but float strings cannot because of error
#type_casting strings with float(): float or int strings can be converted to float

#type_casting with int(): int can be converted to int but floats will be rounded down to an int
#type_casting with float(): float or int will be converted to a float



'''
#Notes for is_int_float(number) functions
num=''
while type(num)!=type(1):
    num=int(input("Enter your first number: "))#enter a float number to confirm statement below
#int can be converted to float BUT float canNOT be converted to int!



num1=''
while num1.isdigit()==False:
    num1=input("Enter your second number: ")
#int/float conversion at the right point in code since strings cannot be converted to such
'''








'''

#ADD NEW ITEMS TO A LIST
lst=[1,2]

def addItemsToList(listName,*newItems):
    for a in newItems:
        listName.append(a)
    return listName
print(addItemsToList(lst,10,20))

'''





'''

#CHECK IF ITEM(S) IS IN LIST
lst=[8, 8, 5, 1, 7, 0, 7, 8, 4, 1, 10, 7]

def areItemsInList(listName,*checkItems):
    x=len(checkItems)
    counter=[]
    itemsInListName=[]
    
    for item in checkItems:
        if item in listName:
            counter.append(1)    #(1)appends only if item is in list SO 1 will be added if each item is in list, 1 per item in checkItems
            itemsInListName.append(item)                  
            #print(item)         #uncomment to make comparisons on python shell
            if sum(counter)==x:  #because of (1) code can be placed on left                         
                return True      #because of (1), sum(counter)>=x is not required           
        else:
            pass
        
    missingItems=[]
    if len(itemsInListName)>0:   #remove if you don't need missing items returned
        for item in checkItems:
            if item not in itemsInListName:
                missingItems.append(item)
        print('Missing item(s):')
        return missingItems        

    return False

print(areItemsInList(lst,6,9))
   
'''    




'''

xcards=['a','b','c','d','e','f','g','h','i','j']

def players_divided_cards(number_of_cards,number_of_players,deck):
    player_hands_or_decks={}
    splits=int(number_of_cards/number_of_players)
    list_index=0-splits
    for num in range(0,number_of_players):
        player_no='player_'+str(num+1)
        list_index=list_index+splits
        player_cards=deck[list_index:list_index+splits]
        player_hands_or_decks[player_no]=player_cards
    print(player_hands_or_decks)

players_divided_cards(len(xcards),5,xcards)

'''






#print('============================END============================')
