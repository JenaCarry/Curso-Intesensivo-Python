# Números ordinais
números = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for número in números:
    if número == 1:
        print(f'{número}st.')
    elif número == 2:
        print(f'{número}nd.')
    elif número == 3:
        print(f'{número}rd.')
    else:
        print(f'{número}th.')
