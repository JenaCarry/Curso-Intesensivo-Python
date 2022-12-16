# Papagaio
# 1º Exemplo
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "
mensagem = ''
while mensagem != 'quit':
    mensagem = str(input(prompt))
    if mensagem != 'quit':
        print(mensagem)

# 2º Exemplo
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "
mensagem = ''
ativo = True
while ativo:
    mensagem = str(input(prompt))
    if mensagem == 'quit':
        ativo = False
    else:
        print(mensagem)

# 3º Exemplo
ativo = True
while ativo:
    mensagem = str(input('Tell me something, and I will repeat it back to you: '))  # noqa
    if mensagem == 'quit':
        ativo = False
    else:
        print("\nEnter 'quit' to end the program.")
