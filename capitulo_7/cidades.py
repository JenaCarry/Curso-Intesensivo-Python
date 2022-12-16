# Cidades
# 1º Exemplo
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    cidade = str(input(prompt))
    if cidade == 'quit':
        break
    else:
        print(f"I'd love to go to {cidade.title()}!")

# 2º Exemplo
while True:
    cidade = str(input('Please enter the name of a city you have visited: '))  # noqa
    if cidade == 'quit':
        break
    else:
        print(f"I'd love to go to {cidade.title()}!\n")
        print("Enter 'quit' when you are finished.")
