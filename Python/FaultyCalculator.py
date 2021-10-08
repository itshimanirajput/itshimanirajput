"""
Design a calculator which will correctly solve all the problems except the
following ones:
        25+9= 50, 20*5=200, 100/10=5, 50-25=75

   Your program should take operator and the two numbers as input from the user and then return the result...

"""

print('Enter first number: ')
a = int(input())
print('Enter second number: ')
b = int(input())
print('Enter an operator: ')
op = input()

if op == '+' and a == 25 and b == 9:
    print(50)
elif op == '*' and a == 20 and b == 5:
    print(200)
elif op == '/' and a == 100 and b == 10:
    print(5)
elif op == '-' and a == 50 and b == 25:
    print(75)
elif op == '+':
    print(a+b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
elif op == '-':
    print(a-b)
else:
    print('Invalid Input')


