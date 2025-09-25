#crie um algoritimo que solicita 3 numeros e exibe a
#soma desses 3 numeros
import time
import os

numero1= int(input(f'Digite o numero 1: '))
numero2= int(input(f'Digite o numero 2: '))
numero3= int(input(f'Digite o numero 3: '))

soma = numero1+numero2+numero3

print('Calculando...')
time.sleep(2)
os.system('cls')
print(f'a soma dos numeros é {soma}')
