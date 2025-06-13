import datetime
from entidades import Conteudo
from entidades import Plataforma

class Interacao:

    def __init__(self, conteudo_associado: Conteudo, plataforma_interacao: Plataforma, linha_csv: dict) -> None:
        TIPOS_INTERACAO_VALIDOS = ['view_start', 'like', 'share', 'comment']
        self.__conteudo_associado: Conteudo = conteudo_associado
        self.__plataforma_interacao: Plataforma = plataforma_interacao

        self.__interacao_id: int = int(linha_csv['interacao_id']) if 'interacao_id' in linha_csv else -1
        self.__id_usuario: int = int(linha_csv['id_usuario'])
        self.__timestamp_interacao: datetime.datetime = datetime.datetime.strptime(
            linha_csv['timestamp_interacao'], "%Y-%m-%d %H:%M:%S"
        )
        self.__watch_duration_seconds: int = int(linha_csv['watch_duration_seconds'])
        self.__comment_text: str = linha_csv.get('comment_text', '').strip()

        if linha_csv['tipo_interacao'] in TIPOS_INTERACAO_VALIDOS:
            self.__tipo_interacao = linha_csv['tipo_interacao']
        else:
            self.__tipo_interacao = "Interação inválida"

        if self.__watch_duration_seconds < 0:
            self.__watch_duration_seconds = 0

    def __str__(self):
        return f"""Conteúdo associado: {self.conteudo_associado}
        Plataforma de interação: {self.plataforma_interacao}
        Interação ID: {self.interacao_id}
        ID usuário: {self.id_usuario}
        Timestamp da interação: {self.timestamp_interacao}
        Tipo de interação: {self.tipo_interacao}
        Watch duration seconds: {self.watch_duration_seconds}
        Comment text: {self.comment_text}
        """

    def __repr__(self):
        return self.__str__()

    @property
    def conteudo_associado(self) -> Conteudo:
        return self.__conteudo_associado

    @property
    def plataforma_interacao(self) -> Plataforma:
        return self.__plataforma_interacao

    @property
    def interacao_id(self) -> int:
        return self.__interacao_id

    @property
    def id_usuario(self) -> int:
        return self.__id_usuario

    @property
    def timestamp_interacao(self) -> datetime.datetime:
        return self.__timestamp_interacao

    @property
    def tipo_interacao(self) -> str:
        return self.__tipo_interacao

    @property
    def watch_duration_seconds(self) -> int:
        return self.__watch_duration_seconds

    @property
    def comment_text(self) -> str:
        return self.__comment_text