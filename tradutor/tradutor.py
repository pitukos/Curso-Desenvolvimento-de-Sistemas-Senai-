import customtkinter as ct
from deep_translator import GoogleTranslator
#--------funções--------
def traduzir():
  texto_traduzido.delete(0,'end')
  texto_para_traduzir = user_text.get()
  linguagem = var_get.get()
  saida = GoogleTranslator(source='auto',target=linguagem).translate(texto_para_traduzir)
  texto_traduzido.configure(state='normal')
  texto_traduzido.insert(0,saida)
  
ct.set_appearance_mode('system')

app = ct.CTk('#000035')
app.geometry('600x400')
app.resizable(False,False)
app.title('LionHeart Translator')
app.iconbitmap()

ct.CTkLabel(app, text='Universal LionHeart Translator',
            font=('arial',25,'bold'),
            text_color='#FFD700').pack(pady=5)

user_text= ct.CTkEntry(app,placeholder_text='Digite o texto para a tradução',
                    placeholder_text_color='black',
                      width=450,height=40,
                      border_color='#FFD700',
                      border_width=2)
user_text.pack(pady=20)

ct.CTkLabel(app, text='Escolha o idioma para tradução',
            font=('arial',20,'bold'),
            text_color='#FFD700').pack(pady=5)
var_get = ct.StringVar(value='english')
lista_idiomas = GoogleTranslator().get_supported_languages()
idioma= ct.CTkOptionMenu(app,
                         font=('arial',14,'bold'),
                         fg_color='#FFD700',
                         text_color=('black'),
                          values=lista_idiomas,
                          variable=var_get)
idioma.set('english')
idioma.pack(pady=5)

ct.CTkLabel(app,
            text='🌎 Texto Traduzido 🌎',
            font=('arial',20,'bold'),
            text_color='#FFD700').pack(pady=5)

texto_traduzido=ct.CTkEntry(app,
                            width=500, height=100,
                            state=ct.DISABLED)
texto_traduzido.pack(pady=10)

b1 = ct.CTkButton(app, text='Translate',
                  text_color='black',
                  fg_color='#FFD700',
                  font=('arial',18,'bold'),
                  command=traduzir)
b1.pack()

app.mainloop()