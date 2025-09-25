import random
import os

numerosecreto = random.randint(0,100)


while True:
    palpite = int(input('digite um numero entre 0 e 100: '))
    os.system ('cls')

    if(palpite==numerosecreto):
        print('parabens você acertou o numero {numerosecreto}')
        break
    elif(palpite<numerosecreto):
        result = numerosecreto
        print('o numero é menor')
    elif(palpite>numerosecreto):
        result = numerosecreto
        print('O numero secreto é maior')
    else:
        print(f'comando invalido')