nome = 'Miquéias B.'
peso = 115
altura = 1.69
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'seu peso é de {peso}'
linha_3 = f'IMC: {imc:.2f}'

print(linha_1, linha_2, linha_3, sep='\n')