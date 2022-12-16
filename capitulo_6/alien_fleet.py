# Cria uma lista vazia para armazenar alienígenas
aliens = []
# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Modifica os três primeiros itens de verde para amarelo
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
# Mostra os 5 primeiros alienígenas
for alien in aliens[:5]:
    print(alien)
print('...')
# Mostra quantos alienígenas foram criados
print(f'Total number of aliens: {str(len(aliens))}')  # str opcional
