import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://g1.globo.com")

print("Aguardando a pagina carregar...")
time.sleep(10)

lista_dados = []

noticias = driver.find_elements(By.CSS_SELECTOR, '.feed-post-body')

print("Total de noticias encontradas: " + str(len(noticias)))

for n in noticias:
    try:
        info = {}
        titulo_el = n.find_element(By.CSS_SELECTOR, 'a.feed-post-link')
        
        titulo = titulo_el.text
        link = titulo_el.get_attribute('href')
        
        info['titulo'] = titulo
        info['link'] = link
        
        lista_dados.append(info)
    except:
        print("Erro em um dos blocos, pulando...")
        continue

driver.quit()

arquivo = 'manchetes.json'
with open(arquivo, 'w', encoding='utf-8') as f:
    json.dump(lista_dados, f, ensure_ascii=False, indent=4)

print("Scraping finalizado. Arquivo " + arquivo + " criado.")