# Cidades
def describe_city(city, country='brasil'):
    '''Exibe uma frase simples.'''
    print(f'{city.title()} está localizada no(na) {country.title()}.')


describe_city(city='paris', country='frança')
describe_city('são paulo')
describe_city('rio de janeiro')
