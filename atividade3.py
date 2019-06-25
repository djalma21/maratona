#Faça uma calculadora. Na calculadora o usuário deve informar um numero
#uma operação e outro numero. O programa deve exibir o valor da conta.

num1 = int(input('Digite um número: '))
operador = input('Digite um operador. Ex: +  -  *  / ')
num2 = int(input('Digite outro número: '))

if operador == '+':
    print('Resultado é:' ,num1 + num2)
elif operador == '-':
    print('Resultado é:' ,num1 - num2)
elif operador == '*':
    print('Resultado é:' ,num1 * num2)
elif operador == '/':
    print('Resultado é:' ,num1 / num2)
else:
    print('Operação invalida!')