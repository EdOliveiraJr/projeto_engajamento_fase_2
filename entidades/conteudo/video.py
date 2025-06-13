
from entidades.conteudo.conteudo import Conteudo

class Video(Conteudo):
    def __init__(self, id_conteudo: int, nome_conteudo: str, duracao_total_video_seg: int):
        super().__init__(id_conteudo, nome_conteudo)
        self._duracao_total_video_seg = duracao_total_video_seg

    @property
    def duracao_total_video_seg(self) -> int:
        return self._duracao_total_video_seg

    def calcular_percentual_medio_assistido(self) -> float:
        if not self._interacoes:
            return 0.0
        total_assistido = sum(i._watch_duration_seconds for i in self._interacoes)
        return (total_assistido / (len(self._interacoes) * self._duracao_total_video_seg)) * 100
