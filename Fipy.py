from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

# Configurações do navegador
options = Options()
options.add_argument("--disable-gpu")  # Desativa a GPU
options.add_experimental_option("detach", True)  # Impede que o navegador feche automaticamente

# Inicia o navegador com as opções
navegador = webdriver.Chrome(options=options)
navegador.get("https://veiculos.fipe.org.br/")
navegador.maximize_window()

# Aguarda e clica no primeiro elemento (Consulta de carros)
WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a/div[1]'))
).click()

time.sleep(1)

# **Selecionar mês de pesquisa**
navegador.find_element(By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/a/div/b').click()
options_mes_ano = navegador.find_element(By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/div/ul')
lista_mes_ano = options_mes_ano.find_elements(By.CSS_SELECTOR, 'li')
lista_mes_ano[1].click()  # Escolhe o segundo item

# **Selecionar marca**
navegador.find_element(By.XPATH, '//*[@id="selectMarcacarro_chosen"]/a/div/b').click()
options_marca = navegador.find_element(By.XPATH, '//*[@id="selectMarcacarro_chosen"]/div/ul')
lista_marca = options_marca.find_elements(By.CSS_SELECTOR, 'li')
lista_marca[0].click()  # Escolhe a primeira marca disponível

# **Selecionar modelo**
navegador.find_element(By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/a/div/b').click()
options_modelo = navegador.find_element(By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/div/ul')
lista_modelo = options_modelo.find_elements(By.CSS_SELECTOR, 'li')
lista_modelo[1].click()  # Escolhe o segundo modelo disponível

# **Selecionar ano/modelo**
navegador.find_element(By.XPATH, '//*[@id="selectAnocarro_chosen"]/a/div/b').click()
options_ano = navegador.find_element(By.XPATH, '//*[@id="selectAnocarro_chosen"]/div/ul')
lista_ano = options_ano.find_elements(By.CSS_SELECTOR, 'li')
lista_ano[0].click()  # Escolhe o primeiro ano disponível

# **Clicar em "Pesquisar"**
navegador.find_element(By.XPATH, '//*[@id="buttonPesquisarcarro"]').click()

# **Aguardar resultado da pesquisa**
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="resultadoConsultacarroFiltros"]/table/tbody'))
)

# **Extrair os dados da tabela e salvar em um dicionário**
tabela = navegador.find_element(By.XPATH, '//*[@id="resultadoConsultacarroFiltros"]/table/tbody')
linhas = tabela.find_elements(By.CSS_SELECTOR, 'td')

carro = {}

for item in range(0, len(linhas) - 1, 2):
    carro[linhas[item].text] = linhas[item + 1].text

    navegador.close()

object_json = json.dumps(carro, indent = 2, ensure_ascii = False) #Função para cria um arqui json som as informações 
with open('carro.json', 'w') as file:
    file.write(object_json)
