#! python3

import re, pyperclip


#email address regex:
email_regex = re.compile(r'( \S{2,}@[a-z]{2,}\.[a-z]{1,7}\.?[a-z]{1,7} )')
#NOTE: This regex code correctly prints out 400 email addresses from the examplePhoneEmailDirectory.pdf file



#phone number regex:
phone_regex = re.compile(r'''

(

(
((\d\d\d)|(\(\d\d\d\)))      #area code
(-|\s)                       #dash or space after area code
)?                           #note: grouped area code, 0 or 1

\d\d\d-\d\d\d\d              #phone number w/o area code

(
(\s|,\s)                     #space or comma-space between phone number and extension, IF extension found
((ex?t?n?)|x)\.?\s?          #extension word-part
\d{1,6}                      #extension number-part
)?                           #note: grouped extension, 0 or 1

)                            #grouped entire phone number & extension

''', re.VERBOSE | re.IGNORECASE)
#NOTE: This regex code prints out 719 phone numbers from the examplePhoneEmailDirectory.pdf file








#############################

#in py file text-sample for testing scraper

phone_num = '''
1- (905) 934-2363    
2- 416-534-6432    
3- 324-2343   
4- (647) 472-0033

5- 416-757-1243 ext. 2334 
6- 580-3453 Ex 435
7- (289) 345-9001 EXTN 32
8- 416-757-1243 e. 2334 
9- 580-3453 Ext. 435
10- (289) 345-9001 EXTN. 32
11- (289) 345-2342 x. 32
12- 416-888-1243 X 2334 
13- 520-3242 E. 435
14- (289) 325-3422 Extn. 32
15- 416-300-9999, ext. 2334 

'''

email = ' chendurn1@hotmail.com  rando@gmail.com '

#testing:
phone_numbers = phone_regex.findall(phone_num)
#print(phone_numbers)
for tup in phone_numbers:
    print(tup[0])

############################




text = pyperclip.paste() #right-click to copy any text file with phone numbers and email addresses, then run program


extracted_emails = email_regex.findall(text)
phone_numbers = phone_regex.findall(text)


#check tuples here:
print(phone_numbers)

extracted_phone_numbers = []
for tup in phone_numbers:
    extracted_phone_numbers.append(tup[0])
    #print(tup[0])


phone_number_str = '\n'.join(extracted_phone_numbers)
email_addresses_str = '\n'.join(extracted_emails)



allresults = phone_number_str + '\n\n' + email_addresses_str
pyperclip.copy(allresults)  #running program will copy the results for you that can be pasted immediately after (anywhere you choose)


#print(phone_number_str)
#print(email_addresses_str)



print('Number of Phone Numbers:',len(extracted_phone_numbers))
print('Number of Email Addresses:',len(extracted_emails))







'''
comma_regex = re.compile(r', ')

rando = 'hi yes, no , ok ,ya  ,'

mo = comma_regex.findall(rando)

print(mo)
'''
