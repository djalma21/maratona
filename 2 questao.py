nome = input('Informe seu nome:')
salario_vendedor = float(input('Informe seu salário:'))
salario_minimo = 998.0
diferenca_salarial = salario_vendedor - salario_minimo
percentual_salario = (diferenca_salarial * 100) / salario_minimo

if diferenca_salarial > 0:
    print('O seu salário está:',percentual_salario,'% acima do salário mínimo')
elif salario_vendedor == salario_minimo:
    print('Você rebece um salário mínimo')
else:
    print('O seu salário esta:',percentual_salario, '% abaixo do salário mínimo')
