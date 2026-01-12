from .produto import Produto

class ProdutoFinal(Produto):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.estrutura = []  # Lista de objetos ItemEstrutura