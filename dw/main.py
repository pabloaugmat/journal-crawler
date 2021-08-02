# coding=utf8
#TODO:1 - abrir a página de busca com os termos e datas desejados
#exemplos de termos:
#Turquia e imigrantes
#Turquia e refugiados
#TODO:2 - varrer a página de busca mostrando todos os links
#TODO:3 - chegar até o fim das páginas de busca (botão carregar mais ou pŕoxima página)
#TODO:4 - abrir cada link do item 2
#TODO:4.1 - conseguir pegar a periodo da matéria
#TODO:4.2 - conseguir pegar o texto da matéria
#TODO:4.3 - salvar a matéria em um arquivo com nome periodo+link (link sem caracteres especiais) 
#exemplo 2020-02-29-https___oglobo.globo.com_mundo_erdogan-pede-putin-que-se-afaste-da-guerra-na-siria-1-24279490

from DWCrawler import DWCrawler

termos_de_pesquisa = 'Turquia+imigrantes'
periodo = {
    'inicio' : '01.04.2019',
     'fim' : '03.07.2021'
     }

crawler = DWCrawler(termos_de_pesquisa, periodo)
crawler.IniciarPesquisa()
crawler.CapturarLinks()
crawler.RasparNoticias()
