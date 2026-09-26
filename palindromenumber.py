# Palindrome Number: The number which is same from start and end too eg: 121, 12321
num=int(input("Enter the number: "))
original=num
reverse=0
while num>0:
    digit=num % 10
    reverse= reverse*10+digit
    num//=10
if original == reverse:
    print('Palindrome')
else:
    print('Not a Palindrome')
