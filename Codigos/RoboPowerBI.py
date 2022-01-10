import pyautogui as p
import rpa as r
# Robo Power BI
def BotRobo():
    p.FAILSAFE = False # caso haja algum erro no robo.
    p.hotkey('win','r') # seleciona duas teclas de um teclado.
    p.sleep(2) # tempo de espera.
    p.write('C:\DashboardLogistica.pbix') # local do dashboard.
    p.sleep(1)
    p.press('enter') # aperta tecla enter.
    p.sleep(45)
    janela = p.getActiveWindow() 
    janela.maximize() # maximiza a janela.
    p.sleep(5)
    p.click(833,105) # local do botão de atualizar.
    r.close
BotRobo()
