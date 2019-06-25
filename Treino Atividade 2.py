#2 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

numero_int = int(input('Informe um numero:'))
numero_int2 = int(input('Informe outro numero:'))
numero_real = int(input('Informe um numero real:'))

print('O dobro do primeiro com a metade do segundo é:',numero_int * 2 + numero_int2 / 2)
print('A soma do triplo do primeiro com o terceiro é:',numero_int * 3 + numero_real)
print('O terceiro elevado ao cubo é:',numero_real**3)
