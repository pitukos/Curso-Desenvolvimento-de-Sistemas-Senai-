import random
import os

os.system('cls')

numerosecreto = random.randint(0,100)

tentativas = 0

while True:
    palpite = int(input('digite um numero entre 0 e 100: '))
    os.system ('cls')
    tentativas = tentativas + 1 
    if palpite == numerosecreto:
        print(f'parabens você acertou o numero {numerosecreto}, em {tentativas} tentativas')
        break
    elif palpite < numerosecreto:
        print('O numero secreto é maior')
    elif palpite > numerosecreto:
        print('o numero é menor')
    else:
        print(f'comando invalido')