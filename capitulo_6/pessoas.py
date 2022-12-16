# Pessoas
pessoa_0 = {
    'nome': 'joão',
    'sobrenome': 'Vitor',
    'idade': 22,
    'cidade': 'Sorocaba'
}
pessoa_1 = {
    'nome': 'Lucas',
    'sobrenome': 'Silva',
    'idade': 18,
    'cidade': 'Votorantim',
}
pessoa_2 = {
    'nome': 'Ana',
    'sobrenome': 'Maria',
    'idade': 22,
    'cidade': 'Sorocaba'
}
pessoas = [pessoa_0, pessoa_1, pessoa_2]  # type: list
for info in pessoas:
    full_name = info['nome'] + ' ' + info['sobrenome']
    idade = info['idade']
    cidade = info['cidade']
    print(f'\nMeu nome é {full_name} tenho {idade} anos e moro em {cidade}.')
