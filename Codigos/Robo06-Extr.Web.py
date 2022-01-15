# Biliotecas
import pyautogui as p
import rpa as r
import pandas as pd
import os as o

# Código
r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(10)

countPage = 1
while countPage <= 3:
    if countPage == 1:
        r.table('//*[@id="tableSandbox"]','Temp.csv') # retira os dados e salva em uma tabela
        dados = pd.read_csv('Temp.csv') # abri o conjunto de dados na variavel dados
        dados.to_csv(r"Webtable.csv", mode = 'a', index=None, header=True)
        r.click('//*[@id="tableSandbox_next"]') # muda de página
    else:
        r.table('//*[id="tablesandbox"]', 'Temp.csv')  # retira os dados e salva em uma tabela
        dados = pd.read_csv('Temp.csv')  # abri o conjunto de dados na variavel dados
        dados.to_csv(r"Webtable.csv", mode='a', index=None, header=False)
        r.click('//*[@id="tableSandbox_next"]')  # muda de página
    countPage = 1 + countPage
r.close() # Fecha o navegador
o.remove('Temp.csv') # remove o arquivo
csv_xlsx = pd.read_csv('WebTable.csv') # le o arquivo csv
csv_xlsx.to_excel(r'WebTable02.xlsx') # transforma o arquivo em excel
