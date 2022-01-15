from selenium.webdriver import Chrome
import time as t
navegador = Chrome() # entra em nosso navegador
navegador.get("https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login") # site do navegador

navegador.maximize_window()
t.sleep(3) # tempo de espera
navegador.find_element_by_xpath("//map/area[2]").click() # acessa designer gráfico
t.sleep(3) # tempo de espera
navegador.find_element_by_name("ExpressaoPesquisa").send_keys("03768202000176")# coloca o cpf
t.sleep(1) # tempo de espera
navegador.find_element_by_xpath("//select[2]/option[4]").click() # seleciona o cpf
t.sleep(2) # tempo de espera
navegador.find_element_by_css_selector('input[type="submit"]').click()
navegador.quit() # fecha o navegador


