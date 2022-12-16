# Devolvendo um valor simples
def get_formatted_name(first_name, last_name):
    '''Devolve um nome completo formatado de modo elegante.'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()


'''Quando chamamos uma função que devolve um valor, precisamos
fornecer uma variável em que o valor de retorno possa ser armazenado.'''
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Deixando um argumento opcional
def get_formatted_name2(first_name, last_name, middle_name=''):
    '''Devolve um nome completo formatado de modo elegante.'''
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name


musician = get_formatted_name2('jimi', 'hendrix')
print(musician)
musician = get_formatted_name2('john', 'hooker', 'lee')
print(musician)
