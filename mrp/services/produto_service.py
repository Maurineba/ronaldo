from models.produto_final import ProdutoFinal
from models.item_estrutura import ItemEstrutura
from models.insumo import Insumo

class ProdutoService():
   def realizar_producao(self, produto_final, qtd_desejada, estoque):
      if not isinstance(produto_final, ProdutoFinal):
         raise TypeError("Este item não é um Produto Final")


      if not produto_final.estrutura:
         raise ValueError("Este produto não tem estrutura cadastrada")

      pode_produzir = True
      for item in produto_final.estrutura:
         necessario = item.quantidade * qtd_desejada
         disponivel = estoque.obter_quantidade(item.insumo)
         if disponivel < necessario:
            print(f"❌ Falta Insumo: {item.insumo.nome} (Precisa: {necessario}, Tem: {disponivel})")
            pode_produzir = False

      if pode_produzir:
         for item in produto_final.estrutura:
            estoque.remover(item.insumo, item.quantidade * qtd_desejada)
         estoque.adicionar(produto_final, qtd_desejada)
         print(f"✅ Sucesso: {qtd_desejada} unidade(s) de '{produto_final.nome}' produzidas!")

      return produto_final

   def criar_estrutura(self, produto: ProdutoFinal, insumo: Insumo, quantidade: int):
      if quantidade <= 0:
         raise ValueError("Quantidade inválida")

      for item in produto.estrutura:
         if item.insumo == insumo:
            raise ValueError("Este insumo já está na estrutura do produto")

      produto.estrutura.append(ItemEstrutura(insumo, quantidade))
