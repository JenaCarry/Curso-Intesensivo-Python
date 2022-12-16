# Minhas pizzas, suas pizzas
minhas_pizzas = ['Frango com catupiry', 'Portuguesa', 'Calabresa']
pizzas_amigo = minhas_pizzas[:]
pizzas_amigo.append('Margherita')
pizzas_amigo.append('Brigadeiro')
print('Minhas pizzas favoritas são: ')
for minha_pizza in minhas_pizzas:
    print(minha_pizza)
print('\nAs pizzas favoritas de meu amigo são: ')
for pizza_amigo in pizzas_amigo:
    print(pizza_amigo)
