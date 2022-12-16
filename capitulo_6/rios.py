# Rios
rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'yangtze': 'china',
}
for rio, pais in rios.items():
    print(f'O rio {rio.title()} corre pelo {pais.title()}.')
print()

for rio in rios.keys():
    print(rio.title())
print()

for pais in rios.values():
    print(pais.title())
