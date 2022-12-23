estados_brasil = ['Tocantins',
                  'Minas Gerais',
                  'Distrito Federal',
                  'São Paulo',
                  'Rio de Janeiro',
                  'Alagoas',
                  'Rondônia',
                  'Bahia',
                  'Acre',
                  'Ceara',
                  'Mato Grosso do Sul',
                  'Pará',
                  'Santa Catarina',
                  'Paraná',
                  'Mato Grosso',
                  'Sergipe',
                  'Amazonas',
                  'Pernambuco',
                  'Rio Grande do Norte',
                  'Rondônia',
                  'Maranhão',
                  'Goiás',
                  'Amapá',
                  'Paraíba',
                  'Espírito Santo',
                  'Rio Grande do Sul',
                  'Nada']
print(estados_brasil)
del estados_brasil[-1]
estados_brasil.append('Piauí')
print(f'\nEu já visitei o estado do {estados_brasil[13].title()}.\n')

print(f'Ordem alfabética {sorted(estados_brasil)}\n')
print(f'Ordem alfabética inversa {sorted(estados_brasil, reverse=True)}\n')

estados_brasil.reverse()
print(f'Invertido {estados_brasil}\n')
estados_brasil.reverse()
print(f'Ordem original {estados_brasil}\n')

estados_brasil.sort(reverse=True)
print(f'Ordem alfabética inversa {estados_brasil}\n')

estados_brasil.sort()
print(f'Ordem alfabética {estados_brasil}\n')

print(f'{estados_brasil[-2]} tem ao todo {len(estados_brasil[-2].replace(" ", ""))} letras.')  # noqa
