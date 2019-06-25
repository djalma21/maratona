#Crie um programa que receba 3 númenos do usúario e imprima o maior deles

numero1 = int(input('Insira um número: '))
numero2 = int(input('Insira outro: '))
numero3 = int(input('Insira mais um: '))

if numero1 > numero2 > numero3:
    print('O número maior é:',numero1)
if numero2 > numero1 > numero3:
    print('O número maior é:',numero2)
if numero3 > numero2 > numero1:
    print('O número maior é:', numero3)