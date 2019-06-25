#Crie um programa que receba 3 números do usuario
#e exiba-os em ordem crescente e decrescente

num1 = int(input('Informe um número: '))
num2 = int(input('Informe um número: '))
num3 = int(input('Informe um número: '))

if num1 > num2 > num3:
    print('Ordem decrescente é:' ,num1,',',num2,',',num3)
elif num1 > num3 > num2:
    print('Ordem decrescente é:' ,num1,',',num3,',',num2)
elif num2 > num1 > num3:
    print('Ordem decrescente é:' ,num2,',',num1,',',num3)
elif num2 > num3 > num1:
    print('Ordem decrescente é:' ,num2,',',num3,',',num1)
elif num3 > num2 > num1:
    print('Ordem decrescente é:' ,num3,',',num2,',',num1)
elif num3 > num1 > num2:
    print('Ordem decrescente é:' ,num3,',',num1,',',num2)

if num1 < num2 < num3:
    print('Ordem crescente é:' ,num1, ',',num2,',',num3)
elif num1 < num3 < num2:
    print('Ordem crescente é:' ,num1, ',',num3,',',num2)
elif num2 < num1 < num3:
    print('Ordem crescente é:' ,num2, ',',num1,',',num3)
elif num2 < num3 < num1:
    print('Ordem crescente é:' ,num2, ',',num3,',',num1)
elif num3 < num2 < num1:
    print('Ordem crescente é:' ,num3, ',',num2,',',num1)
elif num3 < num1 < num2:
    print('Ordem crescente é:' ,num3, ',',num1,',',num2)