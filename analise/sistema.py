import csv
from entidades import *


class SistemaAnaliseEngajamento:
    VERSAO_ANALISE = "2.0"
    id_plataforma_atual = 0

    def __init__(self):
        self.__plataformas_registradas = {}
        self.__conteudos_registrados = {}
        self.__usuarios_registrados = {}
        self.__proximo_id_plataforma = SistemaAnaliseEngajamento.id_plataforma_atual + 1
        SistemaAnaliseEngajamento.id_plataforma_atual += 1

    def cadastrar_plataforma(self, nome):
        if nome not in self.__plataformas_registradas:
            plataforma = Plataforma(nome, self.__proximo_id_plataforma)
            self.__plataformas_registradas[nome] = plataforma
            self.__proximo_id_plataforma += 1
        return self.__plataformas_registradas[nome]

    def obter_plataforma(self, nome):
        return self.__plataformas_registradas.get(nome) or None

    def listar_plataformas(self):
        return list(self.__plataformas_registradas.values())

    def _carregar_interacoes_csv(self, path):
        with open(path, encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def processar_interacoes_do_csv(self, path):
        interacoes = self._carregar_interacoes_csv(path)
        for linha in interacoes:
            if self.obter_plataforma(linha["plataforma"]) is None:
                self.cadastrar_plataforma(linha["plataforma"])

            if self.__conteudos_registrados.get(linha["id_conteudo"]) is None:
                if linha["nome_conteudo"].lower().find("podcast"):
                    podcast = Podcast(
                        linha["id_conteudo"],
                        linha["nome_conteudo"],
                        linha["watch_duration_seconds"],
                    )
                    self.__conteudos_registrados[linha["id_conteudo"]] = podcast
                if linha["nome_conteudo"].lower().find("video"):
                    video = Video(
                        linha["id_conteudo"],
                        linha["nome_conteudo"],
                        linha["watch_duration_seconds"],
                    )
                    self.__conteudos_registrados[linha["id_conteudo"]] = video

                if linha["nome_conteudo"].lower().find("artigo"):
                    artigo = Artigo(
                        linha["id_conteudo"],
                        linha["nome_conteudo"],
                        linha["watch_duration_seconds"],
                    )
                    self.__conteudos_registrados[linha["id_conteudo"]] = artigo

            if self.__usuarios_registrados.get(linha["id_usuario"]) is None:
                usuario = Usuario(linha["id_usuario"])
                self.__usuarios_registrados[linha["id_usuario"]] = usuario

            try:
                plataforma = self.obter_plataforma(linha["plataforma"])
                conteudo = self.__conteudos_registrados.get(linha["id_conteudo"])
                usuario = self.__usuarios_registrados.get(linha["id_usuario"])

                print(plataforma, conteudo, usuario)

                interacao = Interacao(conteudo, plataforma, linha)
                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao)
            except ValueError as e:
                print(f"Erro ao processar interação: {e}")

    def gerar_relatorio_engajamento_conteudos(self):

        for conteudo in self.__conteudos_registrados.values():
            print(f"\nConteúdo: {conteudo}")
            print("- Total de interações de engajamento:")
            print(f"  • {conteudo.calcular_total_interacoes_engajamento()}")

            print("- Contagem por tipo de interação:")
            contagem = conteudo.calcular_contagem_por_tipo_interacao()
            for tipo, qtd in contagem.items():
                print(f"  • {tipo}: {qtd}")

                

    def gerar_relatorio_atividade_usuarios(self):
            print("6. Chamando métodos da classe Usuario")
            for usuario in self.__usuarios_registrados.values():
                print(f"\nUsuário: {usuario}")

                print("- Interações do tipo 'like':")
            for interacao in usuario.obter_interacoes_por_tipo("like"):
                print(f"  • {interacao}")

                print("- Conteúdos únicos consumidos:")
            for conteudo in usuario.obter_conteudos_unicos_consumidos():
                print(f"  • {conteudo}")

                print("- Tempo total de consumo por plataforma:")
            for plataforma in self.__plataformas_registradas:
                tempo = usuario.calcular_tempo_total_consumo_plataforma(plataforma)
                print(f"  • {plataforma.nome_plataforma}: {tempo} segundos")

                print("- Plataformas mais frequentes:")
            for nome, quantidade in usuario.plataformas_mais_frequentes(3):
                print(f"  • {nome}: {quantidade} interações")


    def identificar_top_conteudos(self, metrica, n=3):

        tops = int(0)

        if metrica == 'tempo_total_consumo':           
            for conteudo in self.__conteudos_registrados:
                print("- Tempo total de consumo:")
                print(f"  • {conteudo.calcular_tempo_total_consumo()} segundos")
        if metrica == 'media_tempo_consumo':
            for counteudo in self.__conteudos_registrados:
                print("- Tempo médio de consumo:")
                print(f"  • {conteudo.calcular_media_tempo_consumo():.2f} segundos")

        
      