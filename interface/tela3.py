from builtins import int
import tkinter
import customtkinter as ct
import os
from tkinter import messagebox

#---------Funções-------------
def shutdown():
    os.system('shutdown -s ')
    
def restart():
    os.system('shutdown /r /t 0')
    
def logoff():
    os.system('shutdown -l')
#-----------------------------
ct.set_appearance_mode('system')

janela = ct.CTk('#008080')

janela.maxsize(300,600)

janela.minsize(300,400)

janela.title('LionHeart PowerPatch V.1.0')

janela.iconbitmap('lion_39035.ico')

ct.CTkLabel(janela, text='Power Patch',
            font=('verdana',30,'bold'),
            text_color='#ADFF2F').pack(pady=25)

desligar = ct.CTkButton(janela, text='Desligar',
                        width=250,height=20,
                        fg_color='#2F4F4F',hover_color='white',
                        font=('verdana',30,'bold'),
                        cursor='hand2',
                        command=shutdown)
desligar.pack(pady=20)
   
reiniciar = ct.CTkButton(janela, text='Reiniciar',
                        width=250,height=20,
                        fg_color='#2F4F4F',hover_color='white',
                        font=('verdana',30,'bold'),
                        cursor='hand2',
                        command=restart) 
reiniciar.pack(pady=20)   
   
bloquear = ct.CTkButton(janela, text='Bloquear',
                        width=250,height=20,
                        fg_color='#2F4F4F',hover_color='white',
                        font=('verdana',30,'bold'),
                        cursor='hand2',
                        command=logoff) 
bloquear.pack(pady=20)   





janela.mainloop()