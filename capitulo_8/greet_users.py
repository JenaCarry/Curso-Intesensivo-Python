# Saudar usuários
def greet_users(names):
    '''Exibe uma saudação simples a cada usuário na lista.'''
    for name in names:
        print(f'Hello {name.title()}!')


username = ['hannah', 'ty', 'margot']
greet_users(username)
