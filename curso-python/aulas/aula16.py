# if / elif / else
# se / se não se / se não

entrada = ' '
while entrada != 'entrar' or 'sair':
    print('Você quer entrar ou sair? ')
    print()
    entrada = input('Digite seu resposta: "entrar ou sair"')

    if entrada == 'entrar':
        print('LIBERADO!')
    elif entrada == 'sair':
        print('ATÉ LOGO!')
    else:
        print('Digite uma opção válida!')
