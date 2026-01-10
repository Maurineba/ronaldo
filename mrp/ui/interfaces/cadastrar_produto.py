from mrp.services.empresa_service import EmpresaService


empresa_service = EmpresaService()


def cadastrar_produto_ui(empresa_service):
   print("\n--- NOVO CADASTRO DE PRODUTO ---")

   codigo = input("Código identificador: ").strip()
   if not codigo:
      print("❌ O código não pode ser vazio.")
      return

   nome = input("Nome do produto: ").strip()
   if not nome:
      print("O nome nao pode ser vazio")
      return

   print("Selecione o tipo:")
   print(" [1] Insumo")
   print(" [2] Produto Final")
   opcoes = ("1", "2")

   tipo = str(input("Opção: "))
   if tipo not in opcoes:
      print("Escolha uma opcao valida")
      return

   # sucesso, mensagem = empresa_service.cadastrar_novo_produto(codigo, nome, tipo)
   # if sucesso:
   #     print(f"✅ {mensagem}")
   # else:
   #     print(f"❌ {mensagem}")
