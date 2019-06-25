nome = input('Informe seu nome:')
data_nascimento = int(input('Informe sua data de nascimento:'))
idade_maior = 18
ano_atual = 2019
resultado = data_nascimento - ano_atual
if resultado <= idade_maior:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')