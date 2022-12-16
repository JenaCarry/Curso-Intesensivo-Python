# Modelos de impressão
# 1º Exemplo
# Começa com alguns designs que devem ser impressos
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simula a impressão de cada design, até que não haja mais nenhum
while unprinted_designs:
    # Transfere cada design para completed_models após a impressão
    current_design = unprinted_designs.pop()
    # Simula a criação de uma impressão 3D a partir do design
    print(f'Printing model: {current_design}.')
    completed_models.append(current_design)
# Exibe todos os modelos finalizados
print('\nThe following models have been printed: ')
for completed_model in completed_models:
    print(completed_model)


# 2º Exemplo
def print_models(unprinted_designs, completed_designs):
    '''Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simula a criação de uma impressão 3D a partir do design
        print(f'Printing model: {current_design}.')
        completed_designs.append(current_design)


def show_completed_models(completed_models):
    '''Mostra todos os modelos impressos.'''
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# Evitando que uma função modifique uma lista
# nome_da_função(nome_da_lista[:])
# print_models(unprinted_designs[:],completed_models)
