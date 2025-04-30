from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Chrome()
navegador.get('https://www4.fazenda.sp.gov.br/DareICMS/DareAvulso')
navegador.maximize_window()

cnpj = navegador.find_element('id', 'txtCriterioConsulta')
cnpj.click()
cnpj.send_keys('44084747000140')

consultar = navegador.find_element('id', 'btnConsultar')
consultar.click()
time.sleep(8)

select_element = navegador.find_element('id', 'ddlTipoDebito')
navegador.execute_script("arguments[0].scrollIntoView({block:'center'})", select_element)
time.sleep(1)
select_element.click()
select = Select(select_element)
time.sleep(0.5)

select.select_by_value("6304")


import pandas as pd
import os
from datetime import datetime

caminho_arquivo = r"C:\Users\ickbo\Desktop\C-digoGov\Exemplo.xlsx"
dados = pd.read_excel(caminho_arquivo)
data = dados.iloc[2, 14]
data_formatada = pd.to_datetime(data).date()
dataconvertida = data_formatada.strftime("%d/%m/%Y")
time.sleep(1)

campodata = navegador.find_element('id', 'txtVencimento')
campodata.click()
campodata.send_keys(Keys.ARROW_LEFT)
campodata.send_keys(Keys.ARROW_LEFT)
campodata.send_keys(dataconvertida)

time.sleep(1)

mes_ano = data_formatada.strftime("%m/%Y")
camporef = navegador.find_element("id", 'txtReferencia')
camporef.click()
camporef.send_keys(mes_ano)

time.sleep(1)

numNota = dados.iloc[0, 1]
nomenota = dados.iloc[1, 1]
valornota = dados.iloc[0, 11]

obs = navegador.find_element("id", "txtObservacao")
obs.click()
obs.send_keys(f"ICMS ST ANTEC. NFE - nº{numNota} - {nomenota} ")

time.sleep(0.5)

campovalor = navegador.find_element("id", "txtValorCalculo")
campovalor.click()
campovalor.send_keys(f"ICMS ST PAGAR - R${valornota:.2f}")

time.sleep(2)

btngerar = navegador.find_element("id", "btnGerar")
btngerar.click()

time.sleep(2)

from selenium.webdriver.common.alert import Alert
alerta = Alert(navegador)
alerta.accept()

time.sleep(5)