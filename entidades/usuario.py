from typing import Set

from entidades import *


class Usuario:
    # Construtor que recebe o id do usu�rio
    def __init__(self, id_usuario: int):
        self.__id_usuario = id_usuario
        self._interacoes_realizadas: list['Interacao'] = []

    # Getter e setter para id_usuario
    @property
    def id_usuario(self) -> int:
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, novo_id: int):
        self.__id_usuario = novo_id
    
    # Getter para interacoes_realizadas
    @property
    def interacoes_realizadas(self) -> list['Interacao']:
        return self._interacoes_realizadas
    
    # M�todos principais
    def registrar_interacao(self, interacao: 'Interacao'):
        # if interacao.id_usuario == self.__id_usuario:
        self._interacoes_realizadas.append(interacao)

    def obter_interacoes_por_tipo(self, tipo: str) -> list['Interacao']:
        if tipo not in ['view_start', 'like', 'share', 'comment']:
            raise ValueError(f"Tipo de interação inválido: {tipo}. Deve ser um dos: 'view_start', 'like', 'share', 'comment'.")
        if not self._interacoes_realizadas:
            raise ValueError("Nenhuma interação registrada para este usuário.")
        
        return list(
            filter(lambda interacao: interacao.tipo_interacao == tipo, self._interacoes_realizadas)
        )

    def obter_conteudos_unicos_consumidos(self) -> Set['Conteudo']:
        if not self._interacoes_realizadas:
            raise ValueError("Nenhuma interação registrada para este usuário.")
        
        return set(
            interacao.conteudo_associado.id_conteudo for interacao in self._interacoes_realizadas
        )

    def calcular_tempo_total_consumo_plataforma(self, plataforma: 'Plataforma') -> int:
        
        tempo_total = 0

        for interacao in self._interacoes_realizadas:
            if interacao.plataforma_interacao == plataforma:
                tempo_total += interacao._watch_duration_seconds

        return tempo_total

    def plataformas_mais_frequentes(self, top_n=3) -> list:
        if not self._interacoes_realizadas:
            raise ValueError("Nenhuma interação registrada para este usuário.")
        if top_n <= 0:
            raise ValueError("O valor de top_n deve ser maior que zero.")
        if not isinstance(top_n, int):
            raise TypeError("O valor de top_n deve ser um inteiro.")
        if top_n > len(self._interacoes_realizadas):
            raise ValueError("O valor de top_n não pode ser maior que o número total de interações registradas.")
        if not isinstance(top_n, int):
            raise TypeError("O valor de top_n deve ser um inteiro.")

                
        
        frequencia = {}
        
        for interacao in self._interacoes_realizadas:
            plataforma = interacao.plataforma_interacao
            if plataforma in frequencia:
                frequencia[plataforma] += 1
            else:
                frequencia[plataforma] = 1
                lista_frequencias = []
                plataformas_ordenadas = []  
                
                for plataforma in frequencia:
                    lista_frequencias.append((plataforma, frequencia[plataforma]))
                    n = len(lista_frequencias)
                    
                    for i in range(n):
                        for j in range(0, n - i - 1):
                            if lista_frequencias[j][1] < lista_frequencias[j + 1][1]:
                                lista_frequencias[j], lista_frequencias[j + 1] = lista_frequencias[j + 1], lista_frequencias[j]
                                
                                
                                for i in range(min(top_n, len(lista_frequencias))):
                                    plataformas_ordenadas.append(lista_frequencias[i][0])
                                    
                return plataformas_ordenadas

    def __str__(self):
        return f"Usuario(id={self.__id_usuario})"

    def __repr__(self):
        return self.__str__()

