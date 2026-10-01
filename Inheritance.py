# Inheritance - It is a process of acquiring properties from one class to other class(Parent-Child/ Super-Sub)

# # Types of Inheritanse:
# # 1. Single Inheritance - One parent to One child
# # Parent Class
# class Animal:
#     def eat(self):
#         print('Animal Eats')
# # Child Class
# class Lion(Animal):
#     def roar(self):
#         print('Lion Roars')
# l=Lion()
# l.roar()
# l.eat()
# l.roar()



# # Multiple Inheritance:
# # One child inherits properties from multiple parents
# class Father:
#     def father_properties(self):
#         print("Father's Properties")
# class Mother:
#     def mother_properties(self):
#         print("Mother's Properties")
# class Child(Father, Mother):
#     def child_properties(self):
#         print("Child's Properties")
# c=Child()
# c.father_properties()
# c.mother_properties()
# c.child_properties()


# # Multilevel Inheritance:
# # Inheritance happens across multiple levels
# # Grandparent ->Parent ->Child
# class GrandParent:
#     def house(self):
#         print("Grandparent's House")
# class Parent(GrandParent):
#     def car(self):
#         print("Parent's Car")
# class Child(Parent):
#     def bike(self):
#         print("Child's Bike")
# c=Child()
# c.house()
# c.car()
# c.bike()
    


# # Hierarchial Inheritance:
# # One Parent -> Multiple Child class
# class Animal:
#     def eat(self):
#         print("Animal Eat's")
# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")
# class Cat(Animal):
#     def meow(self):
#         print('Cat Meows')
# d = Dog()
# c = Cat()
# d.eat()
# d.bark()
# c.eat()
# c.meow()


# # Hybrid Inheritance -
# # Combination of two or more types of inheritance
# class A:
#     def method_a(self):
#         print('A')
# class B(A):
#     def method_b(self):
#         print('B')
# class C(A):
#     def method_c(self):
#         print('C')
# class D(B, C):
#     def method_d(self):
#         print('D')
# d = D()
# d.method_a()
# d.method_b()
# d.method_c()
# d.method_d()


# # Super Method - In python super is used to access functionaly from the parent class functionality
# class Parent:
#     def show(self):
#         print("Parent Method")
# class Child(Parent):
#     def show(self):
#         super().show()  # without this super keyword here we don't get to print the output as Parent Method without it the method in child overrides the parent and prints output as only Child Method
#         print('Child Method')
# c= Child()
# c.show()


# # Super() Method with Constructor:
# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__(self,name,marks):
#         super().__init__(name)
#         self.marks=marks
# s = Student('Ram',99)
# print(s.name)
# print(s.marks)


# # Vehicle and Car
# class Vehicle:
#     def start(self):
#         print('Start the Engine')
#     def stop(self):
#         print('Stop the Engine')
# class Car(Vehicle):
#     def drive(self):
#         print('Drive th eVehicle')
# c= Car()
# c.start()
# c.drive()
# c.stop()

# # Person and Student
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
# class Student(Person):
#     def __init__(self,name,age,roll_no,course):
#         super().__init__(name,age)
#         self.roll_no=roll_no
#         self.course=course
#     def display(self):
#         super().display()
#         print(self.roll_no,self.course)
# s=Student('Ram',99,1,'CSE')
# s.display()