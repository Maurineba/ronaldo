def menu_principal(empresa):
   while True:
      print("\n==============================")
      print("🏭 SISTEMA MRP -", empresa.nome)
      print("==============================")
      print("1 - Cadastrar Produto")
      print("2 - Criar Estrutura de Produto")
      print("3 - Produzir Produto")
      print("4 - Ver Estoque")
      print("0 - Sair")

      opcao = input("Escolha: ")

      if opcao == "1":
         cadastrar_produto(empresa)

      elif opcao == "2":
         criar_estrutura(empresa)
      elif opcao == "3":
         produzir_produto(empresa)
      elif opcao == "4":
         empresa.estoque.listar()
      elif opcao == "0":
         print("Encerrando sistema...")
         break
      else:
         print("❌ Opção inválida")
