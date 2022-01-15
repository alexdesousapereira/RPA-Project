import pyautogui as p
# p.moveTo(38,442, duration = 1) # move o mouse
# p.click(38,442) # move e 1 click
# p.sleep(2) # tempo executar código
# print(p.position()) # posição ícone

# Robo 01
def BotRobo01():
    p.FAILSAFE = False # caso tenha de algum erro o robo para. obs: obrigatorio para biblioteca pyautogui
    p.hotkey('win', 'r') # executa uma tecla de atalho
    p.sleep(2) # tempo executa código
    p.typewrite('notepad') # escreve dentro do meu painel selecionado em azul
    p.sleep(2) # tempo executa código
    p.press('enter') # executa a tecla dentro do painel selecionado
    p.sleep(1)
    p.typewrite('Oi!| Eu sou um Bot |')  # escreve dentro do meu painel selecionado em azul
    p.sleep(2)
    valor = p.getActiveWindow() # indentifica a janela aberta do windows
    valor.close()
    p.press('right') # seleciona a tecla da direita do teclado
    p.sleep(2)
    p.press('enter')
BotRobo01()