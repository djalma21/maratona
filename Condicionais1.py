email = 'thegodman@yopmail.com'
senha = 'dmenor1533'

email_informado = input('Informe seu e-mail:')
senha_informada = input('Informe sua senha:')

if (email_informado == email and senha_informada == senha):
    print('Seja bem-vindo',email)
else:
    print('Email ou senha incorretos, por favor verificar!')
