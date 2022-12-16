# Animais de estimação
cachorro = {'animal': 'cachorro', 'dono': 'lucas', 'nome': 'bob'}
gato = {'animal': 'gato', 'dono': 'pedro', 'nome': 'frajola'}
passaro = {'animal': 'pássaro', 'dono': 'ana', 'nome': 'mike'}
pets = [cachorro, gato, passaro]
for pet in pets:
    print(f'{pet["dono"].title()} tem um {pet["animal"].title()}.')
    print(f'O nome dele é {pet["nome"].title()} e é um amorzinho.\n')
