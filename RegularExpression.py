# # Regular Expression - It is a pattern used to search,match,extract or validate text.
# # re.search() - 
# import re
# text = 'Ima leraning Python'
# result=re.search('Python',text)
# print(result)

# We need to use search when we want to know as 'does this pattern occurs somewhere in text'

# # re.match() - It checks the pattern only at the beginning 
# import re
# text = 'From Day One Im focusing on Python and It is Easy'
# result=re.match('Python',text)
# print(result)

# # re.fullmatch() - It requires the entire string to match the pattern
# import re
# text = 'From Day One Im focusing on Python and It is Easy'
# result=re.fullmatch('Python',text)
# print(result) # It prints the value only when it has only the searching element even the text has extra space in it it would be None as output

# # re.findall() - It finds all occurances of pattern in a file and then returns as a list
# import re
# text= 'I have 10 apples and 20 oranges'
# # \d - digits (digits from 0 to 9)
# # \d+ - combination of one or more digits
# result=re.findall(r"\d+",text) # Here when we use '+' we get the output as ['1','0','2','0'] but here we got ['10', '20'] because we have used \d+ 
# print(result)


# # Word characters
# import re
# text='Python_123'
# result=re.findall(r'\w',text)
# print(result)


# import re
# text='Python_123'
# result=re.findall(r'\w+',text)
# print(result)

# # ^ - Start of String
# # The pattern must start at beginning
# import re
# pattern=r"^Python"
# print(re.search(pattern,'Python is easy'))


# # $ - Pattern must end at the end of the string
# import re
# pattern=r"Python$"
# print(re.search(pattern, 'is easy Python'))

# r " ^"

# Quantifiers - It is used to specify how many times a character or group of characters can occur in a string
# * - Zero or more occurrences of the preceding character or group
# + - One or more occurrences of the preceding character or group 
# ? - Zero or one occurrence of the preceding character or group
# {} - Specifies the exact number of occurrences of the preceding character or group

# import re
# value=input('Enter the String: ')
# pattern=r"^\d+$"

# if re.fullmatch(pattern,value):
#     print('Only Digits')
# else:
#     print('Invalid')



# # Phone Number Validation Program
# import re
# phone=input('Enter Number: ')
# pattern=r"^[6-9]\d{9}$"
# if re.fullmatch(pattern,phone):
#     print('Valid')
# else:
#     print('Invalid')


# # Email Validation
# # username@domain.com
# # r"^[\w.-]+@[\w.-]+\.\w+$"
# # [\w.-]+ - user name 
# # [\w.-]+ - domain
# # \. - dot opearation
# # \w+ - .com or .in 
# import re
# email=input('Enter Email: ')
# pattern=r"^[\w.-]+@[\w.-]+\.\w+$"
# if re.fullmatch(pattern,email):
#     print('Valid')
# else:
#     print('Invalid')

# # Name Password Validation
# import re
# name=input('Enter Name: ')
# password=input('Enter the password: ')

# # Name
# if re.fullmatch(r"[A-Za-z]+",name):
#     print('Valid')
# else:
#     print('Invalid')

# # Password pattern
# pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
# if re.fullmatch(pattern,password):
#     print('Valid')
# else:
#     print('Invalid')

# # r- raw string
# # ^ - start of string
# # ?=. - positive lookahead  
