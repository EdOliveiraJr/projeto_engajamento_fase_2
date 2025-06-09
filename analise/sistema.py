from entidades.conteudo import Conteudo
from entidades.plataforma import Plataforma
from entidades.usuario import Usuario
from entidades.interacao import Interacao

class SistemaAnaliseEngajamento:  
  def __init__(self):
    VERSAO_ANALISE = "2.0"
    # Dicionário mapeando nome_plataforma (str) para objetos Plataforma. Usado para o "CRUD" em memória.
    self.__plataformas_registradas: dict['nome_plataforma' : str, 'Plataforma'] = {} 
    #  Dicionário mapeando id_conteudo (int) para objetos Conteudo (ou suas subclasses).
    self.__conteudos_registrados: dict['id_conteudo' : int, 'Conteudo'] = {}
    #  Dicionário mapeando id_usuario (int) para objetos Usuario.
    self.__usuarios_registrados:  dict['id_usuario' : int , 'Usuario'] = {}
    # Para gerar IDs para novas plataformas.
    self.__proximo_id_plataforma : int = 1
    
    # cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma: Cria e adiciona uma nova plataforma se não existir. Retorna o objeto Plataforma.
    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
      if nome_plataforma not in self.__plataformas_registradas:
        plataforma = Plataforma(nome_plataforma)
        self.__plataformas_registradas[nome_plataforma] = plataforma
        return plataforma
      else:
        raise ValueError(f"Plataforma '{nome_plataforma}' já cadastrada.")
    # obter_plataforma(self, nome_plataforma: str) -> Plataforma: Retorna uma plataforma pelo nome. Se não existir, pode cadastrá-la.
    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
      if nome_plataforma in self.__plataformas_registradas:
        return self.__plataformas_registradas[nome_plataforma]
      else:
        return self.cadastrar_plataforma(nome_plataforma)
    #  listar_plataformas(self) -> list: Retorna uma lista de todas as plataformas cadastradas.
    def listar_plataformas(self) -> list[Plataforma]:
      return list(self.__plataformas_registradas.values())
    
    # _carregar_interacoes_csv(self, caminho_arquivo: str) -> list: Carrega dados brutos do CSV.
    def _carregar_interacoes_csv(self, caminho_arquivo: str) -> list[dict]:
      import csv
      interacoes = []
      with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
          interacoes.append(row)
      return interacoes
    
    # 4.2. processar_interacoes_do_csv(self, caminho_arquivo: str):
    # 4.2.2. Ao invés de gerar um dicionario com os dados brutos, será adaptado para armazenar os dados como objetos da classe adequada:
    def processar_interacoes_do_csv(self, caminho_arquivo: str):
      # 4.2.1. Chama _carregar_interacoes_csv.
      interacoes = self._carregar_interacoes_csv(caminho_arquivo)

      for interacao in interacoes:
        # 4.2.3. Obtém/Cria o objeto Plataforma.
        nome_plataforma = interacao['plataforma']
        plataforma = self.obter_plataforma(nome_plataforma)
        
        # 4.2.4. Obtém/Cria o objeto Conteudo.
        titulo_conteudo = interacao['titulo_conteudo']
        conteudo = plataforma.conteudos_registrados.get(titulo_conteudo)
        if not conteudo:
          conteudo = Conteudo(titulo=titulo_conteudo, descricao=interacao['descricao'], conteudo=interacao['conteudo'])
          plataforma.conteudos_registrados[titulo_conteudo] = conteudo
        
        # 4.2.5. Obtém/Cria o objeto Usuario.
        id_usuario = int(interacao['id_usuario'])
        usuario = plataforma.usuarios_registrados.get(id_usuario)
        if not usuario:
          usuario = Usuario(id_usuario=id_usuario, nombre=interacao['nombre'], email=interacao['email'], fecha_registro=interacao['fecha_registro'])
          plataforma.usuarios_registrados[id_usuario] = usuario
        
        # 4.2.6. Tenta instanciar Interacao, lidando com ValueError para validações.
        try:
          id_interacao = int(interacao['id_interacao'])
          tipo_interacao = interacao['tipo_interacao']
          data_interacao = interacao['data_interacao']
          
          nova_interacao = Interacao(id_interacao=id_interacao, id_usuario=id_usuario, id_produto=titulo_conteudo, tipo_interacao=tipo_interacao, data_interacao=data_interacao)
          
          # 4.2.7. Se Interação válida, registra-a nos objetos Conteudo e Usuario.
          conteudo.interacoes.append(nova_interacao)
          usuario.interacoes.append(nova_interacao)
          
        except ValueError as e:
          print(f"Erro ao processar interação: {e}")

    # gerar_relatorio_engajamento_conteudos(self, top_n: int = None): Itera por __conteudos_registrados, usa os métodos de cada objeto Conteudo para calcular métricas e as exibe.
    def gerar_relatorio_engajamento_conteudos(self, top_n: int = None):
      relatorio = []
      for conteudo in self.__conteudos_registrados.values():
        # Aqui, assumimos que Conteudo tem métodos para calcular métricas de engajamento.
        metricas = conteudo.calcular_metricas_engajamento()
        relatorio.append({
          'titulo': conteudo.titulo,
          'metricas': metricas
        })
      # Ordena o relatório por uma métrica específica, se top_n for fornecido.
      if top_n:
        relatorio = sorted(relatorio, key=lambda x: x['metricas']['visualizacoes'], reverse=True)[:top_n]
      return relatorio
      
    # gerar_relatorio_atividade_usuarios(self, top_n:  int = None): Similar, para usuários.
    def gerar_relatorio_atividade_usuarios(self, top_n: int = None):
      relatorio = []
      for usuario in self.__usuarios_registrados.values():
        # Aqui, assumimos que Usuario tem métodos para calcular métricas de atividade.
        metricas = usuario.calcular_metricas_atividade()
        relatorio.append({
          'usuario': usuario.nombre,
          'metricas': metricas
        })
      # Ordena o relatório por uma métrica específica, se top_n for fornecido.
      if top_n:
        relatorio = sorted(relatorio, key=lambda x: x['metricas']['interacoes'], reverse=True)[:top_n]
      return relatorio

    # identificar_top_conteudos(self, metrica: str, n: int): (e.g., metrica='tempo_total_consumo').
    def identificar_top_conteudos(self, metrica: str, n: int):
      conteudos_ordenados = sorted(self.__conteudos_registrados.values(), key=lambda c: c.calcular_metricas_engajamento()[metrica], reverse=True)
      return conteudos_ordenados[:n]
    

    @classmethod
    def obter_versao(cls):
        return cls.VERSAO_ANALISE