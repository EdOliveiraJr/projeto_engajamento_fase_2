from analise import Sistema

if __name__ == '__main__':
	sistema = Sistema()
	sistema.processar_interacoes_do_csv('interacoes_globo.csv')
	sistema.cadastrar_plataforma('interacoes_globo.csv')