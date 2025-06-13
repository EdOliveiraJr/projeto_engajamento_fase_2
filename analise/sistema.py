import csv
from entidades import *

class SistemaAnaliseEngajamento:
    VERSAO_ANALISE = "2.0"
    id_plataforma_atual = 0

    def __init__(self):
        self.__plataformas_registradas  = {}
        self.__conteudos_registrados  = {}
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
            print(linha['nome_conteudo'])

            if  self.obter_plataforma(linha['plataforma']) is None:
                self.cadastrar_plataforma(linha['plataforma'])
                       
            if self.__conteudos_registrados.get(linha['id_conteudo']) is None:
                if('podcast' in linha['nome_conteudo'].lower()):
                    podcast = Podcast(linha['id_conteudo'], linha['nome_conteudo'], linha['watch_duration_seconds'])
                    self.__conteudos_registrados.append(podcast) 

                if('video' in linha['nome_conteudo'].lower()):
                    video = Video(linha['id_conteudo'], linha['nome_conteudo'], linha['watch_duration_seconds'])
                    self.__conteudos_registrados.append(video)

                if('artigo' in linha['nome_conteudo'].lower()):
                    artigo = Artigo(linha['id_conteudo'], linha['nome_conteudo'], linha['watch_duration_seconds'])
                    self.__conteudos_registrados.append(artigo)

            if self.__usuarios_registrados.get(linha['id_usuario']) is None:
                usuario = Usuario(linha['id_usuario'], linha['nome_usuario'])
                self.__usuarios_registrados[linha['id_usuario']] = usuario

            try:
                conteudo = self.__conteudos_registrados[linha['id_conteudo']]
                plataforma = self.obter_plataforma(linha['plataforma'])
                usuario = self.__usuarios_registrados[linha['id_usuario']]
                
                interacao = Interacao(conteudo, plataforma, linha)
                conteudo.adicionar_interacao(interacao)
                plataforma.adicionar_interacao(interacao)
                usuario.adicionar_interacao(interacao)
            except ValueError as e:
                print(f"Erro ao processar interação: {e}")
                

    def gerar_relatorio_engajamento_conteudos(self, top_n=None):
        for conteudo in self.__conteudos_registrados.values():
            print(f"Conteúdo: {conteudo}")
            print(f"  Total de Interações: {conteudo.calcular_total_interacoes_engajamento()}")
            print(f"  Comentários: {conteudo.listar_comentarios()}")

    def gerar_relatorio_atividade_usuarios(self, top_n=None):
        for usuario in self.__usuarios_registrados.values():
            print(f"Usuário: {usuario}")
            print(f"  Plataformas mais usadas: {usuario.plataformas_mais_frequentes()}")

    def identificar_top_conteudos(self, metrica, n):
        if metrica == 'tempo_total_consumo':
            return sorted(
                self.__conteudos_registrados.values(),
                key=lambda c: c.calcular_tempo_total_consumo(),
                reverse=True
            )[:n]
