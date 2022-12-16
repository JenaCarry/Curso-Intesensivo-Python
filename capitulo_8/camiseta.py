# Camiseta, Camisetas grandes
def make_shirt(shirt_size='g', message='eu amo python'):
    '''Exibe o tamanho e uma mensagem na camiseta.'''
    print(f'A camiseta tem o tamanho "{shirt_size.title()}" '
          f'e a mensagem estampada é "{message.title()}".')


# Argumentos posicionais
make_shirt('m', 'fúria')
# Argumentos nomeados
make_shirt(shirt_size='m', message='fúria')
# Argumentos default
make_shirt()
make_shirt('m')
make_shirt(message='navi')
