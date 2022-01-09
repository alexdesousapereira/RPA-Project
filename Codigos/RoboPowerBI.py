import pyautogui as p

p.hotkey('win','r') # seleciona duas teclas de um teclado
p.sleep(2)
p.write('C:\DashboardLogistica.pbix')
p.sleep(1)
p.press('enter')
p.sleep(45)
janela = p.getActiveWindow()
janela.maximize()
p.sleep(5)
p.click(833,105)
