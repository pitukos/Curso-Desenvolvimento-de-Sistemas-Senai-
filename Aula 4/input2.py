n1 = float(input('digite um numero'))
n2 = float(input('digite outro numero'))
simbolo = input('digite qual é a operção que você deseja [+,-,*,/] :')

if(simbolo == '+'):
    result = n1+n2
    print(f'a some é {result}')
elif(simbolo == '-'):
    result = n1+n2
    print(f'A subtração é {result}')
elif(simbolo == '*'):
    result = n1+n2
    print(f'A Multiplicação é {result}')
elif(simbolo == '/'):
    result = n1+n2
    print(f'A Divisão é {result}')
else:
    print(f'Operação invalida')
    
    