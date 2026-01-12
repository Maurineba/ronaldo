from .estoque import Estoque

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.produtos_cadastrados = []
        self.estoque = Estoque()

    def cadastrar_produto(self, produto):
        self.produtos_cadastrados.append(produto)
        self.estoque.adicionar(produto, 0)

    def buscar_produto(self, codigo):
        for p in self.produtos_cadastrados:
            if p.codigo == codigo:
                return p
        return None

    def excluir_produto(self, codigo):
        produto = self.buscar_produto(codigo)
        if produto:
            self.produtos_cadastrados.remove(produto)
            self.estoque.remover_do_sistema(codigo)
            return True
        return False