# Transferindo itens de uma lista para outra
# Começa com os usuários que precisam ser verificados
unconfirmed_users = ['alice', 'brian', 'candace']
# E com uma lista vazia para armazenar os usuários confirmados
confirmed_users = []  # type: list
# Verifica cada usuário até que não haja mais usuários não confirmados
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user {current_user.title()}.')
# Transfere cada usuário verificado para a lista de usuários confirmados
    confirmed_users.append(current_user)
# Exibe todos os usuários confirmados
print('The following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
