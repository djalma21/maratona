"""Faça um programa que receba um número inteiro e positivo.
Se o numero for positivo, imprima a serie de fibonacci.
Se o numero for impar, imprima seus antecessores em decrescente ate zero.
Se o numero for par, imprima a soma de todos os numeros primos
entre este numero e zero"""

numero = int(input('Numero:'))
n = numero
quantidade_divisores = 0
fatorial = 1
msg = f'{numero}: '

if numero > 0:
    while n >= 1:
        if numero % n == 0:
            quantidade_divisores += 1
        n -= 1
    if quantidade_divisores > 2:
        print(f'{numero}: Não é primo!')

    else:
        print(f'{numero}: É primo!')

        if numero % 2 != 0:
            while numero >= 1:
                if numero != 1:
                    msg += f'{numero} , '
                numero = numero - 1
            msg += str(fatorial)
            print(msg, ", 0")

        if numero % 2 == 0:
            valor = numero
            a, b = 0, 1
            while b < valor:
                print(b)
                a, b = b, a + b
