
from os import replace
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.support.relative_locator import with_tag_name
from typing import Dict,List


class DWCrawler:
    def __init__(self,termos_de_pesquisa: str,  periodo: dict):
        
        self.termos_de_pesquisa = termos_de_pesquisa
        self.results_counter: str = '999'
        self.periodo = periodo
        self.driver = Firefox()
        self.lista_de_links: list = []

    def IniciarPesquisa(self):

        url = ("https://www.dw.com/search/?languageCode=pt-BR&item={0}&searchNavigationId=7111-2199-30899&from={2}&to={3}&sort=DATE&resultsCounter={1}"
            .format(self.termos_de_pesquisa,
                    self.results_counter,
                    self.periodo['inicio'],
                    self.periodo['fim']))

        self.driver.get(url)

    def CapturarLinks(self):

        resultados_da_pesquisa = self.driver.find_element_by_class_name('searchResults')
        resultados = resultados_da_pesquisa.find_elements_by_tag_name('a')

        for resultado in resultados:

            if(resultado.get_attribute('href') == ''):
                continue

            #print(resultado.get_attribute('href'))
            self.lista_de_links.append(resultado.get_attribute('href'))

    def RasparNoticias(self):

        for link in self.lista_de_links:
            
            self.driver.get(link)
            self.CriarArquivo(link)

    def CriarArquivo(self, link):
        
        import re

        link_sem_caracteres_especiais = re.sub('[^0-9a-zA-Z]+', '_', link)
         
        print(link_sem_caracteres_especiais)

        data = self.driver.find_element_by_class_name('smallList')
        data = data.find_element_by_tag_name('li').get_attribute('textContent')
        data = data[4:]
        print(data)

        texto = self.driver.find_element_by_class_name('group')
        texto = texto.find_element_by_class_name('longText')
        texto_descartavel = texto.find_element_by_class_name('longText').get_attribute('textContent')
        texto = texto.get_attribute('textContent')
        texto = texto[0 : texto.find(texto_descartavel)]#TODO usar replace aqui
        
        print(texto)

        #input("APERTE ENTER PARA CONTINUAR")