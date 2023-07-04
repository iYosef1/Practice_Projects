from lxml import html
import requests
import random
import re


def is_int_float(number):
    """
    This functions returns True if the arguement is an integer or float, and False if otherwise.
    Fractions and any other forms of numbers cannot be passed in as an argument within this function.
    """
    try:
        number=float(number)
        return True
    except:
        return False




browser_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'}


def word_of_the_day():
    url = 'https://www.merriam-webster.com/word-of-the-day'
    # 'https://www.merriam-webster.com/word-of-the-day'
    page = requests.get(url, browser_headers)
    tree = html.fromstring(html=page.content)

    # word info
    wod = tree.xpath('//div[@class="word-and-pronunciation"]/h1/text()')[0]
    speech_part = tree.xpath("//div[@class='word-attributes']/span[1]/text()")[0]
    pronunciation = tree.xpath("//div[@class='word-attributes']/span[2]/text()")[0]
    word_info = f'\n{speech_part} | {pronunciation}\n'

    # definitions
    all_defs = tree.xpath("//div[@class='wod-definition-container']/child::p")
    definitions = []
    for p in all_defs:
        each_def = p.xpath('.//text()')
        definitions.append(''.join(each_def))

    for def_ in definitions:
        index = definitions.index(def_)
        if (is_int_float(def_[0]) == False) and (def_[0] != ':'):
            def_ = '  ' + def_
            definitions[index] = def_

    definitions.insert(0, word_info)
    definitions.insert(0, wod)
    the_word_of_the_day = definitions

    for columns in the_word_of_the_day:
        #print(columns)
        pass
    return the_word_of_the_day


word_columns = word_of_the_day()


def add_word_to_dict(dictionary_file):
    # for-loop used to remove ', ': necessary when writing to csv file
    # \n also removed for excel file
    word_columns[1] = word_columns[1].strip('\n')
    for num in range(len(word_columns)):
        if ', ' in word_columns[num]:
            separator_substitute = re.sub(', ', ' (comma) ', word_columns[num])
            word_columns[num] = separator_substitute
    word_columns_string = ', '.join(word_columns)
    
    with open(dictionary_file, 'a') as f:
        f.write(f'{word_columns_string}\n')


def all_words_from_dict(dictionary_file):
    all_dict_words = []
    with open(dictionary_file, 'r') as f:
        for line in f:
            line = line[:-1].split(', ')
            line[1] = '\n' + line[1] + '\n'
            for num in range(len(line)):
                if ' (comma) ' in line[num]:
                    sub_comma = re.sub(r' \(comma\) ', ', ', line[num])
                    line[num] = sub_comma
            all_dict_words.append(line)
    return all_dict_words


def your_word_for_the_day():
    all_dict_words = all_words_from_dict('Dictionary_of_Words_of_the_Day.csv')

    all_words = []
    for word in all_dict_words:
        all_words.append(word[0])

    if word_columns[0] in all_words:
        #print('Today\'s word already exists in the dictionary.\
              #\nBelow is a random word from the dictionary.\n')
        latest_word = random.choice(all_dict_words) 
        return latest_word
    else:
        add_word_to_dict('Dictionary_of_Words_of_the_Day.csv')
        updated_dict = all_words_from_dict('Dictionary_of_Words_of_the_Day.csv')
        latest_word = updated_dict[-1]
        for column in latest_word:
            #print(column)
            pass
        return latest_word


print(your_word_for_the_day())
     
        

    
    




