def calcpreço(x):
    if(distancia <= 200):
        preço=distancia*0.5
    else:
        preço=distancia*0.45
    return preço



distancia = int(input(f'Digite a distancia que você deseja percorrer em KM: '))

preço=calcpreço(distancia)

print(f'O valor da passagem é de R${preço}')

