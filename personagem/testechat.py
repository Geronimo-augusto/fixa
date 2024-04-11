import pickle
from tkinter import *

janela = Tk()
janela.geometry('500x300')

# cria dicionário para armazenar texto das caixas de texto
texto_caixas = {}

# cria as caixas de texto
caixa_texto1 = Text(janela, height=5, width=30)
caixa_texto1.grid(row=0, column=0)
caixa_texto2 = Text(janela, height=5, width=30)
caixa_texto2.grid(row=1, column=0)

# função para salvar o texto das caixas de texto em um arquivo pickle
def salvar():
    # armazena o texto de cada caixa de texto no dicionário
    texto_caixas['caixa_texto1'] = caixa_texto1.get("1.0", END)
    texto_caixas['caixa_texto2'] = caixa_texto2.get("1.0", END)
    
    # salva o dicionário em um arquivo pickle
    with open('informacoes.pickle', 'wb') as f:
        pickle.dump(texto_caixas, f)
        
# função para carregar o texto das caixas de texto a partir do arquivo pickle
def carregar():
    # carrega o dicionário do arquivo pickle
    with open('informacoes.pickle', 'rb') as f:
        texto_caixas = pickle.load(f)
        
    # insere o texto de volta nas caixas de texto correspondentes
    caixa_texto1.delete("1.0", END)
    caixa_texto1.insert(END, texto_caixas['caixa_texto1'])
    
    caixa_texto2.delete("1.0", END)
    caixa_texto2.insert(END, texto_caixas['caixa_texto2'])

# cria botões para salvar e carregar as informações
botao_salvar = Button(janela, text="Salvar", command=salvar)
botao_salvar.grid(row=2, column=0)

botao_carregar = Button(janela, text="Carregar", command=carregar)
botao_carregar.grid(row=3, column=0)

janela.mainloop()
