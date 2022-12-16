# Enquete
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jean': 'python',
    'lucas': 'java',
}
for name in favorite_languages.keys():
    print(f'Obrigado por responder a nossa enquete, {name.title()}.')
if 'pedro' not in favorite_languages.keys():
    print(f'\n{name.title()}, por favor, participe da nossa enquete!')
