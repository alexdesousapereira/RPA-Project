# ROBO CRIA Formulário
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t

navegador = Chrome() # entra em nosso navegador
navegador.get("https://ferendum.com/pt/") # site do navegador
navegador.maximize_window() # maximiza o site
t.sleep(4) # espera carregar
navegador.find_element_by_name("titulo").send_keys("A automação é uma coisa boa? (Alex02)")
navegador.find_element_by_name("titulo").send_keys("Os robôs estão cada vez mais frequentes em nossas vidas...")
navegador.find_element_by_name("creador").send_keys("Alex Curso de RPA com Python")
navegador.find_element_by_css_selector( 'input[type="email"]').send_keys("alexdesousapereiraa@gmail.com")
navegador.find_element_by_id("op1").send_keys(" Sim! Ela me ajuda muito..")
navegador.find_element_by_id("op2").send_keys(" Sim! Ela me ajuda muito..")
navegador.find_element_by_name("config_anonimo").click()
navegador.find_element_by_name("config_priv_pub").click()
navegador.find_element_by_name("config_un_solo_voto").click()
navegador.find_element_by_name("config_aut_req").click()
navegador.find_element_by_name("accept_terms_checkbox").click()
t.sleep(5)
navegador.find_element_by_css_selector('input[value="Criar enquete"]').click()
t.sleep(5)
navegador.find_element_by_id("crear_votacion").click()
t.sleep(3)
texto = navegador.find_element_by_id("textoACopiar").text
print(texto)
navegador.quit()







