def criar_estrutura_ui(empresa_service):
   print("\n--- CONFIGURAR ESTRUTURA ---")

   codigo_pf = input("Código do Produto Final: ")

   pf = empresa_service.buscar_produto(codigo_pf)

   if not pf or not hasattr(pf, 'estrutura'):
      print("❌ Erro: Produto não encontrado ou não permite estrutura.")
      return

   while True:
      print(f"\nEditando: {pf.nome}")

      cod_insumo = input("Código do Insumo (ou '0' para finalizar): ")

      if cod_insumo == "0":
         break

      insumo = empresa_service.buscar_produto(cod_insumo)
      if not insumo:
         print("❌ Insumo não cadastrado.")
         continue

      try:
         qtd = int(input(f"Quantidade de {insumo.nome} p/ cada {pf.nome}: "))

         sucesso, mensagem = empresa_service.adicionar_item_a_estrutura(pf, insumo, qtd)
         if sucesso:
            print(f"✅ {mensagem}")
         else:
            print(f"⚠️ {mensagem}")
      except ValueError:
         print("❌ Erro: Digite um número válido para a quantidade.")
   print(f"\n✅ Estrutura de '{pf.nome}' atualizada!")
