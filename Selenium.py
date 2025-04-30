from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#Abrir o navegador

navegador = webdriver.Chrome()

#Abrir um site
navegador.get('https://www4.fazenda.sp.gov.br/DareICMS/DareAvulso')

#Deixar em tela cheia
navegador.maximize_window()

# Selecionar um elemento na tela
cnpj = navegador.find_element('id', 'txtCriterioConsulta')

#clicar em um elemento

cnpj.click()

#encontrar varios elementos
#lista_botoes = navegador.find_element('class name', 'form-control')

#for botao in lista_botoes:
 #   if 'cnpj' in botao.text:
  #      botao.click()
  #      break


#Selecionar aba
#aba = navegador.window_handles
#navegador.switch_to.window(aba[0])

#Escrever em um campo/formulario
#observacao = navegador.find_element('id', 'txtObservacao')
cnpj.send_keys('44084747000140')

consultar = navegador.find_element('id', 'btnConsultar')
consultar.click()

#Colocar elemento na tela
#navegador.execute_script("arguments[0].scrollIntoView({block:'center'})", botaoqueroclicar)
#botaoqueroclicar = navegador.find_element('id', 'btnConsultar')

#Esperar o carregamento de algo
#Opçao 1
#time.sleep(3)

#Opçao 2, espera dinamica
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


time.sleep(8)
select_element = navegador.find_element('id', 'ddlTipoDebito')
navegador.execute_script("arguments[0].scrollIntoView({block:'center'})", select_element)
time.sleep(2)
select_element.click()
select = Select(select_element)
time.sleep(3)

select.select_by_value("6304")


import pandas as pd
import os
from datetime import datetime


dados = pd.read_excel("Exemplo.xlsx", engine="openpyxl")
data = dados.iloc[2, 14]
print("Data:", data)
data_formatada = pd.to_datetime(data).date()
dataconvertida = data_formatada.strftime("%d/%m/%Y")
print("Data formatada:", dataconvertida)

time.sleep(2)

campodata = navegador.find_element('id', 'txtVencimento')
campodata.click()

campodata.send_keys(dataconvertida)

time.sleep(3)