# Números favoritos
favorite_numbers = {
    'lucas': [2, 6],
    'maria': [6, 7],
    'junior': [12, 2],
    'ana': [9],
    'jean': [8],
}
for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f'\nOs números favorito de {name.title()} são: ')
        for number in numbers:
            print(f'\t{number}')
    else:
        print(f'O número favorito de {name.title()} é {number}.')
