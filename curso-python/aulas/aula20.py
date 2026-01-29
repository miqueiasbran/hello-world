primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor}).')
elif primeiro_valor == segundo_valor:
    print(f'Os dois valores são iguais.')
else:
    print(f'O segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor}).')