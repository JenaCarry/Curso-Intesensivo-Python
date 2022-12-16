# Argumentos posicionais - Devemos fornecer o tipo do argumento, nessa ordem.
def describe_pets(animal_type, pet_name):
    '''Exibe informações sobre um animal de estimação.'''
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")


# A ordem é importante em argumentos posicionai
describe_pets('hamster', 'harry')
# Várias chamadas defunção
describe_pets('dog', 'willie')

# Argumentos nomeados
describe_pets(animal_type='hamster', pet_name='harry')

# Valores default
# Pode ser especificado por meio do formato posicional ou nomeado


def describe_pets2(pet_name, animal_type='dog'):
    '''Exibe informações sobre um animal de estimação.'''
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")


describe_pets2('willie')
describe_pets2(pet_name='willie')
