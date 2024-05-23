
from tkinter import *
import pickle
from PIL import Image, ImageTk


fixa = Tk()

def espaco():
    cont= Toplevel(fixa)
    cont.title( "continuacao")
    cont.geometry("716x900")

    imag = Image.open("./espaco.png")
    photo = ImageTk.PhotoImage(imag)

    canvasEspaco = Canvas(cont, width=imag.width, height=imag.height)
    canvasEspaco.pack(fill="both", expand=True)
    canvasEspaco.create_image(0,0, image =photo, anchor = 'nw')
    

    botao_voltar= Button(canvasEspaco, text= "fechar", command=lambda: sair_salvar())
    botao_voltar.grid(column= 0, row= 0,padx=0, pady=3)

    salvar = Button(canvasEspaco, text="salvar",command=lambda: salvar_espaco())
    salvar.grid(row=0, column= 1,padx=2, pady=3) 
    botao_carregar = Button(canvasEspaco, text="carregar",command=lambda: carregar_espaco())
    botao_carregar.grid(row=0, column= 2,padx=2, pady=3) 

    textocont = Text(canvasEspaco)
    textocont.place( x= 0, y= 30, width= 710, height= 860)

    def sair_salvar():
         salvar_espaco()
         cont.destroy()
    

    def salvar_espaco():
        cont = {}
        cont['textocont'] = textocont.get("1.0", END)
        
        with open('informacoesEspaco.pickle', 'wb') as f:
            pickle.dump(cont , f)
        print(cont)
    def carregar_espaco():
        with open('informacoesEspaco.pickle', 'rb') as f:
                cont = pickle.load(f)
                print(cont)
                textocont.delete("1.0", END)
                textocont.insert(END, cont['textocont'])

    cont.wait_window()



def talentos():
    cont= Toplevel(fixa)
    cont.title( "talentos")
    cont.geometry("716x900")
   
    imag = Image.open("talentos.png")
    photo = ImageTk.PhotoImage(imag)

    canvasTalentos = Canvas(cont, width=imag.width, height=imag.height)
    canvasTalentos.pack(fill="both", expand=True)
    canvasTalentos.create_image(0,0, image =photo, anchor = 'nw')
    
    botao_voltar= Button(canvasTalentos, text= "fechar", command=lambda: sair_salvar())
    botao_voltar.grid(column= 0, row= 0,padx=0, pady=3)

    salvar = Button(canvasTalentos, text="salvar",command=lambda: salvar_talentos())
    salvar.grid(row=0, column= 1,padx=2, pady=3) 
    botao_carregar = Button(canvasTalentos, text="carregar",command=lambda: carregar_talentos())
    botao_carregar.grid(row=0, column= 2,padx=2, pady=3) 
   
    lista = [["texto_NOME3",48, 65, 174,  30],["textoINFO6", 308, 39, 360,  20],["textoINFO7", 308, 81, 360,  20],["textoCARAC",40, 141, 420,  725],["textoTRPER",490, 154,185,  60],["textoIDE", 490, 234,185,  45],["textoVIN",490, 299,185,  45],["textoFRAQ", 490, 364,185,  44]]

    for index in lista:
        for i in index:
            texto = index[0]   
            texto = Text(canvasTalentos)
            texto.place(x=index[1],y=index[2], width= index[3], height= index[4])
    
    # texto_NOME3=  Text(canvasTalentos)
    # texto_NOME3.place(x= 48, y= 65, width=174, height= 30)
    # textoINFO6=  Text(canvasTalentos)
    # textoINFO6.place(x= 308, y= 39, width=360, height= 20)
    # textoINFO7=  Text(canvasTalentos)
    # textoINFO7.place(x= 308, y= 81, width=360, height= 20)

    # textoCARAC=  Text(canvasTalentos)
    # textoCARAC.place(x= 40, y= 141, width=420, height= 725)

    # textoTRPER=  Text(canvasTalentos)
    # textoTRPER.place(x= 490, y= 154, width=185, height= 60)

    # textoIDE=  Text(canvasTalentos)
    # textoIDE.place(x= 490, y= 234, width=185, height= 45)

    # textoVIN=  Text(canvasTalentos)
    # textoVIN.place(x= 490, y= 299, width=185, height= 45)

    # textoFRAQ=  Text(canvasTalentos)
    # textoFRAQ.place(x= 490, y= 364, width=185, height= 44)
    textos_talentos=["texto_NOME3","textoINFO6","textoINFO7","textoCARAC","textoTRPER","textoIDE","textoVIN","textoFRAQ"]

    def sair_salvar():
        salvar_talentos()
        cont.destroy()
    

    def salvar_talentos():
        cont = []
        print(textos_talentos)
        for texto in textos_talentos :
            info = texto.get("1.0", END)
            cont.append(info)
        with open('informacoesTalentos.pickle', 'wb') as f:
            pickle.dump(cont , f)
        print(cont)


    def carregar_talentos():
        with open('informacoesTalentos.pickle', 'rb') as f:
                info = pickle.load(f)
                print(info)
        for i, texto in enumerate(textos_talentos):
            if i < len(info):
                texto.delete("1.0", END)
                texto.insert(END, info[i])

    cont.wait_window()
