din = int(input('Digite o valor do dinheiro:'))
print ('o valor que será deconposto é R$',din)
cn100 = 0
cn50 = 0
cn20 = 0
cn10 = 0
cn05 = 0
cn02 = 0
cn01 = 0

while din >= 100:
    cn100 = cn100 + 1
    din = din - 100
while din >= 50:
    cn50 = cn50 + 1
    din = din - 50
while din >= 20:
    cn20 = cn20 + 1
    din = din - 20
while din >= 10:
    cn10 = cn10 + 1
    din = din - 10
while din >= 5:
    cn05 = cn05 + 1
    din = din - 5
while din >= 2:
    cn02 = cn02 + 1
    din = din - 1
while din >= 1:
    cn01 = cn01 + 1
    din = din - 1
print('A quantidade de notas de 100 é:',cn100,',de 50 é:',cn50,',de 20 é:',cn20,',de 10 é:',cn10,',de 5 é:',cn05,',de 2 é:',cn02,',de 1 é:',cn01)
print ('Fatorado com sucesso!')