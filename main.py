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

    # 6. Métodos da classe Usuario
    print("6. Chamando métodos da classe Usuario")
    for usuario in sistema._SistemaAnaliseEngajamento__usuarios_registrados.values():
        print(f"\nUsuário: {usuario}")

        print("- Interações do tipo 'like':")
        for interacao in usuario.obter_interacoes_por_tipo("like"):
            print(f"  • {interacao}")

        print("- Conteúdos únicos consumidos:")
        for conteudo in usuario.obter_conteudos_unicos_consumidos():
            print(f"  • {conteudo}")

        print("- Tempo total de consumo por plataforma:")
        for plataforma in plataformas:
            tempo = usuario.calcular_tempo_total_consumo_plataforma(plataforma)
            print(f"  • {plataforma.nome_plataforma}: {tempo} segundos")

        print("- Plataformas mais frequentes:")
        for nome, quantidade in usuario.plataformas_mais_frequentes(3):
            print(f"  • {nome}: {quantidade} interações")

        print("\n--------------------------------------------------\n")

    # 7. Métodos da classe Conteudo
    print("7. Chamando métodos da classe Conteudo")
    for conteudo in sistema._SistemaAnaliseEngajamento__conteudos_registrados.values():
        print(f"\nConteúdo: {conteudo}")

        print("- Total de interações de engajamento:")
        print(f"  • {conteudo.calcular_total_interacoes_engajamento()}")

        print("- Contagem por tipo de interação:")
        contagem = conteudo.calcular_contagem_por_tipo_interacao()
        for tipo, qtd in contagem.items():
            print(f"  • {tipo}: {qtd}")

        print("- Tempo total de consumo:")
        print(f"  • {conteudo.calcular_tempo_total_consumo()} segundos")

        print("- Tempo médio de consumo:")
        print(f"  • {conteudo.calcular_media_tempo_consumo():.2f} segundos")

        print("- Comentários:")
        for comentario in conteudo.listar_comentarios():
            print(f"  • {comentario}")

        print("\n--------------------------------------------------\n")
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
