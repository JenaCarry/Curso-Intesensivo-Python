# Álbum, Álbuns dos usuários
def make_album(artist_name, album_title, tracks_number=''):
    '''Exibe o nome do artista e o título de um álbum.'''
    describe_album = {'Nome do artista:': artist_name, 'Título do álbum:': album_title}  # noqa
    if tracks_number:
        describe_album['Número de faixas do álbum:'] = tracks_number
    return describe_album


while True:
    print('\n(digite \'q\' para sair)')
    nome = str(input('Nome de um Artista: ')).title()
    if nome == 'Q':
        break
    album = str(input('Título de um Álbum: ')).title()
    if album == 'Q':
        break
    faixa = str(input('Deseja adicionar número de faixas do álbum? [S/N] ')).upper()[0]  # noqa
    if faixa == 'S':
        numeros = int(input('Número de faixas do álbum: '))
        dados = make_album(nome, album, numeros)
    else:
        dados = make_album(nome, album)
    print(dados)
