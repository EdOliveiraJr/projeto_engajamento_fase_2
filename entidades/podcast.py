
from entidades.conteudo import Conteudo

class Podcast(Conteudo):
    def __init__(self, id_conteudo: int, nome_conteudo: str, duracao_total_episodio_seg: int):
        super().__init__(id_conteudo, nome_conteudo)
        self._duracao_total_episodio_seg = duracao_total_episodio_seg
