#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#entre 3 e 4 como "Cúmplice"
#e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".

pergunta1 = input('Telefonou para a vítima?')
pergunta2 = input('Esteve no local do crime?')
pergunta3 = input('Mora perto da vítima?')
pergunta4 = input('Devia para a vítima?')
pergunta5 = input('Já trabalhou para a vítima?')
crime = "sim"
resultado = 0

if pergunta1 == crime:
    resultado = resultado + 1
crime = "sim"
if pergunta2 == crime:
    resultado = resultado + 1
crime = "sim"
if pergunta3 == crime:
    resultado = resultado + 1
crime = "sim"
if pergunta4 == crime:
    resultado = resultado + 1
crime = "sim"
if pergunta5 == crime:
    resultado = resultado + 1
crime = "sim"
if resultado == 0 and 1:
    print('Inocente')
if resultado == 2:
    print('Suspeita')
if resultado == 3 and 4:
    print('Cúmplice')
if resultado == 5:
    print('Assassino')
