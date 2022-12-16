# Múltiplos de três
múltiplos = [valor * 3 for valor in range(1, 11)]
print(múltiplos, end=' \n')

múltiplos1 = []
for valor in range(1, 11):
    múltiplos1.append(valor * 3)
print(múltiplos1, end=' \n')

múltiplos2 = []
for valor in range(3, 31, 3):
    múltiplos2.append(valor)
print(múltiplos2, end=' \n')
