velocidade = int(input(f'digite a velocidade ultrapassada aqui!! '))
 
multa = (velocidade-80)*5

if(velocidade<=80):
    print('você esta na media de velocidade permitida')
else:
    print(f'você ultrapassou o limite de velocidade você será multado no valor de R${multa:.2f}') 