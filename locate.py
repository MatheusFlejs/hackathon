import pyautogui
import time
import pandas as pd
tabela = pd.read_excel("entrega.xlsx")
time.sleep(2)
print(pyautogui.position()) 
#pyautogui.PAUSE = 3
#pyautogui.click(x=665, y=749)

#pyautogui.press("tab")

#linha = 0

#for linha in tabela.index:

    #pyautogui.write(str(tabela.loc[linha, "User"]))
    #pyautogui.press("tab")
    #pyautogui.press("enter")