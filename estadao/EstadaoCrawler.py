
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from typing import List,Dict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EstadaoCrawler:
    def __init__(self, termos_de_pesquisa: str, periodo: str):
        
        self.termos_de_pesquisa = termos_de_pesquisa
        self.periodo = periodo
        self.driver = None
        self.lista_de_links : dict = {}

    def IniciarPesquisa(self):

        op = Options()
        op.set_preference('javascript.enabled', True)
        
        self.driver = Firefox(options=op)
        self.driver.get('https://busca.estadao.com.br/?tipo_conteudo=Not%C3%ADcias&quando={}&q={}'.format(
            self.periodo,self.termos_de_pesquisa
        ))


    def CarregarTodasNoticias(self):

        carregar_mais_display = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH,
            '/html/body/section[3]/div/section[1]/div/section[2]/div')))
        carregar_mais_display=carregar_mais_display.value_of_css_property('display')

        while carregar_mais_display != 'none':

            carregar_mais_botao = self.driver.find_element(By.CLASS_NAME,'btn-mais')#
            self.driver.execute_script("arguments[0].click();", carregar_mais_botao)#

            try:
                carregar_mais_display = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME,'btn-mais')))
                carregar_mais_display=carregar_mais_display.value_of_css_property('display')
            except:
                carregar_mais_display = self.driver.find_element(By.XPATH,
                    '/html/body/section[3]/div/section[1]/div/section[2]/div')
                carregar_mais_display=carregar_mais_display.value_of_css_property('display')


    def CapturarLinks(self):
        noticias = self.driver.find_elements(By.CLASS_NAME, 'link-title')
        datas = self.driver.find_elements(By.CLASS_NAME, 'data-posts')

        indice = 0

        for noticia in noticias:
            try:
                self.lista_de_links[noticia.get_attribute('href')] = datas[indice].get_attribute('textContent')
                print(noticia.get_attribute('href'))
                #print(self.driver.find_element(By.CLASS_NAME,'data-posts').get_attribute('textContent'))

                indice += 1
            except:
                 self.driver.quit()


    def RasparNoticias(self):

        op = Options()
        op.set_preference('javascript.enabled', False)
        
        self.driver = Firefox(options=op)

        for link in self.lista_de_links:
            try:
                self.driver.get(link)
                self.CriarArquivo(link)
            except:
                pass

        self.driver.quit()
    
    def CriarArquivo(self, link):

        import re

        link_sem_caracteres_especiais = re.sub('[^0-9a-zA-Z]+', '_', link)
        print(link_sem_caracteres_especiais)

        data = self.lista_de_links[link]
        data = self.FormatarData(data)

        #exemplo 2020-02-29-https___oglobo.globo.com_mundo_erdogan-pede-putin-que-se-afaste-da-guerra-na-siria-1-24279490

        titulo = "{}-{}".format(data,link_sem_caracteres_especiais)

        paragrafos = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, 'p'))
        )

        paragrafos = self.driver.find_elements(By.TAG_NAME, 'p')
        
        texto = ''

        for paragrafo in paragrafos:

            print(paragrafo.get_attribute('textContent'),"\n")
            texto = texto + "{}\n".format(paragrafo.get_attribute('textContent'))


        try:
            arquivo = open('{}.txt'.format(titulo),'w+', encoding="utf-8")
            arquivo.write(texto)
            arquivo.close
        except:
            pass
        


    def FormatarData(self, data):

        #data = '18 de dezembro de 2019 | 06h00'

        meses = {
        'janeiro' : '01',
        'fevereiro' : '02',
        'março' : '03',
        'abril' : '04',
        'maio' :  '05',
        'junho' : '06',
        'julho' : '07',
        'agosto' : '08',
        'setembro' : '09',
        'outubro' : '10',
        'novembro' : '11',
        'dezembro' : '12'
        }

        mes_palavra = data[6:-16]
        mes_numero = 0
        for mes in meses:
            if mes_palavra == mes: 
                mes_numero = meses[mes]

        ano = data[-12:-8]
        dia = data[0:2]

        data = '{}-{}-{}'.format(ano,mes_numero,dia)

        return data
            