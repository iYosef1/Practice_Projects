
a = '''
___  ___
\  \/  /
 >    < 
/__/\_ \\
      \\/
        
___  ___
\  \/  /
 >    < 
/__/\_ \\
      \\/

 h      
'''


x = '''
 ______________   --------------   
| ------------ | | A            |  
||     __     || |              |  
||    /__\    || |      __      |  
||   //  \\\   || |     /  \     |  
||  |   _/ |  || |    _\  /_    |  
||  |  |   |  || |   /      \   |  
||   \ o  /   || |   \_/||\_/   |  
||    \__/    || |      ||      |  
||____________|| |            A |  
 --------------   --------------   
'''


b = ''' -------------- 
| A            |
|              |
|      __      |
|     /  \     |
|    _\  /_    |
|   /      \   |
|   \_/||\_/   |
|      ||      |
|            A |
 -------------- '''


c = '''

 ______________     
| ------------ |  
||     __     || 
||    /__\    || 
||   //  \\\   || 
||  |   _/ |  ||   
||  |  |   |  ||  
||   \ o  /   || 
||    \__/    ||  
||____________||  
 --------------  


'''



d = '''
        __                         
  ____ |  | _______  _____  ___.__.
 /  _ \|  |/ /\__  \ \__  \<   |  |
(  <_> )    <  / __ \_/ __ \\___  | 
 \____/|__|_ \(____  (____  / ____|
            \/     \/     \/\/     
'''





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
    final_art_length = max(depth) #max(depth) + 1 will add a line to arts drawn
    #print(final_art_length)
    #print(xtra_rows_list)
    #print(list_max)
    return xtra_rows_list, list_max, final_art_length



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
            pass
            #space = ' '*space_count #remove comment to add an extra row to arts
            #art.append(space)       #remove comment to add an extra row to arts
        else:
            for num in range(row): #range(row + 1) will add another row to arts printed, also add 1 to final_art_length
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


        






class AdjacentPrint:

    def __init__(self, filler):
        self.filler = filler
        #self.list = list_item #list of lists
        #self.dictionary = dictionary_item #dictionary of lists
        #self.ascii_arts = ascii_arts_gallery #dictionary of ascii arts (lists)

    def write(self, text):
        print(text, end = self.filler)

    def close(self):
        print()

    def adjacent_lists(self):
        #used on a list of lists or a dictionary of lists by index or key, respectively
        #with column and row space
        pass

    def draw_ascii(self, art_gallery, names_list, chosen_arts = False):
        if type(art_gallery) == type([ ]):
            dicti = ascii_art_dictionary(art_gallery, names_list)
            art_dicti = dicti[0]
            final_art_length = dicti[1]
            if type(chosen_arts) == type([]):
                for line in range(final_art_length):
                    for art in chosen_arts:
                        print(art_dicti[art][line], end = self.filler)
                    print('')
                return     
            for line in range(final_art_length):
                for item in art_dicti:
                    print(art_dicti[item][line], end = self.filler)
                print('')
            return
        else:
            print('Please pass in a list of ascii arts as your argument.')
            return








