# Factorial Program 5! = 1 * 2 * 3 * 4 * 5 = 120
num=int(input('Enter the number: '))
factorial=1
while num>0:
    factorial*=num
    #factorial = factorial*num
    num-=1
print(factorial)