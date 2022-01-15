import pyautogui as p
import rpa as r
import pandas as pd
r.broswer
r.init() # abre navegador padrão
r.url('http://rpachallenge.com') # carrega o site
janela=p.getActiveWindow()
janela.maximize()
p.sleep(7) # tempo de espera
r.download('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx','challenge.xlsx') # faz o dowload do arquivo
p.sleep(1)

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1') # le arquivo excel
df = pd.DataFrame(dados, columns=["First Name","Last Name ", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])
r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
for row in df.itertuples(): # pega as cada de uma em uma linha da planilha com as variáveis.
    r.type('//*[@ng-reflect-name="labelFirstName"]',row[1])
    r.type('//*[@ng-reflect-name="labelLastName"]',row[2])
    r.type('//*[@ng-reflect-name="labelCompanyName"]',row[3])
    r.type('//*[@ng-reflect-name="labelRole"]',row[4])
    r.type('//*[@ng-reflect-name="labelAddress"]',row[5])
    r.type('//*[@ng-reflect-name="labelEmail"]',row[6])
    r.type('//*[@ng-reflect-name="labelPhone"]',str(row[7]))
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
p.sleep(7)
p.screenshot('score.png')
r.close()



