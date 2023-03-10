# Conhecendo o Mundo
lugares = ['Japão', 'Espanha', 'Coreia do Sul', 'Eua', 'Antártida']
print(f'Normal {lugares}\n')

print(f'Ordem alfabética {sorted(lugares)}\n')
print(f'Normal {lugares}\n')

print(f'Ordem alfabética inversa {sorted(lugares, reverse=True)}\n')
print(f'Normal {lugares}\n')

lugares.reverse()
print(f'Ordem invertida {lugares}\n')
lugares.reverse()
print(f'Ordem invertida para normal {lugares}\n')

lugares.sort()
print(f'Ordem alfabética permanente {lugares}\n')

lugares.sort(reverse=True)
print(f'Ordem alfabética inversa permanente {lugares}\n')
