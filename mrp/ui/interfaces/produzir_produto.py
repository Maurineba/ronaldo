from services.empresa_service import EmpresaService
from services.produto_service import ProdutoService

def produzir_produto_ui(empresa):
   empresa_service = EmpresaService(empresa)
   produto_service = ProdutoService()

   print("\n--- ORDEM DE PRODUÇÃO ---")

   codigo = input("Código do Produto Final: ")

   produto = empresa_service.buscar_produto(codigo)
   if not produto:
      raise "Produto nao encontrado"

   quantidade = int(input("Quantidade a produzir: "))
   if quantidade <= 0:
      raise "Quantidade deve ser um número inteiro positivo."

   produto = produto_service.realizar_producao(produto, quantidade)

   print(f"Produto '{produto.nome}' produzido com sucesso!!!")


