# Olá admin,  Sem usuários
usuários = ['Jean', 'Lucas', 'Admin', 'Ana', 'Maria']  # type: list[str]
if usuários:
    for usuário in usuários:
        if usuário == 'Admin':
            print(
                f'\nOlá {usuário}, gostaria de ver um relatório de status?\n')
        else:
            print(f'Olá {usuário}, obrigado por fazer login novamente.')
else:
    print('Precisamos encontrar novos usuários!')
