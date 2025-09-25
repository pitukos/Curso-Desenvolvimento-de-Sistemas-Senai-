import os

def nota(media):
    media = 7
    notas = []

for x in range(3):
    nota = float(input('digite sua nota aqui: '))
    if (nota>=7):
        print(f'você passou com a media :{nota:.1f} ')
    else:
        print(f'você perdeu com a media :{nota:.1f} ')
os.system('cls')