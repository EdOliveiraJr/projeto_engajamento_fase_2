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
         
        resultado = {}
        for item in Interacao:
            idc = item['id_conteudo']
            nome = item['nome_conteudo']
            tipo = item['tipo_interacao']
            if idc not in resultado:
                resultado[idc] = {
                'nome_conteudo': nome,
                'view_start': 0,
                'like': 0,
                'share': 0,
                'comment': 0
            }
        if tipo in resultado[idc]:
            resultado[idc][tipo] += 1
        else:
            resultado[idc][tipo] = 1 
            return resultado

    def obter_conteudos_unicos_consumidos(self) -> Set['Conteudo']:
        metricas = {}
        for item in Conteudo:
            id_conteudo = item['id_conteudo']
            
            if id_conteudo not in metricas:
                metricas[id_conteudo] = {
                'nome_conteudo': item['nome_conteudo'],
                'likes': 0,
                'shares': 0,
                'comments': 0,
                'total de interações': 0
            }
        
        tipo = item['tipo_interacao']

        if tipo == 'like':
            metricas[id_conteudo]['likes'] += 1
            metricas[id_conteudo]['total de interações'] += 1
        elif tipo == 'share':
            metricas[id_conteudo]['shares'] += 1
            metricas[id_conteudo]['total de interações'] += 1
        elif tipo == 'comment':
            metricas[id_conteudo]['comments'] += 1
            metricas[id_conteudo]['total de interações'] += 1
            
            return metricas

#    def calcular_tempo_total_consumo_plataforma(self, plataforma: 'Plataforma') -> int:
#        total = 0
#        for i in self.__interacoes_realizadas:
#            if i._plataforma_interacao == plataforma:
#                total += i._watch_duration_seconds
#        return total

    def plataformas_mais_frequentes(self, top_n: int) -> List['Plataforma']:
        frequencia = {}


    def __str__(self):
        return f"Usuario(id={self.__id_usuario})"

    def __repr__(self):
        return self.__str__()