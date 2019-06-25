#Solicite 2 numeors inteiros de um usuário.
#Exiba todos os numeros entre eles

num1 = int(input('Informe um numero:'))
num2 = int(input('Informe outro numero:'))


if num1 < num2:
    num1 += 1
    while num1 < num2:
        print(num1)
        num1 += 1

if num1 > num2:
    num1 -= 1
    while num1 > num2:
        print(num1)
        num1 -= 1