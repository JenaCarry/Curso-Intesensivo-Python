# Sanduíches
def make_sandwich(*toppings):
    '''Apresenta o sanduíche que estamos prestes a preparar. '''
    print('\nFazendo um sanduíche com os seguintes recheios: ')
    for topping in toppings:
        print(f'- {topping}.')


make_sandwich('presunto', 'queijo')

make_sandwich('hamburger', 'cheddar', 'picles')

make_sandwich('presunto', 'queijo', 'tomate')
