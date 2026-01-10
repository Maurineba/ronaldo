from mrp.models.estoque import Estoque

from mrp.services.estoque_service import EstoqueService

class EmpresaService():
   def __init__(self):
      self.estoque = Estoque()
      self.produtos_cadastrado = []

   def cadastrar_produto(self, produto):
      self.produtos_cadastrados.append(produto)
      self.estoque.adicionar(produto, 0)

   def buscar_produto(self, codigo):
      for produto in self.produtos_cadastrados:
          if produto.codigo == codigo:
              return produto
      return None

   def excluir_produto(self, codigo):
      produto = self.buscar_produto(codigo)
      if produto:
          self.produtos_cadastrados.remove(produto)
          self.estoque.remover_do_sistema(codigo)
          return True
      return False
