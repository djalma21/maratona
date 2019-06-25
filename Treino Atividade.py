#1 - Tendo como dado de entrada a altura (h) de uma pessoa, e o sexo construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = input('Informe M para masculino e F para feminino: ')
altura = float(input('Informe sua altura:'))

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print ('Seu peso ideal é:', peso_ideal)
if sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print('Seu peso ideal é:', peso_ideal)