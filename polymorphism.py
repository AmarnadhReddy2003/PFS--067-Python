# Polymorphism - poly - many mrophism - forms (One name many forms)
# Polymorphism is a concept in object oriented programming that allows objects of different classes to be treated as a objects of common super class.
# It enables a 



# class Dog:
#     def sound(self):
#         print('Dog Barks')
# class Cat:
#     def sound(self):
#         print('Cat Meows')
# d=Dog()
# c=Cat()
# d.sound()
# c.sound()


# Type of Polymorphism:
# 1. Method Overloading
# 2. Method Overriding
# 3. Operator Overloading

# # Method Overriding - It occurs when a child class provides it's own implementation of a method that already exists in parent class
# # Method Overriding
# class Animal:
#     def sound(self):
#         print('Animals makes sound')
# class Dog(Animal):
# # Here in the above we can print the value in Animal class to by using the super keyword in the Dog class
#     def sound(self):
#         print('Dog Barks')
# class Cat(Animal):
#     def sound(self):
#         print('Cat Meows')
# d=Dog()
# c=Cat()
# d.sound()
# c.sound()



# # Method Overloading - Having multiple methods with same name but different parameters
# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
# calc=Calculator()
# calc.add(10,20)
# calc.add(10,20,30) 


# # Method overloading using 1. default Arguments:
# class Calculator:
#     def add(self,a,b,c=0):
#         return a+b+c
# calc=Calculator()
# print(calc.add(10,20)) # a,b machine c=0 automatically
# print(calc.add(10,20,30)) 

# # Method overloading using 2. Using *args
# class Calc:
#     def add (self,*args):
#         return sum(args)
# c=Calc()
# print(c.add(10,20))
# print(c.add(10,20,30))
# print(c.add(10,20,30,40))
# print(c.add(10,20,30,40,50))


# # Operator Overloading - It is a way to define how operators behave for user-defined classes. In Python, we can overload operators by defining special methods in our classes. These special methods have double underscores before and after their names (e.g., __add__, __sub__, __mul__, etc.). By implementing these methods, we can customize the behavior of operators for our objects.
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return Point(
#             self.x+other.x,
#             self.y+other.y)
# p1=Point(10,20)
# p2=Point(30,40)
# p3=p1+p2
# print(p3.x)
# print(p3.y)



# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __eq__ (self, other):
#         return self.marks == other.marks
# s1= Student('A',100)
# S2=Student('B',90)
# print(s1==S2)


# # Abstraction - It is a process of hiding the implementation details and showing only functionality to the user. In Python, we can achieve abstraction using abstract classes and abstract methods. An abstract class is a class that cannot be instantiated and is meant to be subclassed. An abstract method is a method that is declared in an abstract class but does not have any implementation in that class. Subclasses of the abstract class must provide an implementation for the abstract methods.
# # It means hidingunnecessary details and showing only the required functionality.
# from abc import ABC, abstractmethod
# # ABC called as Abstract Base Class
# class Animal(ABC):
#     @abstractmethod
#     def sound(self): # Here this method should completeli imeplementd in the 
#         pass
# # Animal says that every animal must provide a sound() method
# class Dog(Animal):
#     def sound(self):
#         print('Dog Barks')
# class Cat(Animal):
#     def sound(self):
#         print('Cat Meows')
# dog=Dog()
# dog.sound()
# cat=Cat()
# cat.sound()

