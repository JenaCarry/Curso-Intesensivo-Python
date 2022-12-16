# Nomes de cidade
def city_country(city, country):
    '''Exibe o nome da cidade e país.'''
    formatted_string = f'{city}, {country}'
    return formatted_string.title()


while True:
    print('\n(digite \'q\' para sair)')
    cidade = str(input('Nome da sua cidade: '))
    if cidade == 'q':
        break
    pais = str(input('Nome do seu país: '))
    if pais == 'q':
        break
    cidade_pais = city_country(cidade, pais)
    print(f'\n{cidade_pais}')
