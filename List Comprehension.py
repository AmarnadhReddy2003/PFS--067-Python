# List Comprehension - A list comprehension is a short and clean way of creating a list using loops
# numbers=[]
# for i in range(1,6):
#     numbers.append(i)
# print(numbers)

# # List comprehension
# numbers=[i for i in range(1,6)]
# print(numbers)
# # One line representation of loop
# # Syntax: [expression for variable in iterable]
# # [x for x in range(1,n)]

# # Squares printing
# squares=[i*i for i in range(1,6)]
# print(squares)

# # List comprehension on strings
# names=['Ram','Vijay','Ravi', 'Ajay']
# result=[name.upper() for name in names]
# print(result)


# # Printing even numbers using list comprehension
# numbers=[i for i in range(1,11) if i %2 == 0]
# print(numbers)


# # Filtering values using list comprehension
# nums=[10,15,20,25,30,40,60]
# result=[n for n in nums if n>20]
# print(result)


# Nested list comprehension - It means having more than one for loop inside list comprehension
# Normal version
# result=[]
# for i in range(1,4):
#     for j in range(1,4):
#         result.append((i,j))
# print(result)


# # Using list comprehension
# result=[(i,j) for i in range(1,4) for j in range(1,4)]
# print(result)

# matrix= [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result=[x for row in matrix for x in row]
# print(result)


# matrix= [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result=[y for x in matrix for y in x]
# print(result)


# # Generators - it produces the each value at a time when it's required
# def numbers():
#     for i in range(1,6):
#         yield i
# print(numbers)
# Yield - It passes the function and remebers it's current state

# def numbers():
#     yield 1
#     yield 2
#     yield 3
# result= numbers()
# print(next(result)) # # Here we should use next() because without it we get only objectt address not the actual value itself
# print(next(result)) # # Here yield in generators is similar to return in functions 
# print(next(result))

# def numbers():
#     for i in range(1,6):
#         yield i
# result=numbers()
# print(result)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


# # yield vs return
# def demo():
#     return 10
#     return 20
# print(demo()) # # Here we get only 10 value because when ever the interpreter sees it it just return the values to function it called and then stops executing further anything 

# def demo1():
#     yield 1
#     yield 2
#     yield 3
# result= demo1()
# print(next(result))
# print(next(result))
# print(next(result))

# # Using generator with for loop
# def numbers():
#     for i in range(1,6):
#         yield i
# for x in numbers():
#     print(x)

# # Generator Expression
# # List comp = []
# # Generator comp = ()
# nums=(x*x for x in range(1,6))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# We needt o use generators when we want to generate values at a time
def even():
    for i in range(1,21):
        if i% 2==0:
            yield i
for x in even():
    print(x) 