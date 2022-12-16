# Percorrendo todos os pares chave-valor com um laço
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages is {languages.title()}.")
print()

# Percorrendo todas as chaves de um dicionário com um laço
for name in favorite_languages.keys():
    print(name.title())
print()

# Percorrendo todas as chaves de um dicionário com um laço
friends = ['jen', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f'Hi {name.title()}, I see your '
              f'favorite languages is {favorite_languages[name].title()}!')
print()

# Percorrendo todas as chaves de um dicionário com um laço
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
print()

# Percorrendo as chaves de um dicionário em ordem usando um laço
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll.')

# Percorrendo todos os valores de um dicionário com um laço
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())
print()

# Percorrendo todos os valores de um dicionário com um laço set()
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
