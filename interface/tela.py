import tkinter
import customtkinter as ct

ct.set_appearance_mode('system')

janela = ct.CTk('#191970')


ct.CTkLabel(janela, text='LionHeart',
            font=('arial', 30,'bold'),
            text_color='yellow').pack(pady=15)

login = ct.CTkEntry(janela,
                    placeholder_text='Usuario',
                    width=200,height=40)
login.pack(pady=5)

senha = ct.CTkEntry(janela,
                    placeholder_text='Senha',
                    width=200,height=40,show='•')

senha.pack(pady=10)

botao = ct.CTkButton(janela,text='Login',
                     font=('arial',20),fg_color='darkred',hover_color='white')
botao.pack(pady=5)

janela.mainloop()