
from entidades.conteudo.conteudo import Conteudo

class Artigo(Conteudo):
    def __init__(self, id_conteudo: int, nome_conteudo: str, tempo_leitura_estimado_seg: int):
        super().__init__(id_conteudo, nome_conteudo)
        self._tempo_leitura_estimado_seg = tempo_leitura_estimado_seg
