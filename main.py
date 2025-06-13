from analise import Sistema

if __name__ == '__main__':
	sistema = Sistema()
	sistema.processar_interacoes_do_csv('interacoes_globo.csv')
	sistema.gerar_relatorio_atividade_usuarios()
	sistema.gerar_relatorio_engajamento_conteudos()
	sistema.identificar_top_conteudos()