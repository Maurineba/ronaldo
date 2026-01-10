def produzir_produto(empresa):
   print("\n--- ORDEM DE PRODUÇÃO ---")
   codigo = input("Código do Produto Final: ")

    # Validação simples de entrada de número
   try:
      quantidade = int(input("Quantidade a produzir: "))
      if quantidade <= 0: raise ValueError
   except ValueError:
      print("❌ Erro: Quantidade deve ser um número inteiro positivo.")
      return

    # Busca o produto via serviço
   produto = empresa_service.buscar_produto(codigo)

   if not produto:
      print(f"❌ Erro: Produto '{codigo}' não encontrado.")
      return

    # Tenta produzir e recebe o feedback do serviço
   sucesso, mensagem = producao_service.fabricar(produto, quantidade)

   if sucesso:
      print(f"✅ {mensagem}")
   else:
      print(f"⚠️ {mensagem}")
