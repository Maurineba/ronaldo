from models.produto_final import ProdutoFinal
from models.produto import Produto

class ProdutoService():
   def realizar_producao(produto_final, qtd_desejada, estoque):
      if not isinstance(produto_final, ProdutoFinal):
           print("Erro: Este item não é um Produto Final.")
           return

      if not produto_final.estrutura:
         print("Erro: Este produto não tem Estrutura cadastrada.")
         return

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
