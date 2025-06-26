import pandas as pd
import pyautogui
import time
import os

# 1. Lê os dados da planilha
df = pd.read_excel("clientes.xlsx")

# 2. Abre o navegador (substitua 'chrome' se quiser outro navegador)
os.system("start chrome")
time.sleep(3)  # Espera o navegador abrir

# 3. Digita o site da empresa
pyautogui.write("https://www.suaempresa.com.br/cadastro", interval=0.05)
pyautogui.press("enter")
time.sleep(5)  # Espera o site carregar

# 4. Preenche os campos para cada cliente
for index, row in df.iterrows():
    # Espera garantir que os campos estão prontos
    time.sleep(1)
    
    # Digita Código do Produto
    pyautogui.write(str(row['Código Produto']), interval=0.05)
    pyautogui.press('tab')

    # Digita Nome
    pyautogui.write(row['Nome completo do cliente'], interval=0.05)
    pyautogui.press('tab')

    # Digita Produto
    pyautogui.write(row['Produto'], interval=0.05)
    pyautogui.press('tab')

    # Digita Valor unitário
    pyautogui.write(str(row['Valor unitário']), interval=0.05)
    pyautogui.press('tab')

    # Digita Quantidade pedida
    pyautogui.write(str(row['Quantidade pedida']), interval=0.05)
    pyautogui.press('tab')

    # Digita Valor Total
    pyautogui.write(str(row['Valor Total da Compra']), interval=0.05)
    pyautogui.press('tab')

    # Pressiona Enter para cadastrar
    pyautogui.press('enter')

    # Espera um tempo antes do próximo cadastro
    time.sleep(2)

print("Todos os clientes foram cadastrados com sucesso!")
