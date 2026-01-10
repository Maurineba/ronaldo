from mrp.services.empresa_service import EmpresaService
from mrp.services.produto_service import ProdutoService

empresa_service = EmpresaService()
produto_service = ProdutoService()

def produzir_produto_ui(empresa):
   print("\n--- ORDEM DE PRODUÇÃO ---")
   codigo = input("Código do Produto Final: ")

   try:
      quantidade = int(input("Quantidade a produzir: "))
      if quantidade <= 0: raise ValueError
   except ValueError:
      print("❌ Erro: Quantidade deve ser um número inteiro positivo.")
      return

   produto = empresa_service.buscar_produto(codigo)

   if not produto:
      print(f"❌ Erro: Produto '{codigo}' não encontrado.")
      return

   sucesso, mensagem = produto_service.realizar_producao(produto, quantidade)

   if sucesso:
      print(f"✅ {mensagem}")
   else:
      print(f"⚠️ {mensagem}")
