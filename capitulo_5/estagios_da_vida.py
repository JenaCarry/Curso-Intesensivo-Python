# Estágios da vida
idade = int(input('Qual a sua idade: '))
if idade <= 2:
    print(f'Você tem apenas {idade} anos, ainda é um bebê.')
elif idade <= 4:
    print(f'Você tem {idade} anos, ainda é uma criança.')
elif idade <= 13:
    print(f'Você tem {idade} anos, já é um(a) garoto(a).')
elif idade <= 20:
    print(f'Você tem {idade} anos, já é um(a) adolescente.')
elif idade <= 65:
    print(f'Você tem {idade} anos, já é um adulto.')
else:
    print(f'Você tem {idade} anos, já é um idoso.')