def magia():
    cont= Toplevel(fixa)
    cont.title( "magia")
    cont.geometry("716x900")
    imag = Image.open("magias.png")
    photo = ImageTk.PhotoImage(imag)

    canvasMaiga = Canvas(cont, width=imag.width, height=imag.height)
    canvasMaiga.pack(fill="both", expand=True)
    canvasMaiga.create_image(0,0, image =photo, anchor = 'nw')

    botao_voltar= Button(canvasMaiga, text= "fechar", command=lambda: sair_salvar())
    botao_voltar.grid(column= 0, row= 0,padx=0, pady=3)

    salvar = Button(canvasMaiga, text="salvar",command=lambda: salvar_magias())
    salvar.grid(row=0, column= 1,padx=2, pady=3) 
    botao_carregar = Button(canvasMaiga, text="carregar",command=lambda: carregar_magias())
    botao_carregar.grid(row=0, column= 2,padx=2, pady=3) 

    texto_NOME2 =  Text(canvasMaiga)
    texto_NOME2.place(x= 55, y= 64, width=200, height= 21)

    textoINFO3=  Text(canvasMaiga)
    textoINFO3.place(x= 345, y= 55, width=60, height= 30)
    textoINFO4=  Text(canvasMaiga)
    textoINFO4.place(x= 460, y= 55, width=60, height= 30)

    textoINFO5=  Text(canvasMaiga)
    textoINFO5.place(x= 580, y= 55, width=60, height= 30)

    textoTRUQUES=  Text(canvasMaiga)
    textoTRUQUES.place(x= 35, y= 190, width=210, height= 130)

    textoESPACOS=  Text(canvasMaiga)
    textoESPACOS.place(x= 55, y= 355, width=170, height= 25)

    textoMAGIAS=  Text(canvasMaiga)
    textoMAGIAS.place(x= 35, y= 390, width=200, height= 215)

    textoESPACOS2=  Text(canvasMaiga)
    textoESPACOS2.place(x= 55, y= 625, width=170, height= 25)

    textoMAGIAS2=  Text(canvasMaiga)
    textoMAGIAS2.place(x= 35, y= 665, width=210, height= 215)

    textos_magias = [texto_NOME2,textoINFO3,textoINFO4,textoINFO5,textoTRUQUES,textoESPACOS,textoMAGIAS,textoESPACOS2, textoMAGIAS2]

    def sair_salvar():
        salvar_magias()
        cont.destroy()
    

    def salvar_magias():
        cont = []
        print()
        for texto in textos_magias :
            info = texto.get("1.0", END)
            cont.append(info)
        with open('informacoesMagias.pickle', 'wb') as f:
            pickle.dump(cont , f)
            print(cont)
    def carregar_magias():
        with open('informacoesMagias.pickle', 'rb') as f:
                info = pickle.load(f)
                print(info)
        for i, texto in enumerate(textos_magias):
            if i < len(info):
                texto.delete("1.0", END)
                texto.insert(END, info[i])

    cont.wait_window() 

    
