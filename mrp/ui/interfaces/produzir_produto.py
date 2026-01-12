from services.empresa_service import EmpresaService
from services.produto_service import ProdutoService

def produzir_produto_ui(empresa):
   empresa_service = EmpresaService(empresa) #instância do serviço da empresa
   produto_service = ProdutoService() #instância do serviço de produto

   print("\n--- ORDEM DE PRODUÇÃO ---")

   codigo = input("Código do Produto Final: ")

   produto = empresa_service.buscar_produto(codigo) #verifica se o produto existe
   if not produto:
      print ("Produto nao encontrado")
      return

   quantidade = int(input("Quantidade a produzir: "))
   if quantidade <= 0:
      print("Quantidade deve ser um número inteiro positivo maior que 0.")
      return

   produto = produto_service.realizar_producao(produto, quantidade) #Ronaldo :p

   print(f"Produto '{produto.nome}' produzido com sucesso!!!")


