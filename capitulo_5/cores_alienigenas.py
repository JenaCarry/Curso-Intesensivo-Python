# Cores de alienígenas 1
cor_alienígena1 = 'verde'
if cor_alienígena1 == 'amarelo':
    print('Você não ganhou nenhum ponto.\n')
elif cor_alienígena1 == 'verde':
    print('Você acabou de ganhar 5 pontos.\n')

# Cores de alienígenas 2
cor_alienígena2 = 'amarelo'
if cor_alienígena2 == 'verde':
    print('Você ganhou 5 pontos por atingir o alienígena.\n')
else:
    print('Você ganhou 10 pontos.\n')

# Cores de alienígenas 3
cor_alienígena3 = 'vermelho'
if cor_alienígena3 == 'verde':
    print('Você ganhou 5 pontos por atingir o alienígena.\n')
elif cor_alienígena3 == 'amarelo':
    print('Você ganhou 10 pontos.\n')
else:
    print('Você ganhou 15 pontos por atingir o alien vermelho.\n')
