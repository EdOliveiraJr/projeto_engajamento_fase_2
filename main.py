from analise.sistema import SistemaAnaliseEngajamento

def pipeline():
    print("************ Iniciando pipeline completo ************\n")

    sistema = SistemaAnaliseEngajamento()

    # 1. Processar CSV
    print("1. Carregando e processando interações do CSV")
    sistema.processar_interacoes_do_csv("interacoes_globo.csv")
    print("-> Interações carregadas e processadas.\n")

    # 2. Listar plataformas
    print("2. Listando plataformas registradas")
    plataformas = sistema.listar_plataformas()
    for p in plataformas:
        print(f"- {p}")
    print()

    # 3. Relatório de engajamento dos conteúdos
    print("3. Gerando relatório de engajamento dos conteúdos")
    sistema.gerar_relatorio_engajamento_conteudos()
    print()

    # 4. Relatório de atividade dos usuários
    print("4. Gerando relatório de atividade dos usuários")
    sistema.gerar_relatorio_atividade_usuarios()
    print()

    # 5. Top 5 conteúdos por tempo total de consumo
    print("5. Identificando top 5 conteúdos por tempo total de consumo")
    top_conteudos = sistema.identificar_top_conteudos("tempo_total_consumo", 5)
    for i, c in enumerate(top_conteudos, 1):
        print(f"{i}. {c} - Tempo total consumido: {c.calcular_tempo_total_consumo()} segundos")
    print()

if __name__ == "__main__":
             info = '''
        Projeto Formação em Tecnologia Rede Globo
        Módulo DS-PY-19: Lógica de Programação em Python
        Fase 1: Coleta e Estruturação Inicial de Dados de Engajamento Globo
        
        Turma: 1372
        Professor: Flávio Crispim
        Equipe:
                Daniel Brambila
                Felipe Martins
                Lucas Sandes
                Malu Fazendo
                Danilo Pinho
                Edvaldo Oliveira
    '''
    print(info)
    pipeline()
    print("************ Pipeline executado com sucesso! ************")
