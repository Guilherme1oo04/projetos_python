from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def verifica(texto):
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    navegador.get("https://nilc-fakenews.herokuapp.com/")

    entrada_de_txt = navegador.find_element(By.XPATH, '//*[@id="news"]')
    entrada_de_txt.send_keys(texto)

    bt_verificar = navegador.find_element(By.XPATH, '//*[@id="send"]')
    bt_verificar.click()

    time.sleep(1)

    resultado = navegador.find_element(By.XPATH, '//*[@id="answer"]').text

    return resultado
