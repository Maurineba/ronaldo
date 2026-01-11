from models.estoque import Estoque
from models.empresa import Empresa
from models.produto import Produto


class EmpresaService():
   def __init__(self, empresa: Empresa):
      self.empresa = empresa
      self.estoque = Estoque()
      self.produtos_cadastrado = []

   def cadastrar_produto(self, produto: Produto):
      self.empresa.produtos_cadastrados.append({"produto":produto.nome, "codigo":produto.codigo})
      if self.empresa.produtos_cadastrados[-1]["codigo"] == produto.codigo and self.empresa.produtos_cadastrados[-1]["produto"] == produto.nome:
          return True
      return False


   def buscar_produto(self, codigo):
      for produto in self.empresa.produtos_cadastrados:
          if produto["codigo"] == codigo:
              return produto
      return None

   def excluir_produto(self, codigo):
      produto = self.buscar_produto(codigo)
      if produto:
          self.produtos_cadastrados.remove(produto)
          self.estoque.remover_do_sistema(codigo)
          return True
      return False

   def listar_produtos(self):
      print("\n--- PRODUTOS CADASTRADOS ---")

      if not self.empresa.produtos_cadastrados: #verifica se a lista está vazia
         print("Nenhum produto cadastrado.")
         pass

      for produto in self.empresa.produtos_cadastrados: #se a lista não estiver vazia, percorre e imprime os produtos
         print(f"Código: {produto['codigo']} | Nome: {produto['produto']}")