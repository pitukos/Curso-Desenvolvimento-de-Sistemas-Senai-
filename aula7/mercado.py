
def contar_vogais(texto):
    vogais = 'aeiou'
    contador = 0
    for andar in texto:
        if andar in vogais:
            contador = contador+1
    print(f'a quantidade de vogais é {contador} ')
        
        
texto = input('Digite algum texto: ')

contar_vogais()