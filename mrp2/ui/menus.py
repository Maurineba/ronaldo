from ui.formularios import (
    cadastrar_produto_ui, criar_estrutura_ui, registrar_compra_ui,
    editar_estoque_ui, produzir_ui, consultar_produto_ui,
    editar_produto_ui, excluir_produto_ui
)

def mostrar_menu_principal(empresa):
    print(f"\n>> MENU: {empresa.nome}")
    print("1. Cadastrar Produto      6. Ver Estoque")
    print("2. Definir Estrutura      7. Editar Produto")
    print("3. Comprar/Entrada        8. Excluir Produto")
    print("4. Editar Estoque (Qtd)   9. Consultar Produto")
    print("5. Produzir Item          0. Sair")

def processar_opcao(op, empresa):
    if op == "1": 
        cadastrar_produto_ui(empresa)
    elif op == "2": 
        criar_estrutura_ui(empresa)
    elif op == "3": 
        registrar_compra_ui(empresa)
    elif op == "4": 
        editar_estoque_ui(empresa)
    elif op == "5": 
        produzir_ui(empresa)
    elif op == "6": 
        empresa.estoque.listar()
    elif op == "7": 
        editar_produto_ui(empresa)
    elif op == "8": 
        excluir_produto_ui(empresa)
    elif op == "9": 
        consultar_produto_ui(empresa)
    elif op == "0": 
        return False
    else: 
        print("❌ Opção inválida.")
    return True