from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import by
from selenium.webdriver.chrome.service. import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# install webdriver_manager

driver.get ("https://economia.uol.com.br/cotacoes/bolsas/")
# import url from pager

input_busca = driver.find_element(By.ID, "filled-normal")
input_busca.send_keys('PETR3.SA')
sleep(2)
# criar um variavel referente a busca do id no html
#e passar o parametro para a busca,no caso PETR3.SA
input_busca.send_keys(Keys.ENTER)
#para o selenium imprimir um enter no id do html
input('')