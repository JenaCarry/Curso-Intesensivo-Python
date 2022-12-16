# Passando um número arbitrário de argumentos
# O * no nome do parâmetro *toppings diz a Python para criar uma tupla vazia
def make_pizza(*toppings):
    '''Apresenta a pizza que estamos prestes a preparar.'''
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print(f'- {topping}.')


make_pizza('pepperoni')

make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Misturando argumentos posicionais e arbitrários
# O parâmetro que aceita um número arbitrário de argumentos deve ser colocado por último # noqa
def make_pizza2(size, *toppings):
    '''Apresenta a pizza que estamos prestes a preparar.'''
    print(f'\nMaking a {size}-inch pizza with the following toppings: ')
    for topping in toppings:
        print(f'- {topping}.')


make_pizza2(16, 'pepperoni')

make_pizza2(12, 'mushrooms', 'green peppers', 'extra cheese')
