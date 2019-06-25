numero = int(input('Informe um número:'))
sucessor = numero + 1
antecessor = numero - 1

print('Sucessor:' ,sucessor)
print('Antecessor:',antecessor)
if antecessor % 2 == 0:
    print('Antecessor e o sucessor do número' ,numero,'é par')
else:
    print('Antecessor e o sucessor do número' ,numero,'é impar')
