positivo = []
negativo = []

for x in range(10):
    numero = int(input('digite o valor (+ ou -): '))
    if(numero>=0):
        positivo.append(numero)
    else:
        negativo.apend(numero)
        
print(f'A quantidade de positivos é {len(positivo)}')
print(f'A quantidade de negativos é {len(negativo)}')
print(f'A soma dos positivos é {sum(positivo)}')