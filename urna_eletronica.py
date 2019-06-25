HULK = '11'
VIDEL = '88'
SEIYA = '12'
MESSI = '10'
CR7 = '07'

#Codigo de parada
SAIR = '00'

#Votos
votos_hulk = 0
votos_videl = 0
votos_seiya = 0
votos_messi = 0
votos_cr7 = 0
votos_nulos = 0
msg = 'pirulim \n Fim!'

while True:
    numero_candidato = input('Informe o numero do seu candidato:')
    if numero_candidato == HULK:
        votos_hulk += 1
    elif numero_candidato == VIDEL:
        votos_videl += 1
    elif numero_candidato == SEIYA:
        votos_seiya += 1
    elif numero_candidato == MESSI:
        votos_messi += 1
    elif numero_candidato == CR7:
        votos_cr7 += 1
    elif numero_candidato == SAIR:
        print(f'Hulk: {votos_hulk}')
        print(f'Videl:{votos_videl}')
        print(f'Seiya:{votos_seiya}')
        print(f'Messi:{votos_messi}')
        print(f'CR7:{votos_cr7}')
        print(f'Nulos:{votos_nulos}')
        print('Eleições encerradas!')
        break
    else:
        votos_nulos += 1
    print(msg)

