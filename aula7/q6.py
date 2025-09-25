import random
import os

alunos = []

while True: 
    nome = input('Digite o nome do aluno: ')
    os.system('cls')
    if(nome == 'sair'):
        break
    else:
        alunos.append(nome)
        
sortudo = random.choice(alunos)

print(f'o ganhador do mouse pad foi o {sortudo}')