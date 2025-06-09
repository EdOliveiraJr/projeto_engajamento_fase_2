from typing import List, Set

class Usuario:
    # Construtor que recebe o id do usuário
    def __init__(self, id_usuario: int):
        self.__id_usuario = id_usuario
        self.__interacoes_realizadas: List['Interacao'] = []

    # Getter e setter para id_usuario
    @property
    def id_usuario(self) -> int:
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, novo_id: int):
        self.__id_usuario = novo_id
    
    
    # Getter para interacoes_realizadas
    @property
    def interacoes_realizadas(self) -> List['Interacao']:
        return self.__interacoes_realizadas
    
    # Métodos principais
    def registrar_interacao(self, interacao: 'Interacao'):
        if interacao._id_usuario == self.__id_usuario:
            self.__interacoes_realizadas.append(interacao)

    def obter_interacoes_por_tipo(self, tipo: str) -> List['Interacao']:
        return [i for i in self.__interacoes_realizadas if i._tipo_interacao == tipo]

    def obter_conteudos_unicos_consumidos(self) -> Set['Conteudo']:
        return set(i._conteudo_associado for i in self.__interacoes_realizadas)

    def calcular_tempo_total_consumo_plataforma(self, plataforma: 'Plataforma') -> int:
        total = 0
        for i in self.__interacoes_realizadas:
            if i._plataforma_interacao == plataforma:
                total += i._watch_duration_seconds
        return total

    def plataformas_mais_frequentes(self, top_n: int) -> List['Plataforma']:
        frequencia = {}


    def __str__(self):
        return f"Usuario(id={self.__id_usuario})"

    def __repr__(self):
        return self.__str__()