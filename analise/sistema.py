import csv
from entidades.plataforma import Plataforma
from entidades.conteudo import Video
from entidades.usuario import Usuario
from entidades.interacao import Interacao

class SistemaAnaliseEngajamento:
    VERSAO_ANALISE = "2.0"

    def __init__(self):
        self.__plataformas_registradas = {}
        self.__conteudos_registrados = {}
        self.__usuarios_registrados = {}
        self.__proximo_id_plataforma = 1

    def cadastrar_plataforma(self, nome):
        if nome not in self.__plataformas_registradas:
            plataforma = Plataforma(nome, self.__proximo_id_plataforma)
            self.__plataformas_registradas[nome] = plataforma
            self.__proximo_id_plataforma += 1
        return self.__plataformas_registradas[nome]

    def obter_plataforma(self, nome):
        return self.__plataformas_registradas.get(nome) or self.cadastrar_plataforma(nome)

    def listar_plataformas(self):
        return list(self.__plataformas_registradas.values())

    def _carregar_interacoes_csv(self, path):
        with open(path, encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def processar_interacoes_do_csv(self, path):
        for linha in self._carregar_interacoes_csv(path):
            try:
                plataforma = self.obter_plataforma(linha['plataforma'])
                id_conteudo = int(linha['id_conteudo'])
                if id_conteudo not in self.__conteudos_registrados:
                    conteudo = Video(id_conteudo, linha['nome_conteudo'], int(linha.get('duracao_total_video_seg', 0)))
                    self.__conteudos_registrados[id_conteudo] = conteudo
                else:
                    conteudo = self.__conteudos_registrados[id_conteudo]

                id_usuario = int(linha['id_usuario'])
                usuario = self.__usuarios_registrados.setdefault(id_usuario, Usuario(id_usuario))

                interacao = Interacao(
                    interacao_id=int(linha['interacao_id']),
                    conteudo_associado=conteudo,
                    id_usuario=id_usuario,
                    timestamp_interacao=linha['timestamp_interacao'],
                    plataforma_interacao=plataforma,
                    tipo_interacao=linha['tipo_interacao'],
                    watch_duration_seconds=int(linha.get('watch_duration_seconds', 0)),
                    comment_text=linha.get('comment_text', '')
                )

                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao)
            except Exception as e:
                print(f"Erro ao processar linha: {linha}. Erro: {e}")

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
