# Carros
def make_car(fabricante, modelo, **detalhes):
    ficha_tecnica = {}
    ficha_tecnica['fabricante'] = fabricante
    ficha_tecnica['modelo'] = modelo
    for chave, valor in detalhes.items():
        ficha_tecnica[chave] = valor
    return ficha_tecnica


car = make_car(
    'BMW',
    'Série 3 2022',
    cor='branco',
    potência=184,
    combustível='flex',
)
print(car)
