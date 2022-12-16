# Preenchendo um dicionário com dados de entrada do usuário
responses = {}  # type: dict
# Define uma flag para indicar que a enquete está ativa
polling_active = True
while polling_active:
    # Pede o nome da pessoa e a resposta
    name = str(input('\nWhat is your name? '))  # .title()
    response = str(input('Which mountain would you like to climb someday? '))
    # Armazena a resposta no dicionário
    responses[name] = response
    # Descobre se outra pessoa vai responder à enquete
    repeat = str(
        input('Would you like to let another person respond? (yes/no): '))
    if repeat.lower() == 'no':
        polling_active = False
# A enquete foi concluída, e mostra os resultados
print('\n---Poll Results---')
for name, response in responses.items():
    print(f'{name.title()} would like to climb {response.title()}.')
