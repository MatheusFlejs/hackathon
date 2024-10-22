import pyautogui as pyg
import time
import pandas as pd

pyg.PAUSE = 0.9

#entrando no chrome
pyg.press("win")
pyg.write("chrome")
pyg.press("enter")

#entrar no Gmail
time.sleep(3)

pyg.press("tab")
pyg.press("tab")
pyg.press("tab")
pyg.press("tab")
pyg.press("tab")
pyg.press("tab")
pyg.press("tab")
pyg.press("enter")

pyg.write("https://mail.google.com/mail/u/1/?hl=pt-BR&shva=1#inbox?compose=new")
pyg.press("enter")

time.sleep(3.5)

tabela = pd.read_excel("entrega.xlsx")

#digitar linhar 0

for linha in tabela.index:  # Para cada linha no índice da tabela
    time.sleep(2)  # Pausa a execução do programa por 2 segundos
    pyg.click(x=79, y=220)  # Clica na posição (79, 220) da tela
    pyg.write(str(tabela.loc[linha, "User"]))  # Escreve o valor da coluna "User" da linha atual
    pyg.press("enter")  # Pressiona a tecla "Enter"
    time.sleep(2)  # Pausa a execução do programa por mais 2 segundos
    
    #submit
    pyg.click(x=940, y=364)
    time.sleep(1.5) 
    pyg.write("Compra Moveis INSS")
    

    #adicionar imgs
    pyg.click(x=1087, y=696)
    time.sleep(1.5) 
    pyg.click(x=449, y=261)
    time.sleep(1.5)
    pyg.click(x=686, y=557)
    time.sleep(1.5)
    pyg.doubleClick(x=598, y=177)
    time.sleep(1.5)
    pyg.press("enter")
    pyg.press("enter")
    pyg.press("enter")
    pyg.press("enter")



    #corpo da mensagem
    pyg.write("                      OLA, VOCE ENTROU EM CONTATO")
    pyg.press("enter")
    pyg.write("                      COM MOVEIS INSS")
    time.sleep(1.8)
    pyg.press("enter")
    pyg.write("                      SEU PEDIDO FOI CONFIRMADO")
    time.sleep(1.8)
    pyg.press("enter")
    pyg.press("enter")
    pyg.press("enter")
    pyg.press("enter")


    #footer

    pyg.click(x=1087, y=696)
    time.sleep(1.5) 
    pyg.click(x=449, y=261)
    time.sleep(1.5)
    pyg.click(x=686, y=557)
    time.sleep(1.5)
    pyg.doubleClick(x=499, y=186)
    time.sleep(1.5)
    pyg.press("tab")
    pyg.press("enter")

