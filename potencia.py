#Faça um programa que receba dois numeros e calcule
#o primeiro elevado ao segundo. Sem ultilizar o **

num1 = int(input('Informe um numero:'))
num2 = int(input('Informe um expoente:'))
resultado = 1

while num2 > 0:
    resultado *= num1
    num2 -= 1

print(resultado)