from mrp.services.empresa_service import EmpresaService
from mrp.services.produto_service import ProdutoService

from .interfaces.cadastrar_produto import cadastrar_produto_ui
from .interfaces.criar_estrutura import criar_estrutura_ui
from .interfaces.produzir_produto import produzir_produto_ui


empresa_service = EmpresaService()
produto_service = ProdutoService()

def menu_principal(empresa):
   while True:
      print("\n==============================")
      print("SISTEMA MRP -", empresa.nome)
      print("==============================")
      print("1 - Cadastrar Produto")
      print("2 - Criar Estrutura de Produto")
      print("3 - Produzir Produto")
      print("4 - Ver Estoque")
      print("0 - Sair")

      opcao = input("Escolha: ")

      match opcao:
         case "1":
            cadastrar_produto_ui(empresa_service)

         case "2":
            criar_estrutura_ui(empresa_service)

         case "3":
            produzir_produto_ui(empresa_service, produto_service)

         case "4":
            empresa_service.estoque.listar()

         case "0":
            print("\nEncerrando sistema... Até logo!")
            break

         case _:
            print("\nOpção inválida! Tente um número entre 0 e 4.")
