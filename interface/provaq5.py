import tkinter
import customtkinter as ct
import os
from tkinter import messagebox

#---------Funções-------------
def adição():
    a = float(num1.get())
    b = float(num2.get())
    M = a+b
    resultado.configure(text=(f'O resultado é de : {M}'))
def subtração():
    a = float(num1.get())
    b = float(num2.get())
    M = a-b
    resultado.configure(text=(f'O resultado é de : {M}'))
def multiplicação():
    a = float(num1.get())
    b = float(num2.get())
    M = a*b
    resultado.configure(text=(f'O resultado é de : {M}'))
def divisão():
    a = float(num1.get())
    b = float(num2.get())
    M = a/b
    resultado.configure(text=(f'O resultado é de : {M}'))
#----------------------------

ct.set_appearance_mode('system')

janela = ct.CTk('#008080')

janela.geometry('400x600')

janela.title('LionHeart Calculadora')

janela.iconbitmap('lion_39035.ico')

ct.CTkLabel(janela, text='Calculadora',
            font=('verdana',30,'bold'),
            text_color='#ADFF2F').pack(pady=25)

num1 = ct.CTkEntry(janela,
                      placeholder_text='Digite um valor',
                      width=250,height=40)
num1.pack(pady=5)

num2 = ct.CTkEntry(janela,
                      placeholder_text='Digite um valor',
                      width=250,height=40)
num2.pack(pady=5)

som1 = ct.CTkButton(janela, text='+',
                        width=20,height=20,
                        fg_color='#2F4F4F',hover_color='white',
                        font=('verdana',30,'bold'),
                        cursor='hand2',
                        command=adição)
som1.pack(pady=10)

som2 = ct.CTkButton(janela, text='-',
                        width=20,height=20,
                        fg_color='#2F4F4F',hover_color='white',
                        font=('verdana',30,'bold'),
                        cursor='hand2',
                        command=subtração)
som2.pack(pady=10)

som3 = ct.CTkButton(janela, text='*',
                        width=20,height=20,
                        fg_color='#2F4F4F',hover_color='white',
                        font=('verdana',30,'bold'),
                        cursor='hand2',
                        command=multiplicação)
som3.pack(pady=10)

som4 = ct.CTkButton(janela, text='/',
                        width=20,height=20,
                        fg_color='#2F4F4F',hover_color='white',
                        font=('verdana',30,'bold'),
                        cursor='hand2',
                        command=divisão)
som4.pack(pady=10)

resultado = ct.CTkLabel(janela,text='',
                        font=('arial',18))
resultado.pack(pady=5)

janela.mainloop()