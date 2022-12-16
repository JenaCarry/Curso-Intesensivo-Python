import os
# Verificando nomes de usuários
usuários_atuais = [str(input(f'{valor}º nome de usuário: ')).strip().title()
                   for valor in range(1, 6)]
os.system('cls')
novos_usuários = [str(input(f'{valor}º nome de usuário: ')).strip().title()
                  for valor in range(1, 6)]
for novo_usuário in novos_usuários:
    if novo_usuário in usuários_atuais:
        print(f'Status: nome de usuário "{novo_usuário}" está indisponível!')
    else:
        print(f'Status: nome de usuário "{novo_usuário}" está disponível!')
