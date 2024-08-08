
number1 = int(input('Digite o primeiro número:'))
number2 = int(input('Digite o segundo número:'))
operation = input('Digite a operação que deseja realizar (+, -, *, /): ')

if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(abs(number1 - number2))
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    print(number1 / number2)
else:
    print('Operador inválida')