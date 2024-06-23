# Sistema de Gerenciamento de Personagens
## Descrição
Este projeto é uma aplicação em Python que utiliza a biblioteca Tkinter para criar uma interface gráfica para gerenciar personagens,
incluindo funcionalidades para adicionar informações sobre espaço, talentos e magia. Os dados inseridos são salvos em arquivos.pickle para armazenamento e recuperação futuros.

## Estrutura do Projeto
- personagens: Pasta contendo o arquivo de código principal.
- Arquivos de imagem e arquivos.pickle: Localizados fora da pasta `personagens`.
## Dependências
- Python 3.x
- Tkinter
- Pillow (PIL)
- Pickle
## Instalação das Dependências
Você pode instalar as dependências utilizando `pip`:

```bash
pip install pillow
```
## Arquivo: `personagens/main.py`
### Código
```python
import tkinter as tk
from tkinter import Toplevel, Canvas, Text, Button
from PIL import ImageTk, Image
import pickle

fixa = tk.Tk()

def create_text_widgets(canvas, positions):
    text_widgets = []
    for (x, y, w, h) in positions:
        text = Text(canvas)
        text.place(x=x, y=y, width=w, height=h)
        text_widgets.append(text)
    print(text_widgets)
    return text_widgets

def open_new_window(title, image_path, text_positions, pickle_file):
    def save_data():
        data = [text.get("1.0", tk.END) for text in text_widgets]
        with open(pickle_file, 'wb') as f:
            pickle.dump(data, f)
        print(data)
    
    def load_data():
        try:
            with open(pickle_file, 'rb') as f:
                data = pickle.load(f)
            for i, text in enumerate(text_widgets):
                text.delete("1.0", tk.END)
                text.insert(tk.END, data[i])
        except FileNotFoundError:
            print(f"No data found in {pickle_file}")

    cont = Toplevel(fixa)
    cont.title(title)
    cont.geometry("716x900")

    # Load the image and store it as an attribute of the Toplevel window
    image = Image.open(image_path)
    cont.photo = ImageTk.PhotoImage(image)

    canvas = Canvas(cont, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=cont.photo, anchor='nw')

    Button(canvas, text="Fechar", command=cont.destroy).grid(row=0, column=0, padx=2, pady=3)
    Button(canvas, text="Salvar", command=save_data).grid(row=0, column=1, padx=2, pady=3)
    Button(canvas, text="Carregar", command=load_data).grid(row=0, column=2, padx=2, pady=3)

    text_widgets = create_text_widgets(canvas, text_positions)
    return text_widgets

def espaco():
    text_positions = [(0, 30, 710, 860)]
    open_new_window("Espaço", "../espaco.png", text_positions, '../informacoesEspaco.pickle')

def talentos():
    text_positions = [
        (48, 65, 174, 30), (308, 39, 360, 20), (308, 81, 360, 20),
        (40, 141, 420, 725), (490, 154, 185, 60), (490, 234, 185, 45),
        (490, 299, 185, 45), (490, 364, 185, 44)
    ]
    open_new_window("Talentos", "../talentos.png", text_positions, '../informacoesTalentos.pickle')

def magia():
    text_positions = [
        (55, 64, 200, 21), (345, 55, 60, 30), (460, 55, 60, 30),
        (580, 55, 60, 30), (35, 190, 210, 130), (55, 355, 170, 25),
        (35, 390, 200, 215), (55, 625, 170, 25), (35, 665, 210, 215)
    ]
    open_new_window("Magia", "../magias.png", text_positions, '../informacoesMagias.pickle')

def save_fixa():
    data = [text.get("1.0", tk.END) for text in textos_fixas]
    with open('../informacoes.pickle', 'wb') as f:
        pickle.dump(data, f)
    print(data)

def load_fixa():
    try:
        with open('../informacoes.pickle', 'rb') as f:
            data = pickle.load(f)
        for i, text in enumerate(textos_fixas):
            text.delete("1.0", tk.END)
            text.insert(tk.END, data[i])
    except FileNotFoundError:
        print("No data found in informacoes.pickle")

# Main window
fixa.geometry("716x900")
fixa.title("fixa")
image = Image.open("../status.png")
photo = ImageTk.PhotoImage(image)

canvasFixa = Canvas(fixa, width=image.width, height=image.height)
canvasFixa.pack(fill="both", expand=True)
canvasFixa.create_image(0, 0, image=photo, anchor='nw')

Button(canvasFixa, text="1", command=espaco).grid(column=1, row=1)
Button(canvasFixa, text="2", command=magia).grid(column=1, row=2)
Button(canvasFixa, text="3", command=talentos).grid(column=1, row=3)
Button(canvasFixa, text="Salvar", command=save_fixa).grid(row=1, column=3, padx=2, pady=3)
Button(canvasFixa, text="Carregar", command=load_fixa).grid(row=2, column=3, padx=2, pady=3)
Button(canvasFixa, text="Fechar", command=fixa.destroy).grid(column=2, row=1, padx=2, pady=0)

# Positions for the text widgets in the main window
text_positions_fixa = [
    (51, 60, 174, 30), (307, 40, 360, 20), (307, 75, 360, 20),
    (39, 175, 50, 25), (53, 209, 23, 18), (39, 260, 50, 25),
    (53, 294, 23, 18), (39, 343, 50, 25), (53, 376, 23, 18),
    (39, 427, 50, 25), (53, 460, 23, 18), (39, 511, 50, 25),
    (53, 544, 23, 18), (39, 595, 50, 25), (53, 628, 23, 18),
    (126, 362, 21, 300), (126, 229, 21, 100), (114, 146, 21, 22),
    (114, 189, 20, 22), (278, 170, 20, 22), (343, 170, 20, 22),
    (412, 170, 20, 22), (273, 225, 37, 22), (338, 225, 37, 22),
    (408, 225, 37, 22), (278, 300, 40, 22), (403, 310, 42, 15),
    (403, 292, 42, 15), (500, 144, 37, 25), (500, 174, 37, 25),
    (500, 208, 37, 25), (500, 238, 37, 25), (500, 270, 37, 25),
    (500, 304, 37, 25), (500, 335, 37, 25), (500, 368, 37, 25),
    (590, 155, 90, 18), (590, 185, 90, 18), (577, 220, 28, 18),
    (581, 257, 105, 115), (38, 691, 422, 190), (486, 415, 200, 450),
    (257, 560, 202, 90), (257, 430, 202, 15), (257, 454, 202, 15),
    (257, 478, 202, 15), (257, 500, 202, 15), (257, 524, 202, 15),
    (257, 375, 30, 15)
]

textos_fixas = create_text_widgets(canvasFixa, text_positions_fixa)

fixa.mainloop()
```
## Funcionalidades
1. Criar Widgets de Texto: A função create_text_widgets cria widgets de texto em posições especificadas em um canvas.
2. Abrir Novas Janelas: A função open_new_window abre uma nova janela com um título, uma imagem de fundo e widgets de texto nas posições especificadas. Também permite salvar e carregar dados dos widgets de texto usando arquivos .pickle.
3. Espaço, Talentos e Magia: Funções espaco, talentos e magia abrem janelas específicas para adicionar informações sobre espaço, talentos e magia, respectivamente.
4. Salvar e Carregar Dados: As funções save_fixa e load_fixa permitem salvar e carregar os dados dos widgets de texto na janela principal.
## Como Executar
1. Certifique-se de que as imagens (espaco.png, talentos.png, magias.png, status.png) e os arquivos .pickle estejam fora da pasta personagens.
2. Navegue até a pasta personagens:
```bash
cd personagens
```
3. Execute o arquivo main.py:
```bash
python main.py
```
