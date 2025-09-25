import tkinter
import customtkinter as ct
from tkinter import messagebox
#------------Funções------------
def calcular_imc(event=None):
    n=(nome.get())
    a=float(altura.get())
    p=float(peso.get())
    
    imc=p/(a*a)
    if imc <18.5:
        resultado.configure(text=f'{n},seu imc é {imc:.2f} você é magro')
    elif imc >=18.5 and imc <25:
        resultado.configure(text=f'{n},seu imc é {imc:.2f} você tem o peso ideal')
    elif imc >=25 and imc <30:
        resultado.configure(text=f'{n},seu imc é {imc:.2f} você esta com sobrepeso')
    else:
     resultado.configure(text=f'{n},seu imc é {imc:.2f} você é obeso')

def limpar():
    nome.delete(0,'end')
    peso.delete(0,'end')
    altura.delete(0,'end')
    resultado.configure(text='')
    
#-------------------------------
ct.set_appearance_mode('dark')

janela = ct.CTk('black')
janela.geometry('400x400')
janela.title('LionHeart Saúde')
janela.iconbitmap()

ct.CTkLabel(janela, text='Aplicativo IMC',
            font=('arial',30,'bold'),
            text_color='#FFD700').pack(pady=25)

nome = ct.CTkEntry(janela,
                    placeholder_text='Nome',
                    placeholder_text_color='white',
                      width=250,height=40,
                      border_color='#FFD700',
                      border_width=2)
nome.pack(pady=5)

peso = ct.CTkEntry(janela,
                    placeholder_text='Peso',
                    placeholder_text_color='white',
                      width=250,height=40,
                      border_color='#FFD700',
                      border_width=2)
peso.pack(pady=5)

altura = ct.CTkEntry(janela,
                    placeholder_text='Altura',
                    placeholder_text_color='white',
                      width=250,height=40,
                      border_color='#FFD700',
                      border_width=2)
altura.pack(pady=5)

botao_calcular = ct.CTkButton(janela,text='calcular',
                      font=('arial',25),
                      fg_color='#FFD700', hover_color='white',
                      command=calcular_imc)
botao_calcular.place(x=50,y=250)

botao_limpar = ct.CTkButton(janela,text='limpar',
                      font=('arial',25),
                      fg_color='#FFD700', hover_color='white',
                      command=limpar)
botao_limpar.place(x=200,y=250)

resultado = ct.CTkLabel(janela,text='' ,text_color='#FFD700',
                        font=('arial',18))
resultado.pack(pady=60)

janela.bind('<Return>',calcular_imc)
janela.mainloop()