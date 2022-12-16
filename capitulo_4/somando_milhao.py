# Contando um milhão, Somando um milhão
milhão = []
for valor in range(0, 1000000):
    milhão.append(valor + 1)
print(min(milhão))
print(max(milhão))
print(sum(milhão))

milhões = [valor + 1 for valor in range(0, 1000000)]
print(min(milhões))
print(max(milhões))
print(sum(milhões))
