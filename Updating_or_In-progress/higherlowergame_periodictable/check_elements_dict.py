
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


import re

estimated_num_regex = re.compile(r'''
~\s?\d+             #approximate number: tilde in front

|                   #OR-operator

\d+\s?–\s?\d+       #range number: long dash in middle and 1 or 0 space before & after dash

|                   #OR-operator

\d+\s?-\s?\d+       #range number: shorter dash in middle and 1 or 0 space before & after dash

|                   #OR-operator

\d+\s?±\s?\d+       #uncertainty number: uncertainty number in middle and 1 or 0 space before & after uncertainty symbol
''', re.VERBOSE)


def is_estimated_number(number):
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
        print(estimated_number)
        return True, estimated_number
    except:
        return False, 'N/A'
        print('failed')
        


#number, name, symbol

elements = re.compile(r'''
    \d{1,3}             #approximate number: tilde in front

    |                   #OR-operator

    \d+\s?–\s?\d+       #range number: long dash in middle and 1 or 0 space before & after dash

    |                   #OR-operator

    \d+\s?-\s?\d+       #range number: shorter dash in middle and 1 or 0 space before & after dash

    |                   #OR-operator

    \d+\s?±\s?\d+       #uncertainty number: uncertainty number in middle and 1 or 0 space before & after uncertainty symbol
    ''', re.VERBOSE)



def pull_dict_from_list(key_or_value):
    pass







from lxml import html
from fake_useragent import UserAgent
import requests


ua = UserAgent()
browser_headers = {'User-Agent': ua.random}

url = 'https://en.wikipedia.org/wiki/Prices_of_chemical_elements'

page = requests.get(url, browser_headers)
tree = html.fromstring(html=page.content)


#print(tree)


num_each_element = tree.xpath('//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/child::td[1]')
print(num_each_element)


price_spot = tree.xpath('//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/child::td[6]/span/text()')
print(price_spot)


price_row_elements = tree.xpath('//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr')
print(price_row_elements)




url = 'https://en.wikipedia.org/wiki/List_of_chemical_elements'

page = requests.get(url, browser_headers)
tree = html.fromstring(html=page.content)

all_elements_page = tree.xpath('//table[contains(@class, "wikitable")]/tbody/tr')
print(all_elements_page)





