# OOPS - Object Oriented Programming, in oops concept we write everything in class and object form.
# It is aprogramming approach where we organize our program around objects rather than only functions and variables.
# Student: 
# Data:
# - name,age,marks,roll_no
# - study(),attend_classes(),write_exam(),dislay_progress
# in oops, we combine data+ behaviour into object

# Class - It is a Blueprint/template to creat an object(no memory allocation for class)
# Object - It is an Instance of class(actual thing created from blueprint)(memory allocation is for object only not for class)

# class Student:
#     pass
# student1=Student() # student1 -> object
# student2=Student()

# Attributes(properties of object)
# Attributes are the data/properties associated with an object


# class Student:
#     pass
# student1=Student() 
# student1.name='Ram'                                 
# student1.age=23
# student1.marks=95
# print(student1.name)
# print(student1.age)
# print(student1.marks)

# # Methods - Function created are called as methods
# class Student:
#     def study(self):
#         print('Student is Studying')
# student1=Student() Here we are calling the class and storing that into the object called student1 and when accessing any method or variabble in it we should call it using object name to access it
# student1.study()
# # Method only belongs to class 

# # Constructors - It is a special method that automatically calls when object is created 
# # Syntax of constructor  __init__()
# class Student:
#     def __init__(self):
#         print('Student is Studying')
# student1=Student()
# student2=Student()
# student3=Student()

# # Constructors with Attributes
# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
# student1=Student('Ram',23,99)
# print(student1.name)
# print(student1.age)
# print(student1.marks)
# # Self represent current object 

# # Creating multiple methods with 
# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(self.name,self.age,self.marks)
# student1=Student('Ram',23,99)
# student2=Student('Seetha',21,98)
# student1.display()
# student2.display()


# # Encapsulation - It means bundling the data and methods together inside a class and controlling how that data is accessed or modified.
# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#     def withdrawl(self,amount):
#         self.balance-=amount
#     def get_balance(self):
#         return self.balance
# ba=BankAccount(100000)
# ba.deposit(10000)
# ba.withdrawl(5000)
# print(ba.get_balance())



# # When we use __(double under score for any varible), it is called as private attribute
# # Double underscore indicates a private like attribute in pyhton through name managing.
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#     def withdrawl(self,amount):
#         self.__balance-=amount
#     def get_balance(self):
#         return self.__balance
# ba=BankAccount(100000)
# ba.deposit(10000)
# ba.withdrawl(5000)
# print(ba.get_balance())


# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#         else:
#             print('Invalid Marks')
# student=Student(80)
# print(student.get_marks())
# student.set_marks(90)
# print(student.get_marks())
