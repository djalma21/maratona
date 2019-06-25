#Somar os números primos de 1 a 100

numero = 1
soma = 0
divisores = 0

while numero <= 10:
    anterior = numero
    divisores = 0
    while anterior > 0:
        if numero % anterior == 0:
            divisores + 1
        anterior -= 1
print(divisores)