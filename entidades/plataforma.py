class Plataforma:
    

    def __init__(self, nome_plataforma: str, id_plataforma: int = None):
        """
        Inicializa um objeto Plataforma.

        Args:
            nome_plataforma (str): O nome da plataforma. Não pode ser vazio. 
            id_plataforma (int): O ID único da plataforma. Defaults to None.
        """
        # A atribuição é feita através da property para garantir a validação.
        self.nome_plataforma = nome_plataforma
        # O ID não possui validação específica, então é atribuído diretamente.
        self._id_plataforma = id_plataforma

    @property
    def id_plataforma(self) -> int:
        """
        Retorna o ID da plataforma.
        Este atributo é "read-only" após a instanciação.
        """
        return self._id_plataforma

    @property
    def nome_plataforma(self) -> str:
        """Retorna o nome da plataforma."""
        return self._nome_plataforma

    @nome_plataforma.setter
    def nome_plataforma(self, nome: str):
        """
        Define ou atualiza o nome da plataforma, com validação. 

        Garante que o nome seja uma string não vazia.

        Args:
            nome (str): O novo nome para a plataforma.

        Raises:
            ValueError: Se o nome for inválido (None, não-string ou vazio).
        """
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome da plataforma não pode ser nulo ou vazio.")
        self._nome_plataforma = nome.strip()

    def __str__(self) -> str:
        """
        Retorna uma representação legível (string) da plataforma, que é o seu nome. 
        """
        return self.nome_plataforma

    def __repr__(self) -> str:
        """
        Retorna uma representação "oficial" do objeto.
        Exemplo: Plataforma(nome='Globoplay') 
        """
        return f"Plataforma(nome='{self.nome_plataforma}')"

    def __eq__(self, other) -> bool:
        """
        Verifica se duas instâncias de Plataforma são iguais. 

        A igualdade é determinada pelo nome da plataforma, ignorando diferenças de maiúsculas/minúsculas.
        """
        if not isinstance(other, Plataforma):
            return NotImplemented
        return self.nome_plataforma.lower() == other.nome_plataforma.lower()

    def __hash__(self) -> int:
        """
        Retorna o hash do objeto, baseado no nome da plataforma. 
        permite que instâncias de Plataforma sejam usadas como chaves em dicionários ou em conjuntos.
        """
        return hash(self.nome_plataforma.lower())