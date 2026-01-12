from models.insumo import Insumo

from services.empresa_service import EmpresaService
from services.produto_service import ProdutoService


def criar_estrutura_ui(empresa):
   empresa_service = EmpresaService(empresa)
   produto_service = ProdutoService()

   print("\n--- CONFIGURAR ESTRUTURA ---")

   codigo_pf = input("Código do Produto Final: ")

   pf = empresa_service.buscar_produto(codigo_pf)
   if not pf:
      raise ValueError("Produto não encontrado")
   if not hasattr(pf,"estrutura"):
      raise ValueError("Produto não permite estrutura")

   codigo_insumo = input("COdigo do Insumo: ")

   insumo = empresa_service.buscar_produto(codigo_insumo)
   if not insumo:
      raise ValueError("Insumo não encontrado")
   if not isinstance(insumo, Insumo):
      raise ValueError("Insira o código de um Insumo, não de Produto Final")

   qtd = int(input("Quantidade do insumo por produto: "))
   produto_service.criar_estrutura(pf, insumo, qtd)

   print(f"Insumo adicionada à Estrutura com sucesso. Produto: {pf.nome}, Estrutura: {pf.estrutura}")
   # while True:
   #    print(f"\nEditando: {pf.nome}")

   #    cod_insumo = input("Código do Insumo (ou '0' para finalizar): ")

   #    if cod_insumo == "0":
   #       break

   #    insumo = empresa_service.buscar_produto(cod_insumo)
   #    if not insumo:
   #       print("❌ Insumo não cadastrado.")
   #       continue

   #    try:
   #       qtd = int(input(f"Quantidade de {insumo.nome} p/ cada {pf.nome}: "))

   #       sucesso, mensagem = empresa_service.adicionar_item_a_estrutura(pf, insumo, qtd)
   #       if sucesso:
   #          print(f"✅ {mensagem}")
   #       else:
   #          print(f"⚠️ {mensagem}")
   #    except ValueError:
   #       print("❌ Erro: Digite um número válido para a quantidade.")
   # print(f"\n✅ Estrutura de '{pf.nome}' atualizada!")
