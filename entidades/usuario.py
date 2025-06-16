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
            interacao.conteudo_associado.nome_conteudo for interacao in self._interacoes_realizadas
        )

    def calcular_tempo_total_consumo_plataforma(self, plataforma: 'Plataforma') -> int:        
        tempo_total = 0

        for interacao in self._interacoes_realizadas:
            if interacao.plataforma_interacao.id_plataforma == plataforma.id_plataforma:
                tempo_total += interacao.watch_duration_seconds

        return tempo_total

    def plataformas_mais_frequentes(self, top_n = 3 ) -> list:
        contagem = {}
        for interacao in self._interacoes_realizadas :
            plataforma_nome = interacao.plataforma_interacao.nome_plataforma
            if plataforma_nome in contagem :
                contagem[plataforma_nome] += 1
            else :
                contagem[plataforma_nome] = 1

        contagem_ordenado = dict(sorted(contagem.items(), key= lambda item: item[1], reverse = True ))

        return list(contagem_ordenado.items())[:top_n]

    def __str__(self):
        return f"Usuario(id={self.__id_usuario})"

    def __repr__(self):
        return self.__str__()

