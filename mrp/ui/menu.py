from services.empresa_service import EmpresaService
from services.produto_service import ProdutoService
from services.estoque_service import EstoqueService
from ui.interfaces.cadastrar_produto import cadastrar_produto_ui
from ui.interfaces.criar_estrutura import criar_estrutura_ui
from ui.interfaces.produzir_produto import produzir_produto_ui


def menu_principal(empresa):
   while True:
      print("\n==============================")
      print("SISTEMA MRP -", empresa.nome)
      print("==============================")
      print("1 - Cadastrar Produto")
      print("2 - Criar Estrutura de Produto")
      print("3 - Produzir Produto")
      print("4 - Ver Estoque")
      print("5 - Listar Produtos Cadastrados")
      print("0 - Sair")

      opcao = input("Escolha: ")

      match opcao:
         case "1":
            cadastrar_produto_ui(empresa)

         case "2":
            criar_estrutura_ui(empresa)

         case "3":
            produzir_produto_ui(empresa)

         case "4":
            estoque_service.listar(empresa) # criar um arquivo em ui/interface para aqui no menu

         case "5":
            empresa_service.listar_produtos() # criar um arquivo em ui/interface para aqui no menu

         case "0":
            print("\nEncerrando sistema... Até logo!")
            break

         case _:
            print("\nOpção inválida! Tente um número entre 0 e 4.")
