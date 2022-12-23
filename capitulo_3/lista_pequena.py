# Reduzindo a lista de convidado
convidados = ['Jean', 'Lucas', 'Pedro']
print(f'Temos {len(convidados)} convidados confirmados.')
print(f'\n{convidados[0].title()}, Gostaria de sair para jantar?')
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
print(f'{convidados[4].title()}, Gostaria de sair para jantar?\n')
print(f'Temos {len(convidados)} convidados confirmados.')

print('\nInfelizmente a mesa está alugada, e só poderei convidar 2 pessoas.\n')
print(f'Sinto muito por não poder convida-lá {convidados.pop(0)}')
print(f'Sinto muito por não poder convida-lo {convidados.pop(1)}')
print(f'Sinto muito por não poder convida-lo {convidados.pop(2)}')
print(f'Sinto muito por não poder convida-lá {convidados.pop(2)}\n')
print(f'Temos apenas {len(convidados)} convidados confirmados.')

print(f'\nVocê ainda está convidada ao jantar de hoje, {convidados[0]}.')
print(f'Você ainda está convidada ao jantar de hoje, {convidados[1]}.')

del convidados[0]
del convidados[0]
print(f'Jantar cancelado: {len(convidados)} nenhum convidado confirmado.')
