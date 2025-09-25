#crie um algoritimo que recebe 3 numeros 
#e imrpime o maior deles
import os
n1 = int(input(f'Digite um numero aqui'))
n2 = int(input(f'Digite um numero aqui'))
n3 = int(input(f'Digite um numero aqui'))

os.system('cls')

if (n1>n2 and n1>n3):
    print('numero 1 é maior !!')
elif (n2>n1 and n2>n3):
    print('numero 2 é maior !!')
elif (n3>n2 and n3>n1):
    print('numero 3 é maior !!')
else:
    print(' existem numeros iguais')
