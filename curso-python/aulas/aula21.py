'''

and = e (todas as condições precisam ser verdadeiras).
or = ou
not = não

Se qualquer valor for considerado falso, a expressão inteira
será avaliada naquele valor.

São considerados falsy: 0, 0.0, '', False

Também existe o tipo None que é usado para representar um não valor.

'''
entrada = input('[E]entrar [S]air: ')
senha_permitida = '123'
senha = input('Digite sua senha: ')

if entrada == 'E' and senha == senha_permitida:
    print('Você entrou no sistema!')

else:
    print('Você saiu do sistema.')


# Avaliação de curto circuito

print(True and True) # O retorno será como True.
print(True and False) # O retorno será como False.
print(bool('')) # O retorno será como False pois é uma string vazia.
print(bool(' ')) # O retorno será como True pois é uma string coom um valor.
