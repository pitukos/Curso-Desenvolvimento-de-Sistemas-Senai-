#----------------- função-------------------------
def calmedia(u1,u2,u3):
    media = (u1+u2+u3)/3
    return media

def result(x):
    
    if(x>=7):
        print(f'Você passou com ({x:.1f}) ')
    elif(x>=5 and x<=6.9):
        print(f'você foi de recu recu com ({x:.1f}):D ')
    else:
        print('Você perdeu de ano otareo com ({x:.1f}) ')
#----------------- função-------------------------

u1 = float(input('Digite a sua nota aqui: '))
u2 = float(input('Digite a sua nota aqui: '))
u3 = float(input('Digite a sua nota aqui: '))

media = calmedia(u1,u2,u3)

result(media)