# Márcio Davi Almeida da Conceição


peso = float(input('informe seu peso! '))
altura = float(input('informe sua altura! '))
imc=peso/(altura*altura)

if (imc<18.5):
    print(f'O seu indice de massa corporal {imc:.1f} indica que você é magro(a)')
    
elif(18.5<=imc<24.9):
    print(f'O seu indice de massa corporal {imc:.1f} indica que você tem o peso ideal')
    
elif(25.0<=imc<29.9):
    print(f'O seu indice de massa corporal {imc:.1f} indica que você esta com sobrepeso')
    
elif(30.0<=imc<34.9):
    print(f'O seu indice de massa corporal {imc:.1f} indica que você tem obesidade1')
    
elif(35.0<=imc<39.9):
    print(f'O seu indice de massa corporal {imc:.1f} indica que você tem obesidade2')
    
else:
    print(f'O seu indice de massa corporal {imc:.1f} indica que você tem obesidade3')
