def build_profile(nome, sobrenome, **user_info):
    '''Constrói um dicionário contendo tudo que sabemos sobre um usuário.'''
    perfil = {}
    perfil['nome'] = nome
    perfil['sobrenome'] = sobrenome
    for chave, valor in user_info.items():
        perfil[chave] = valor
    return perfil


perfil_usuario = build_profile(
    'jean',
    'dias',
    idade=18,
    cidade='sorocaba',
)
print(perfil_usuario)
