# Escrevendo prompts claros
name = input('Please enter your name: ')
print(f'Hello, {name}!')

# Se você nos disser quem você é, podemos personalizar as mensagens que você vê
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? '
name = input(prompt)
print(f'\nHello, {name}!')
