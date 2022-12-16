# Cidades
cidades = {
    'sorocaba': {
        'pais': 'brasil',
        'habitantes': '659.000',
        'fato': 'Um lugar lindo e cheio de histórias',
    },
    'votorantim': {
        'pais': 'brasil',
        'habitantes': '123.599',
        'fato': 'A fabricação de cimento é a principal fonte de renda da cidade',  # noqa
    },
    'itu': {
        'pais': 'brasil',
        'habitantes': '163.882',
        'fato': 'A cidade dos exageros',
    },
}
for cidade, info in cidades.items():
    pais = info['pais']
    hab = info['habitantes']
    fato = info['fato']
    print(f'A cidade de {cidade.title()}, localizada no {pais.title()}'
          f'conta com {hab} habitantes.'
          f'\nE um dos fatos dessa cidade é:\n{fato}!\n')
