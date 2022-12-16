# Testes condicionais
carros = ['audi', 'bmw']
print("Is cars == 'audi'? I predict True.")
print(carros[0] == 'audi')
print("\nIs cars == 'gtr'? I predict False.")
print(carros == 'gtr')
print("\nIs 'bmw'in cars? I predict True")
print('bmw' in carros)

nome = 'JEAN'
print('\nSeu nome é Jean?', nome.lower() == 'jean')

a = 8
b = 4
print('a é maior igual a b?', a >= b)
print('b é maior igual a a?', b >= a)
print('\n"a" e "b" é menor igual a 6?', a <= 6 and b <= 6)
print('"a" e "b" é maior igual a 6?', a >= 6 and b >= 6)
print('"a" ou "b" é maior igual a 6?', a >= 6 or b >= 6)
