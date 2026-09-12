# # List Concatenation
# a= [10,20]
# b= [30,40]
# print(a+b)

# a=[10,20,30]
# b=40
# # TypeError: can only concatenate list (not "int") to list

# # List Repetition 
# a= [10,20]
# print(a*5)

# Built in Functions:
# These are created to reduce th human effort by simply writing the complete code in the functons, which are called as built in funvctions.
# a= [100,20,30,60,90,50,60]
# print(len(a)) # 6
# print(max(a)) # 60
# print(min(a)) # 10
# print(sum(a)) # 210
# print(sorted(a)) # Gives in order


# # List Methods
# # 1.append - Adding element to the end
# a=[10,20,30]
# # list_name.append(value) - Syntax
# a.append(50)
# print(a)


# # Extend - Adding multiple elements 
# nums= [1,2,3,4,5]
# nums.extend([6,7,8])
# print(nums)
# # nums.append(9,8) # TypeError: list.append() takes exactly one argument (2 given)

# # Insert() - Insert a value at specified index
# a=[10,20,30]
# a.insert(1,11)
# print(a)

# # Remove - Removes the first matching value
# # Even though w emay have duplicates, it still removes only one value which occurs first
# a=[10,20,30,40,10] # Removes the specified value which occurs first, even when it has duplicates.
# a.remove(10)
# print(a)

# # pop - It remves the value based on the index and returnns the value 
# list=[100,203,456,986]
# print(list.pop(2)) # Deletes the value and returns the deleted value so it gives 456 as output.

# # Index() - Return the index of first occured value 
# a=[1,2,3,4,5]
# print(a.index(4))

# # Count- Counts the no of times an element is repeated
# nums=[1,2,3,1,4,5,5,5,5]
# print(nums.count(5))

# # Sort() - Sort the existing list in place( It modifies the list there it self and updates the it )
# nums= [345,57,122.34,67]
# print(nums.sort()) 

# # Sorted - It gives the new list (It gives th eentire new list as the result )
# nums= [345,57,122.34,67]
# result= sorted(nums)
# print(result) 
# print(nums)

# Reverse - Reverses the list
reve= [9,8,7,6,5,4,3,2,1]
reve.reverse()
print(reve)

