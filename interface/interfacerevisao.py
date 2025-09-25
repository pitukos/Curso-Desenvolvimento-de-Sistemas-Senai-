import tkinter
import customtkinter as ct
import os
from tkinter import messagebox

def escola():
    n1 = float(unidade1.get())
    n2 = float(unidade2.get())
    n3 = float(unidade3.get())
    
    media = (n1+n2+n3)/3
    if(media>=6):
        resultado.configure(text=f'A sua média foi {media} você foi aprovadoª')
    else:
       resultado.configure(text=f'A sua média foi {media:.1f} você foi para a recuperação')
    
    
    
ct.set_appearance_mode('system')

janela = ct.CTk()

janela.geometry('400x400')

janela.title('LionHeart Notas')

janela.iconbitmap('lion_39035.ico')

unidade1= ct.CTkEntry(janela, width=400, height=20,
                      placeholder_text='Digite a nota da safadaaaaaaaaa 1º unidade')
unidade1.pack(pady=5)

unidade2= ct.CTkEntry(janela, width=400, height=20,
                      placeholder_text='Digite a nota da safadinhaaaa 2º unidade')
unidade2.pack(pady=5)

unidade3= ct.CTkEntry(janela, width=400, height=20,
                      placeholder_text='Digite a nota da safadonaa3 º unidade')
unidade3.pack(pady=5)

botao = ct.CTkButton(janela,text='Calcular',
                     font=('arial',20),
                     fg_color='#41add5',hover_color='white',
                     command=escola)
botao.pack(pady=5)

resultado = ct.CTkLabel(janela,text='',
                        font=('arial',18))
resultado.pack(pady=5)

ct.CTkLabel(janela, text='Media Colegial',
            font=('arial',30,'bold'),
            text_color='#000000').pack(pady=5)

janela.mainloop()