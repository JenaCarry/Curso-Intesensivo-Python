# Lanchonete, Sem pastrami
sandwich_orders = [
    'pastrami',
    'atum',
    'linguiça',
    'pernil',
    'pastrami',
    'frango',
    'pastrami',
]
print("Estamos sem 'pastrami' no momento.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []  # type: list
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f'Preparei seu sanduíche de {current_order}.')
    finished_sandwiches.append(current_order)
print('\nSanduíches finalizados: ')
for completed_order in finished_sandwiches:
    print(f'{completed_order}.')
