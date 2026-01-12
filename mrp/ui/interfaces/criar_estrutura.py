from models.insumo import Insumo
from services.empresa_service import EmpresaService
from services.produto_service import ProdutoService

def criar_estrutura_ui(empresa):
   empresa_service = EmpresaService(empresa)
   produto_service = ProdutoService()

   print("\n--- CONFIGURAR ESTRUTURA ---")

   codigo_produto = input("Código do Produto: ")

   produto = empresa_service.buscar_produto(codigo_produto)
   if not produto:
      print("Produto não encontrado")
      return

   if isinstance(produto, Insumo):
      produto.eh_composto = True

   codigo_componente = input("Código do Componente: ")

   componente = empresa_service.buscar_produto(codigo_componente)
   if not componente:
      print("Componente não encontrado")
      return

   try:
      qtd = int(input("Quantidade do componente por produto: "))
      produto_service.criar_estrutura(produto, componente, qtd)
      print("Componente adicionado com sucesso.")
   except ValueError as e:
      print(f"Erro: {e}")
