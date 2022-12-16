# Férias dos sonhos
enquete = {}
ativo = True
while ativo:
    nome = str(input('Qual o seu nome? '))
    lugar = str(
        input('Se pudesse visitar um lugar do mundo, para onde você iria? '))
    enquete[nome] = lugar
    repetir = str(
        input('Você gostaria de deixar outra pessoa responder? (S/N): ')).upper()[0]  # noqa
    if repetir == 'N':
        ativo = False
print('\n{:-^30}'.format('Resultados da Enquete'))
for nome, lugar in enquete.items():
    print(
        f'Me chamo {nome.title()} e gostaria de visitar o(a) {lugar.title()}.')
