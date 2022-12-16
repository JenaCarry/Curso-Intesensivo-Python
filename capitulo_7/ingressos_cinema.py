# Ingressos para o cinema
while True:
    print("\nDigite 'quit' para sair.")
    idade = str(input('Qual a sua idade: '))
    if idade != 'quit':
        idade_int = int(idade)
        if idade_int <= 3:
            print('O ingresso é gratuito.')
        elif idade_int <= 12:
            print('O ingresso custá 10 dólares.')
        elif idade_int > 12:
            print('O ingresso custá 15 dólares.')
    elif idade == 'quit':
        break
