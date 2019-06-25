num1 = int(input('Digite um número: '))
operador = int(input('Digite um operador. (Ex: 1:+  2:-  3:*  4:/ ) '))

cont = 0

while cont <= 10:
    if operador == 1:
        print(num1, '+',cont , '=', num1 + cont)

    if operador == 2:
        print(num1, '-', cont, '=', num1 - cont)

    if operador == 3:
        print(num1, '*', cont, '=', num1 * cont)

    if operador == 4:
        print(num1, '/', cont, '=', num1 / cont)

    cont += 1