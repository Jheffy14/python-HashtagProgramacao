# Passo a passo do projeto de automação.
# Passo 1: Entrar no sistema da empresa 
    # exemplo https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
pyautogui.PAUSE = 0.5


# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
#texto tem que estar dentro de "" numeros nãos

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=541, y=378)  #da pra personalizar button="left" ou right ou do meio ou clicar 2 vezes clicks=2
#pyautogui.drag clica e arrasta
pyautogui.write("ejuliadoamaral@gmail.com")
pyautogui.press("tab")
pyautogui.write("pmsC0827,")
pyautogui.click(x=680, y=542)
time.sleep(2)

import pandas as pd #as pd é para abreviar
#pandas server para ler qualquer tipo de arquivo
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: #significa para cada linha colocar o tabela.index 
    #Codigo produto
    pyautogui.click(x=542, y=264)
    codigo = str(tabela.loc[linha, "codigo"])
    #pyautogui.write(str(codigo))

    #codig
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #Marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write (str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan": #if a variavel obs é diferetne de nan se for ela esecuta o obs
        pyautogui.write(obs)
  
    pyautogui.press("tab")
    pyautogui.press("enter")
    # apertar botaõ
    pyautogui.scroll(500)
