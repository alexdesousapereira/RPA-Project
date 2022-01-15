import rpa as r
import pyautogui as p

r.init() # padrão navegador
# r.init(visual_automation = True, chrone=False) # caso queira utilizar outro software

# r.url('https://www.google.com.br/')
# janela = p.getActiveWindow() # captura a janela utilizada
# janela.maximize() # maximiza a janela
# r.wait(2.0) # tempo para executar ( neste caso tem ser em decimal)
# r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', 'RPA[enter]') #busca no google
# r.wait(2.0)
# r.snap('page', 'rpa_page.png') # tira print da tela
# r.wait(2.0)
# r.close()# fecha o navegador

# Outra forma procurando pela váriavel

r.url('https://www.google.com.br/')
janela = p.getActiveWindow() # captura a janela utilizada
janela.maximize() # maximiza a janela
r.wait(2.0) # tempo para executar ( neste caso tem ser em decimal)
r.type('//*[@name="q"]', 'RPA[enter]') #busca no google
r.wait(2.0)
r.snap('page', 'rpa_page.png') # tira print da tela
r.wait(2.0)
r.close()# fecha o navegador

