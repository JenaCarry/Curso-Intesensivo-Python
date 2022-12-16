# Mágicos, Grandes mágicos, Mágicos inalterados
def show_magicians(magicians):
    '''Exibe o nome de cada mágico na lista.'''
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    '''Adiciona a expressão "o Grande" ao nome de cada mágico.'''
    for magician in magicians:
        print(f'o Grande {magician.title()}.')


magicians = ['howard thurston', 'david copperfield', 'lace burton']
show_magicians(magicians)
print()

make_great(magicians[:])
