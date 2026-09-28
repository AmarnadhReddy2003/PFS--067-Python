# 1
# 12
# 123
# 1234
# 12345
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

#1
#22
#333
#4444
#55555
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

#5
#54
#543
#5432
#54321

# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#     for j in range(n,n-i,-1):
#         print(j,end='')
#     print()

# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(' ', end='')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(' ', end='')
#     for j in range(1,n-i+1):
#         print(j,end=' ')
#     print()

#1
#2 3
#4 5 6
#7 8 9 10

# n=int(input('Enter the number: '))
# num=1
# for i in range(1,n):
#     for j in range(i):
#         print(num, end=' ')
#         num+=1
#     print()

# n=int(input('Enter the number: '))
# for i in range(1,n):
#     for j in range(1,n):
#         print(j,end=' ')
#     print() 

# n=int(input('Enter the number: '))
# for i in range(1,n):
#     for j in range(n,0,-1):
#         print(j,end=' ')
#     print() 

# n=int(input('Enter the number: '))
# for i in range(n,0,-1):
#     for j in range(n,n-i,-1):
#         print(j,end=' ')
#     print() 

# n=int(input('Enter the number: '))
# for i in range(1,n):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print() 

# # Pyramid Pattern of numbers
# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(' ', end='')
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()


# # Reverse pyramid of stars
# n=int(input('Enter the number: '))
# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(' ', end='')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()




# n=int(input('Enter the number: '))
# # Upper Pyramid
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(' ', end='')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()
# # Lower pyramid
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(' ', end='')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()


#CODE

#C
#CO
#COD
#CODE
# name='RAMAYAN'
# for i in range(1,len(name)+1):
#     for j in range(i):
#         print(name[j], end='')
#     print()

# name='RAMAYAN'
# for i in range(0,len(name)):
#     for j in range(i+1):
#         print(name[j], end='')
#     print()




# n=5
# for i in range(1,n+1):
#     #Spaces before the pyramid


# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(' ',end='')
#     for j in range(1,i+1):
#         if i==1 or i==n or i+j==n+1 or j+i==n+1:
#             print("*",end=' ')
#         else:
#             pass
#     print()

# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#     for j  in range(1,n+1):
#         if i==j or i+j==n+1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# def print_v_pattern(n):
#     """
#     Prints a symmetric 'V' star pattern of a given height n.
#     The total width of the pattern is always (2 * n - 1).
#     """
#     for i in range(n):
#         for j in range(2 * n - 1):
#             # Print '*' at the left arm (j == i) and right arm (j == 2 * n - 2 - i)
#             if j == i or j == (2 * n - 2 - i):
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         # Move to the next line after each row
#         print()

# # Example usage:
# if __name__ == "__main__":
#     height = 5
#     print(f"V Shape Star Pattern (Height = {height}):\n")
#     print_v_pattern(height)

# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or i==n or j==n or i==j or i+j==n+1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# # V shape pattern printing
# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if i==j or j==2*n-i:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# # Hallow triangle pattern 
# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if i==n or j==n+1-i or j==n+i-1:
#             print("*", end=' ')
#         else:
#             print(' ', end=' ')
#     print()


