from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configurações do navegador
options = Options()
options.add_argument("--disable-gpu")  # Desativa a GPU
options.add_experimental_option("detach", True)  # Impede que o navegador feche automaticamente

# Inicia o navegador com as opções
navegador = webdriver.Chrome(options=options)
navegador.get("https://veiculos.fipe.org.br/")
navegador.maximize_window()

# Aguarda e clica no elemento
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a/div[1]'))).click()

time.sleep(1)
#segundo :clicar e selecionar o mes de pesquisa
navegador.find_element(By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/a/div/b').click()
options_mes_ano = navegador.find_elements(By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/div/ul')
lista_mes_ano = options_mes_ano[0].find_elements(By.CSS_SELECTOR,'li')
lista_mes_ano[1].click()

#Terceiro :clicar e selecionar marca 
navegador.find_element(By.XPATH, '//*[@id="selectMarcacarro_chosen"]/a/div/b').click()
options_marca = navegador.find_elements(By.XPATH, '//*[@id="selectMarcacarro_chosen"]/div/ul')
lista_marca = options_marca[0].find_elements(By.CSS_SELECTOR,'li')
lista_marca[2].click()

#Quarto clicar e selecionar modelo 
navegador.find_element(By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/a/div/b').click()
options_modelo = navegador.find_elements(By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/div/ul')
lista_modelo = options_modelo[0].find_elements(By.CSS_SELECTOR,'li')
lista_modelo[3].click()

#Quinto : clicar e selecuonar ano/modelo 
navegador.find_element(By.XPATH, '//*[@id="selectAnocarro_chosen"]/a/div/b').click()
options_ano = navegador.find_elements(By.XPATH, '//*[@id="selectAnocarro_chosen"]/div/ul')
lista_ano = options_ano[0].find_elements(By.CSS_SELECTOR,'li')
lista_ano[0].click()
#sexto : clicar em pesquisar 
navegador.find_element(By.LINK_TEXT,'Pesquisar').click()

#Setimo: salvar os dados da tabela em um dicionarios;


