# Um dicionário em um dicionário
# Muitos usuários
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'maire',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f'\nUsername: {username}.')
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print(f'\nFull name: {full_name.title()}.')
    print(f'\nLocation: {location.title()}.')  # user_info["location"]
