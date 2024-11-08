# Para qualquer automação - passo a passo



# Entrar no sistema da empresa
# Fazer login no sistema
# Importar a base de dados
# Cadastrar um produto
# Repetir isso até acabar a base de dados

import pyautogui
import time


pyautogui.PAUSE = 0.5 


pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)

pyautogui.click(x=775, y=360)
pyautogui.write("guilhermesanches.pessoal@gmail.com")
pyautogui.press("tab")
pyautogui.write("examplesenha")
pyautogui.press("tab")
pyautogui.click(977, y=507)
time.sleep(1)



import pandas
tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index: 

    pyautogui.click(x=711, y=243)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    obs= tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.click(x=897, y=889)
    pyautogui.scroll(5000)




