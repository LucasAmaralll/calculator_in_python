print("\n Calculator in Python ")
number1 = int(input('Enter the number you want to perform the operation: '))
number2 = int(input('Enter the second number you want to perform the operation on: '))
operacao = input("dEnter the operation you want to perform +, -, /, *: ")
if operacao == '+':
    print(number1+number2)
elif operacao == '-':
    print(number1-number2)
elif operacao == '/':
    print(number1/number2)
elif operacao == '*':
    print(number1*number2)
else: print('Try again')