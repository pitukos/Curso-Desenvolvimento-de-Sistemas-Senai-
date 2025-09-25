import random
def sorteio(M):
    sortudo = random.choice(M)
    print(f'a pessoa sortuda é : {sortudo}')


pessoas = []

for x in range(5):
    nome = input(f'Digite o {x+1}º nome')
    pessoas.append(nome)

sorteio(pessoas)