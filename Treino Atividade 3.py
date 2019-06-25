#3 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_semana = int(input('Digite um número correspondente a semana, ex: 1-Domingo, 2-Segunda e etc:'))

if dia_semana == 1:
    print('É domingo')

elif dia_semana == 2:
    print ('É segunda')

elif dia_semana == 3:
    print('É terça')

elif dia_semana == 4:
    print('É quarta')

elif dia_semana == 5:
    print('É quinta')

elif dia_semana == 6:
    print('É sexta')

elif dia_semana == 7:
    print('É sábado')

else:
    print('Valor inválido')