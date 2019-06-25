n1 = int(input('Informe um numero:'))
n2 = int(input('Informe outro numero:'))


menor = n1
maior = n2

if n1 > n2:
    maior = n1
    menor = n2

menor += 1
while menor <= maior:
    if menor % 2 != 0:
        print(menor)
    menor += 1