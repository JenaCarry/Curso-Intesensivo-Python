# Mais convidados
convidados = ['Jean', 'Lucas', 'Pedro']
print(f'Temos {len(convidados)} convidados confirmados.')
print(f'{convidados[0].title()}, Gostaria de sair para jantar?')
print(f'{convidados[1].title()}, Gostaria de sair para jantar?')
print(f'{convidados[2].title()}, Gostaria de sair para jantar?')

print('\nEncontramos uma mesa de jantar maior!\n')
convidados.insert(0, 'Isabella')
convidados.insert(2, 'Luan')
convidados.append('Geovana')
print(f'Temos {len(convidados)} convidados confirmados.')

print(f'\n{convidados[0].title()}, Gostaria de sair para jantar?')
print(f'{convidados[1].title()}, Gostaria de sair para jantar?')
print(f'{convidados[2].title()}, Gostaria de sair para jantar?')
print(f'{convidados[3].title()}, Gostaria de sair para jantar?')
print(f'{convidados[4].title()}, Gostaria de sair para jantar?')
