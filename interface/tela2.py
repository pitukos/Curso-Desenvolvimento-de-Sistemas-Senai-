from builtins import int
import tkinter
import customtkinter as ct
from tkinter import messagebox


def calcular():
    d = int(distancia.get())
    c = int(consumo.get())
    p = float(preco.get())
    
    calculo = (d/c)*p
    resultado.configure(text=f'O valor total para a viagem será de R$ {calculo:.2f}',text_color='#f0eebc')

ct.set_appearance_mode('system')

janela = ct.CTk('#90df6d')
janela.geometry('400x400')

ct.CTkLabel(janela, text='Consumo de Gasolina',
            font=('arial',30,'bold'),
            text_color='#f0eebc').pack(pady=25)

distancia = ct.CTkEntry(janela,
                      placeholder_text='Digite a Distancia',
                      width=250,height=40)
distancia.pack(pady=5)

consumo = ct.CTkEntry(janela,
                      placeholder_text='Digite o consumo do veiculo',
                      width=250,height=40)
consumo.pack(pady=5)

preco = ct.CTkEntry(janela,
                      placeholder_text='Digite o preço do combustivel',
                      width=250,height=40)
preco.pack(pady=5)

botao = ct.CTkButton(janela,text='Calcular',
                     font=('arial',20),
                     fg_color='#41add5',hover_color='white',
                     command=calcular)
botao.pack(pady=5)


resultado = ct.CTkLabel(janela,text='',
                        font=('arial',18))
resultado.pack(pady=5)

janela.mainloop()