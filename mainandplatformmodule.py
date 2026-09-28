# import calc

# print(calc.add(10,20))
# print(calc.sub(40,39))
# print(calc.mul(2,9))
# print(calc.div(20,2))

# # Types of Modules
# # 1. Built-in/Standard Library Modules - These come with python indefault
# # Eg: math,random,sys,os,datetime,statistics,calculator
# import math
# print(math.sqrt(144))


# 2. User defined Modules
# import calc   # User defined module
# from calc import add,sub
# print(calc.add(10,20))

# 3. Third party Modules: These are developed outside Pyhton's standard library and are normally installed separately
# Eg: requests,django,flask,pandas,numpy

# # Module Varaible - We can also create variables in the module and import that module and use the particular variable in it 
# import calc
# print(calc.name)
# print(calc.age)
# print(calc.company)

# import math # Built-in Module
# print(math.sqrt(225))
# print(math.pow(2,3))
# print(math.ceil(4.2)) # ceil Rounds the current float number to next number even when it is 1.00001 the ceil will give output as 2 
# print(math.floor(4.8))
# print(math.factorial(5))
# print(math.pi) 
# radius = 5
# area=math.pi*radius*radius
# print(area)

# import random
# number=random.randint(1,10)
# print(number)
# names=['Ram','Seetha','Lakshman','Ravi','Vayu']
# name = random.choice(names) # It chooses the random name from a list of collections
# print(name)

# import random
# nums=[1,2,3,4,5,6,7,8,9]
# random.shuffle(nums)
# print(nums)

# # sys Module
# import sys
# print(sys.version)

# # sys.argv - Contains command line arguments
# import sys
# name=sys.argv[1]
# print('Hello', name)

# # exit() - Terminates the when it sees exit()
# import sys
# age=15
# if age<18:
#     print('Not Eligible')
#     sys.exit() # Trerminates program, Here without this exit we get ojutput as Eligible because it's outside the condition 
# print('Eligible')

# # Platform Module - It is used to get info about computer operating system, pyhton version,
# import platform
# print(platform.system()) # Returns operating system name
# print(platform.release()) # Returns latest os version in the current system
# print(platform.version()) # Returns the present version of windows
# print(platform.machine()) # Returns the machine architecture like 32or 64 bit 
# print(platform.processor()) # Returns the version of processor
# print(platform.python_version()) # Returns the python's current version in the sysytem
# print(platform.python_implementation())

# import platform
# if platform.system()=='Windows':
#     print('Running on Windows')
# elif platform.system()=='Linux':
#     print('Running on Linux')
# else:
#     print('Nothing')
