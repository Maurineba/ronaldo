def cadastrar_produto_ui(empresa_service):
    print("\n--- NOVO CADASTRO DE PRODUTO ---")

    codigo = input("Código identificador: ").strip().upper()
    if not codigo:
        print("❌ O código não pode ser vazio.")
        return

    nome = input("Nome do produto: ").strip()
    print("Selecione o tipo:")
    print(" [1] Insumo (Matéria-prima)")
    print(" [2] Produto Final (Manufaturado)")
    tipo = input("Opção: ")

    # Delega a criação para o serviço
    sucesso, mensagem = empresa_service.cadastrar_novo_produto(codigo, nome, tipo)

    if sucesso:
        print(f"✅ {mensagem}")
    else:
        print(f"❌ {mensagem}")
