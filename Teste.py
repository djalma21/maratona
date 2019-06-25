numero_entregas = int(input('Informe o número de entregas do gerente:'))
salario_gerentes = 8000.00 + ((numero_entregas/4)*20)
print('O salário do gerente é:',salario_gerentes)

numero_entregas2 = int(input('Informe o número de entregas Scrum Master:'))
salario_sm = 7000.00 + ((numero_entregas2/3.5)*15)
print('O salário Scrum Master é:',salario_sm)

numero_entregas3 = int(input('Informe o número de entregas do desenvolvedor junior:'))
salario_dev_junior = 3000.00 + (numero_entregas3 * 20)
print('O salário do desenvolvedor junior é:',salario_dev_junior)

numero_entregas4 = int(input('Informe o número de entregas do desenvolvedor pleno:'))
salario_dev_pleno = 5000.00 + ((numero_entregas4 / 2)* 50)
print('O salário do desenvolvedor pleno é:',salario_dev_pleno)

numero_entregas5 = int(input('Informe o número de entregas do desenvolvedor sênior:'))
salario_dev_senior = 7000.00 + ((numero_entregas5 / 3)*50)
print('O salário do desenvolvedor sênior é:',salario_dev_senior)