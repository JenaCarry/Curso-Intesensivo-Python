# Ingredientes para uma pizza
# 1º Exemplo
ingredientes = ''
while ingredientes != 'quit':
    ingredientes = str(
        input('Quais ingredientes gostaria de adicionar a sua pizza: '))
    if ingredientes != 'quit':
        print(f'Acrescentaremos {ingredientes} à pizza.\n')
        print("Digite 'quit' para encerrar o programa.")

# 2º Exemplo
ativo = True
while ativo:
    ingredientes = str(
        input('Quais ingredientes gostaria de adicionar a sua pizza: '))
    if ingredientes == 'quit':
        ativo = False
    else:
        print(f'Acrescentaremos {ingredientes} à pizza.\n')
        print("Digite 'quit' para encerrar o programa.")

# 3º Exemplo
while True:
    ingredientes = str(
        input('Quais ingredientes gostaria de adicionar a sua pizza: '))
    if ingredientes == 'quit':
        break
    else:
        print(f'Acrescentaremos {ingredientes} à pizza.\n')
        print("Digite 'quit' para encerrar o programa.")