class status():    
    imag = Image.open("status.png")

    photo = ImageTk.PhotoImage(imag)

    canvasFixa = Canvas(fixa, width=imag.width, height=imag.height)
    canvasFixa.pack(fill="both", expand=True)
    canvasFixa.create_image(0,0, image =photo, anchor = 'nw')

    botao = Button(canvasFixa, text = "1", command=espaco)
    botao.grid(column= 1, row= 1, )

    botao2 = Button(canvasFixa, text = "2", command=magia)
    botao2.grid(column= 1, row= 2, )

    botao3 = Button(canvasFixa, text = "3", command=talentos)
    botao3.grid(column= 1, row= 3, )

    salvarFixa = Button(canvasFixa, text = "Salvar a fixa", command=lambda:status.salvar_fixa())
    salvarFixa.grid(row=1, column= 3,padx=2, pady=3) 

    botao_carregar = Button(canvasFixa, text="Carregar", command=lambda:status. carregar())
    botao_carregar.grid(row=2, column=3,padx=2, pady=3) 

    botao_voltar= Button(canvasFixa, text= "fechar", command=lambda: status.sair_salvar())
    botao_voltar.grid(column= 2, row= 1,padx=2, pady=0)



    texto_NOME=  Text(canvasFixa)
    texto_NOME.place(x = 51,y =60, width=30, height= 174)
    textoINFO=  Text(canvasFixa)
    textoINFO.place(x= 307, y= 40, width=360, height= 20)
    textoINFO2=  Text(canvasFixa)
    textoINFO2.place(x= 307, y= 75, width=360, height= 20)

    #status de cima pra baixo 
    textoF=  Text(canvasFixa)
    textoF.place(x= 39, y= 175, width=50, height= 25)
    textoPF=  Text(canvasFixa)
    textoPF.place(x= 53, y= 209, width=23, height= 18)

    textoD=  Text(canvasFixa)
    textoD.place(x= 39, y= 260, width=50, height= 25)
    textoPD=  Text(canvasFixa)
    textoPD.place(x= 53, y= 294, width=23, height= 18)


    textoC=  Text(canvasFixa)
    textoC.place(x= 39, y= 343, width=50, height= 25)
    textoPC=  Text(canvasFixa)
    textoPC.place(x= 53, y= 376, width=23, height= 18)

    textoI=  Text(canvasFixa)
    textoI.place(x= 39, y= 427, width=50, height= 25)
    textoPI=  Text(canvasFixa)
    textoPI.place(x= 53, y= 460, width=23, height= 18)

    textoS=  Text(canvasFixa)
    textoS.place(x= 39, y= 511, width=50, height= 25)
    textoPS=  Text(canvasFixa)
    textoPS.place(x= 53, y= 544, width=23, height= 18)

    textoCA=  Text(canvasFixa)
    textoCA.place(x= 39, y= 595, width=50, height= 25)
    textoPCA=  Text(canvasFixa)
    textoPCA.place(x= 53, y= 628, width=23, height= 18)

    #pericias 
    textoPer=  Text(canvasFixa)
    textoPer.place(x= 126, y= 362, width=21, height= 300)
    textoSal=  Text(canvasFixa)
    textoSal.place(x= 126, y= 229, width=21, height= 100)

    #bonus e inspiraçao
    textoINSP=  Text(canvasFixa,)
    textoINSP.place(x= 114, y= 146, width=21, height= 22)
    textoBonus=  Text(canvasFixa)
    textoBonus.place(x= 114, y= 189, width=20, height= 22)

    #caixa do lado das pericias
    textoARM=  Text(canvasFixa)
    textoARM.place(x= 278, y= 170, width=20, height= 22)

    textoINI=  Text(canvasFixa)
    textoINI.place(x= 343, y= 170, width=20, height= 22)

    textoDES=  Text(canvasFixa)
    textoDES.place(x= 412, y= 170, width=20, height= 22)

    textoPV=  Text(canvasFixa)
    textoPV.place(x= 273, y= 225, width=37, height= 22)

    textoPVA=  Text(canvasFixa)
    textoPVA.place(x= 338, y= 225, width=37, height= 22)

    textoPVT=  Text(canvasFixa)
    textoPVT.place(x= 408, y= 225, width=37, height= 22)

    textoDV=  Text(canvasFixa)
    textoDV.place(x= 278, y= 300, width=40, height= 22)

    textoSUS=  Text(canvasFixa)
    textoSUS.place(x= 403, y= 310, width=42, height= 15)

    textoFAL=  Text(canvasFixa)
    textoFAL.place(x= 403, y= 292, width=42, height= 15)

    #diheiro
    textoCOBRE=  Text(canvasFixa)
    textoCOBRE.place(x= 500, y= 144, width=37, height= 25)

    textoPRATA=  Text(canvasFixa)
    textoPRATA.place(x= 500, y= 174, width=37, height= 25)

    textoPE=  Text(canvasFixa)
    textoPE.place(x= 500, y= 208, width=37, height= 25)

    textoOURO=  Text(canvasFixa)
    textoOURO.place(x= 500, y= 238, width=37, height= 25)

    textoPLATINA=  Text(canvasFixa)
    textoPLATINA.place(x= 500, y= 270, width=37, height= 25)

    textoESMERALDA=  Text(canvasFixa)
    textoESMERALDA.place(x= 500, y= 304, width=37, height= 25)

    textoCOBALTO=  Text(canvasFixa)
    textoCOBALTO.place(x= 500, y= 335, width=37, height= 25)

    textoDIA=  Text(canvasFixa)
    textoDIA.place(x= 500, y= 368, width=37, height= 25)

    #as parte do lado do dinheiro
    textoESV=  Text(canvasFixa)
    textoESV.place(x=590, y= 155, width=90, height= 18)

    textoPRD=  Text(canvasFixa)
    textoPRD.place(x=590, y= 185, width=90, height= 18)

    textoREF=  Text(canvasFixa)
    textoREF.place(x= 577, y= 220, width=28, height= 18)

    textoIDIOMA=  Text(canvasFixa)
    textoIDIOMA.place(x= 581, y= 257, width=105, height= 115)

    #laaaaaaaaa em baixo
    textoPER=  Text(canvasFixa)
    textoPER.place(x= 38, y= 691, width=422, height= 190)

    #euipamentos 
    textoEQUIP=  Text(canvasFixa)
    textoEQUIP.place(x= 486, y= 415, width=200, height= 450)

    textoATQ=  Text(canvasFixa)
    textoATQ.place(x= 257, y= 560, width=202, height= 90)

    textoATQ1=  Text(canvasFixa)
    textoATQ1.place(x= 257, y= 430, width=202, height= 15)

    textoATQ2=  Text(canvasFixa)
    textoATQ2.place(x= 257, y= 454, width=202, height= 15)

    textoATQ3=  Text(canvasFixa)
    textoATQ3.place(x= 257, y= 478, width=202, height= 15)

    textoATQ4=  Text(canvasFixa)
    textoATQ4.place(x= 257, y= 500, width=202, height= 15)

    textoATQ4=  Text(canvasFixa)
    textoATQ4.place(x= 257, y= 524, width=202, height= 15)

    #percepçao
    textoINTUICAO=  Text(canvasFixa)
    textoINTUICAO.place(x= 257, y= 375, width=30, height= 15)

    textos_fixas = [texto_NOME,textoINFO, textoINFO2, textoF,textoPF, textoD,textoPD,textoPC, textoI,textoPI, textoS,textoPS,textoCA,textoPCA,textoPer,textoSal,textoINSP,textoBonus,textoARM,textoINI,textoDES, textoPV,textoPVA,textoPVT,textoDV,textoSUS,textoFAL,textoCOBRE,textoPRATA,textoPE,textoOURO,textoPLATINA,textoESMERALDA,textoCOBALTO,textoDIA,textoESV,textoPRD,textoREF,textoIDIOMA,textoPER,textoEQUIP,textoATQ,textoATQ1,textoATQ2,textoATQ3,textoATQ4,textoINTUICAO, ]
    
    def salvar_fixa():
        cont = []
        for texto in status.textos_fixas :
            info = texto.get("1.0", END)
            cont.append(info)
        with open('informacoes.pickle', 'wb') as f:
            pickle.dump(cont , f)
        print(cont)

    def carregar():
        with open('informacoes.pickle', 'rb') as f:
                info = pickle.load(f)
                print(info)
        for i, texto in enumerate(status.textos_fixas):
            if i < len(info):
                texto.delete("1.0", END)
                texto.insert(END, info[i])
    def sair_salvar():
        status.salvar_fixa()
        fixa.destroy()
status() 
fixa.mainloop()
#lista = [[nome do texto, x, y , width, heihnt],]
# for index in lista
#   for i in index    
#    index[0] = Text(canvasFixa)
#    index[0].place(x=index[1],y=index[2], width= index[3] height= index[4])
