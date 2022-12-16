# Saudações
# Definindo uma função
def greet_user():
    '''Exibe uma saudação simples.'''  # docstring - Descreve o que a função faz # noqa
    print('Hello!')


greet_user()


# Passando informações para uma função
def greet_user2(username):
    '''Exibe uma saudação simples.'''
    print(f'Hello, {username.title()}!')


greet_user2('jean')
