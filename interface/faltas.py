#-------------------------Equipe-----------------------------

#Márcio Davi Almeida da Conceição / isaac Tavares / Caio alexandre

#----------------------integrantes---------------------------




import tkinter
import customtkinter as ct
from tkinter import messagebox

#------------Funções------------
def calcular():
    c = int(cargah.get())
    f = int(faltasd.get())
    diatotal = (c/4)
    faltadia = ((diatotal*0.25)-f)
    porcentagem_falta_resto = (f/c)*100
    
    if faltadia<0:
        resultado.configure(janela, text=f'Você foi Reprovado por {abs(faltadia)} faltas',
                    font=('comic sens ms',15,'bold'))
    else:
        resultado.configure(janela, text=f'você pode faltar {faltadia} // porcentagem de falta: {porcentagem_falta_resto*4:.0f}%',
                    font=('comic sans mc',15,'bold')).pack()
    
    
#-------------------------------

ct.set_appearance_mode('system')

janela = ct.CTk('#90df6d')
janela.geometry('400x400')
janela.title('faltas.com')
janela.iconbitmap()

ct.CTkLabel(janela, text='Gerenciador de Faltas',
            font=('arial',30,'bold'),
            text_color='#f0eebc').pack(pady=25)

cargah = ct.CTkEntry(janela,
                      placeholder_text='Digite a carga horaria',
                      width=250,height=40)
cargah.pack(pady=5)

faltasd = ct.CTkEntry(janela,
                      placeholder_text='Digite a quantidade de faltas',
                      width=250,height=40)
faltasd.pack(pady=5)

botao = ct.CTkButton(janela,text='Calcular',
                     font=('arial',20),
                     fg_color='#41add5',hover_color='white',
                     command=calcular)
botao.pack(pady=5)

resultado = ct.CTkLabel(janela,text='',
                        font=('arial',18))
resultado.pack(pady=5)

janela.mainloop()