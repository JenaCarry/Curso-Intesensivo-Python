# Alterando a lista de convidados
convidados = ['Jean', 'Lucas', 'Pedro']
print(f'{convidados[0].title()}, Gostaria de sair para jantar?')
print(f'{convidados[1].title()}, Gostaria de sair para jantar?')
print(f'{convidados[2].title()}, Gostaria de sair para jantar?')
print(f'\nO {convidados[2].title()} não poderá comparecer a esse jantar.\n')
convidados[2] = 'Matheus'
print(f'{convidados[0].title()}, Gostaria de sair para jantar?')
print(f'{convidados[1].title()}, Gostaria de sair para jantar?')
print(f'{convidados[2].title()}, Gostaria de sair para jantar?')
