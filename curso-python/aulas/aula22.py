# or = Se qualquer condição for considerada verdadeira, 
# a impressão inteira será considerada naquele valor.

entrada = input('Digite aqui: ')

if entrada == 'E' or entrada == 'e':
    print('Sucesso!')
else:
    print('Derrota!')

# Avaliação de curto circuito
print(0 or False or 0 or 'Valor verdadeiro!' or True)

dado_valioso = input("Tentativa1... ") or input('Tentativa2...')
print(f'{dado_valioso}')