from analise import Sistema

def pipeline():
    print("************ Iniciando pipeline completo ************\n")

    sistema = Sistema()

    # 1. Processar CSV
    print("1. Carregando e processando interações do CSV")
    sistema.processar_interacoes_do_csv("interacoes_globo.csv")
    print("-> Interações carregadas e processadas.\n")

    # 2. Listar plataformas
    print("2. Listando plataformas registradas")
    plataformas = sistema.listar_plataformas()
    for p in plataformas:
        print(f"- {p}")
    print('\n ******************************************\n')
    
    # 3. Relatório de engajamento dos conteúdos
    print("3. Gerando relatório de engajamento dos conteúdos")
    sistema.gerar_relatorio_engajamento_conteudos()
    print('\n ******************************************\n')

    # 4. Relatório de atividade dos usuários
    print("4. Gerando relatório de atividade dos usuários")
    sistema.gerar_relatorio_atividade_usuarios()
    print('\n ******************************************\n')

    print("5. Relatório de métricas de conteúdos")
    print("Métrica - Total total de consumo")
    sistema.identificar_top_conteudos('tempo_total_consumo')
    print()
    print("Métrica - Média de tempo de consumo")
    sistema.identificar_top_conteudos('media_tempo_consumo')
    print()


if __name__ == "__main__":
             info = '''
        Projeto Formação em Tecnologia Rede Globo
        Fase 2: Análise de Engajamento de Mídias Globo com POO
        
        Turma: 1372
        Professor: Bruno e Maurício
        Equipe:
                Edvaldo Oliveira
                Daniel Brambila
                Malu Fazendo
                Lucas Sandes
                Danilo Pinho
                Felipe Martins
    '''
print(info)
pipeline()
print("************ Pipeline executado com sucesso! ************")
