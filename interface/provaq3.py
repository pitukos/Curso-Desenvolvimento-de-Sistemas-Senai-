casa = int(input(f'Digite o valor da casa que deseja comprar : '))
salario = int(input(f'Dogite seu salario seu pobre: '))
anos = int(input(f'Digite em qauntos anos você vai pagar a divida seu otareo: '))

qntprestacao=anos*12
prestacao=casa/qntprestacao

if(prestacao>salario*0.3):
    print('Você não vai conseguir o emprestimo porquê você é muito pobre mano')
else:
    print(f'parabens o emprestimo foi aprovado em {qntprestacao} prestaçoes de R${prestacao:.2f}')