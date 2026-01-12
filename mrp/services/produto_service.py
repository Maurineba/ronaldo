from models.produto_final import ProdutoFinal
from models.empresa import Empresa
from services.estoque_service import EstoqueService
from models.item_estrutura import ItemEstrutura
from models.insumo import Insumo

class ProdutoService():

   def __init__(self, empresa: Empresa, estoque: EstoqueService):
      self.empresa = empresa
      self.estoque = estoque(empresa)

   def realizar_producao(self, produto_final, qtd_desejada):
      if not isinstance(produto_final, ProdutoFinal): #verifica se é produto final
         print("Este item não é um Produto Final")
         return


      if not produto_final.estrutura: #verifica se existe 'insumos' na estrutura
         print("Este produto não tem estrutura cadastrada")
         return

      pode_produzir = True
      for item in produto_final.estrutura:
         necessario = item.quantidade * qtd_desejada
         disponivel = self.estoque.obter_quantidade(item.insumo)
         if disponivel < necessario:
            print(f"❌ Falta Insumo: {item.insumo.nome} (Precisa: {necessario}, Tem: {disponivel})")
            pode_produzir = False

      if pode_produzir:
         for item in produto_final.estrutura:
            self.estoque.remover(item.insumo, item.quantidade * qtd_desejada)
         self.estoque.adicionar(produto_final, qtd_desejada)
         print(f"✅ Sucesso: {qtd_desejada} unidade(s) de '{produto_final.nome}' produzidas!")

      return produto_final

   def criar_estrutura(self, produto: ProdutoFinal, insumo: Insumo, quantidade: int):
      if quantidade <= 0:
         raise ValueError("Quantidade inválida")

      for item in produto.estrutura:
         if item.insumo == insumo:
            raise ValueError("Este insumo já está na estrutura do produto")

      produto.estrutura.append(ItemEstrutura(insumo, quantidade))
