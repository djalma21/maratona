num = int(input('Digite um numero que você deseja fatoriar:'))
msg = '*'
fatorial = 1

print(f"{num}!:", end="")
while num > 1:
    fatorial = fatorial * num
    num = num - 1

