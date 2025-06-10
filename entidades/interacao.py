import datetime
import Conteudo
import Plataforma

class Interacao:
    
    def __init__(self, conteudo_associado: Conteudo, plataforma_interacao: Plataforma, linha_csv: list) -> None:
        TIPOS_INTERACAO_VALIDOS = ['view_start', 'like', 'share', 'comment']
        self.__conteudo_associado: Conteudo = conteudo_associado
        self.__plataforma_interacao: Plataforma = plataforma_interacao

        self.__interacao_id: int
        self.__id_usuario: int = int(linha_csv[2])
        self.__timestamp_interacao: datetime = datetime(linha_csv[3])
        self.__tipo_interacao: str
        self.__watch_duration_seconds: int = int(linha_csv[6])
        self.__comment_text: str = linha_csv[7].strip

        if linha_csv[5] in TIPOS_INTERACAO_VALIDOS:
            self.__tipo_interacao = linha_csv[5]
        else:
            self.__tipo_interacao = "Interação inválida"

        if int(linha_csv[6]) < 0:
            self.__watch_duration_seconds = 0

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
    def timestamp_interacao(self) -> datetime:
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
