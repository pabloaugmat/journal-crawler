from EstadaoCrawler import EstadaoCrawler

termos_de_pesquisa = 'Turquia+imigrantes'
periodo = {
    'inicio' : '01.04.2019',
     'fim' : '03.07.2021'
     }
periodo = '{}%2F{}%2F{}-{}%2F{}%2F{}'.format(periodo['inicio'][0:2],periodo['inicio'][3:5],periodo['inicio'][6:],
                                             periodo['fim'][0:2],periodo['fim'][3:5],periodo['fim'][6:])


crawler = EstadaoCrawler(termos_de_pesquisa, periodo)
crawler.IniciarPesquisa()
crawler.CarregarTodasNoticias()
crawler.CapturarLinks()
crawler.RasparNoticias()