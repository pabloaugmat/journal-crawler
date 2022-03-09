from EstadaoCrawler import EstadaoCrawler

termos_de_pesquisa = 'desemprego'
periodo = {
    'inicio' : '01.06.2021',
     'fim' : '01.02.2022'
     }
periodo = '{}%2F{}%2F{}-{}%2F{}%2F{}'.format(periodo['inicio'][0:2],periodo['inicio'][3:5],periodo['inicio'][6:],
                                             periodo['fim'][0:2],periodo['fim'][3:5],periodo['fim'][6:])


crawler = EstadaoCrawler(termos_de_pesquisa, periodo)
crawler.IniciarPesquisa()
crawler.CarregarTodasNoticias()
crawler.CapturarLinks()
crawler.RasparNoticias()