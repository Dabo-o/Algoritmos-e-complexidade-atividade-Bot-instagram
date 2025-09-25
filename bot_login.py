from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json

USER = ""
PASS = ""
TIMEOUT = 20

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, TIMEOUT)

try:
    driver.get("https://www.instagram.com/accounts/login/")

    username_el = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_el = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    username_el.clear()
    username_el.send_keys(USER)

    time.sleep(5)

    password_el.clear()
    password_el.send_keys(PASS)

    time.sleep(1)

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    search_button_locator = (By.XPATH, "//*[@aria-label='Pesquisa']")

    wait = WebDriverWait(driver, 10)
    search_button = wait.until(EC.element_to_be_clickable(search_button_locator))

    search_button.click()
    
    pesquisar = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Entrada da pesquisa']")))
    pesquisar.clear()
    pesquisar.send_keys("computacaounifavip_")

    time.sleep(5)

    profile_link_locator = (By.XPATH, "//span[text()='computacaounifavip_']")

    wait = WebDriverWait(driver, 5)
    profile_link = wait.until(EC.element_to_be_clickable(profile_link_locator))

    profile_link.click()

    time.sleep(3)

    dados_completos = {}

    wait = WebDriverWait(driver, 10)

    descricao_locator = (By.XPATH, "//div[text()='Criador(a) de conteúdo digital']")
    descricao_element = wait.until(EC.presence_of_element_located(descricao_locator))
    
    texto_descricao = descricao_element.text
    dados_completos['descricao'] = texto_descricao

    time.sleep(3)

    descricao2_locator = (By.XPATH, "//span[text()='CC e ADS - UNIFAVIP']")
    descricao2_element = wait.until(EC.presence_of_element_located(descricao2_locator))
    
    texto_descricao2 = descricao2_element.text
    dados_completos['descricao2'] = texto_descricao2

    perfil_locator = (By.XPATH, "//span[contains(., 'Perfil oficial dos cursos:')]")
    perfil_container = wait.until(EC.presence_of_element_located(perfil_locator))
    
    raw_text_perfil = perfil_container.text
    
    lista_perfil = [linha.strip() for linha in raw_text_perfil.split('\n') if linha.strip()]
    
    dados_completos['informacoes_adicionais'] = lista_perfil
    print("Informações do perfil encontradas e processadas.")

    link_locator = (By.XPATH, "//div[text()='linktr.ee/computacaounifavip']")
    link_element = wait.until(EC.presence_of_element_located(link_locator))
    
    texto_link = link_element.text
    dados_completos['link'] = texto_link

    print("\n--- Dados Completos a serem salvos ---")
    print(dados_completos)
    print("--------------------------------------\n")

    with open('dados_completos.json', 'w', encoding='utf-8') as json_file:
        json.dump(dados_completos, json_file, ensure_ascii=False, indent=4)

    print("✅ Arquivo 'dados_completos.json' foi criado com sucesso!")

finally:
    time.sleep(20)
    driver.quit()