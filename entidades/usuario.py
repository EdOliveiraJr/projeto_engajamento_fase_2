from typing import List, Set
from entidades.interacao import Interacao   
from entidades.conteudo import Conteudo
from entidades.plataforma import Plataforma

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
        
        resultado = []
        for interacao in self.__interacoes_realizadas:
            if interacao._tipo_interacao == tipo:
                resultado.append(interacao)
                return resultado

    def obter_conteudos_unicos_consumidos(self) -> Set['Conteudo']:
        
        conteudos_ids = set()
        
        for interacao in self.__interacoes_realizadas:
            conteudos_ids.add(interacao._id_conteudo)
            return conteudos_ids

    def calcular_tempo_total_consumo_plataforma(self, plataforma: 'Plataforma') -> int:
        
        total = 0
        
        for interacao in self.__interacoes_realizadas:
            if interacao._plataforma_interacao == plataforma:
                duracao = interacao._watch_duration_seconds
                total = total + duracao
                return total

    def plataformas_mais_frequentes(self, top_n: int) -> List['Plataforma']:
        
        frequencia = {}
        
        for interacao in self.__interacoes_realizadas:
            
            plataforma = interacao._plataforma_interacao
            
            if plataforma in frequencia:
                frequencia[plataforma] += 1
                
            else:
                frequencia[plataforma] = 1
                
            plataformas_ordenadas = []
            
            while len(plataformas_ordenadas) < top_n and len(frequencia) > 0:
                
                mais_frequente = None
                maior_contagem = -1
                
                for plataforma in frequencia:
                    
                    if frequencia[plataforma] > maior_contagem:
                        maior_contagem = frequencia[plataforma]
                        if mais_frequente is not None:
                            plataformas_ordenadas.append(mais_frequente)
                            del frequencia[mais_frequente]
                           
                            return plataformas_ordenadas


    def __str__(self):
        return f"Usuario(id={self.__id_usuario})"

    def __repr__(self):
        return self.__str__()