from entidades import conteudo

class Video(conteudo):
    def __init__(self, id_conteudo, nome_conteudo, linha_csv: dict):
        super().__init__(id_conteudo, nome_conteudo)
        self.__duracao_total_video_seg: int = linha_csv["watch_duration_seconds"]

    @property
    def duracao_total_video_seg(self) -> int:
        return self.__duracao_total_video_seg
    
    def calcular_percentual_medio_assistido(self):
        media_tempo = self.calcular_media_tempo_consumo()
        percentual_medio = (media_tempo / self.duracao_total_video_seg) * 100
        return percentual_medio