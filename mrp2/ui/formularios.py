from models import Insumo, ProdutoFinal

def consultar_produto_ui(empresa):
    print("\n[Consultar Produto]")
    cod = input("Código do produto para consulta: ")
    p = empresa.buscar_produto(cod)
    
    if p:
        print("-" * 30)
        print(f"CÓDIGO: {p.codigo}")
        print(f"NOME: {p.nome}")
        tipo = "Insumo (Matéria-prima)" if isinstance(p, Insumo) else "Produto Final (Acabado)"
        print(f"TIPO: {tipo}")
        print(f"ESTOQUE ATUAL: {empresa.estoque.obter_quantidade(p)}")
        
        if isinstance(p, ProdutoFinal):
            print("\nESTRUTURA DE PRODUTO (RECEITA):")
            if not p.estrutura:
                print("   (Nenhum insumo cadastrado)")
            else:
                for item in p.estrutura:
                    print(f"   -> {item.insumo.nome} | Qtd Necessária: {item.quantidade}")
        print("-" * 30)
    else:
        print("❌ Produto não encontrado.")

def editar_produto_ui(empresa):
    print("\n[Editar Produto]")
    cod = input("Código do produto que deseja editar: ")
    p = empresa.buscar_produto(cod)
    if p:
        novo_nome = input(f"Novo nome para {p.nome} (deixe em branco para manter): ")
        if novo_nome:
            p.nome = novo_nome
            print("✅ Nome atualizado!")
    else:
        print("❌ Produto não encontrado.")

def excluir_produto_ui(empresa):
    print("\n[Excluir Produto]")
    cod = input("Código do produto que deseja excluir: ")
    if empresa.excluir_produto(cod):
        print("✅ Produto e registros de estoque removidos!")
    else:
        print("❌ Produto não encontrado.")

def editar_estoque_ui(empresa):
    print("\n[Editar Estoque - Ajuste Direto]")
    cod = input("Código do produto: ")
    p = empresa.buscar_produto(cod)
    if p:
        nova_qtd = int(input(f"Quantidade atual é {empresa.estoque.obter_quantidade(p)}. Nova quantidade: "))
        empresa.estoque.definir_quantidade(cod, nova_qtd)
        print("✅ Estoque ajustado!")
    else:
        print("❌ Produto não encontrado.")

def cadastrar_produto_ui(empresa):
    print("\n[Novo Produto]")
    cod = input("Código: ")
    if empresa.buscar_produto(cod):
        print("❌ Erro: Este código já existe.")
        return
    nome = input("Nome: ")
    tipo = input("Tipo (1-Insumo, 2-Final): ")
    if tipo == "1":
        empresa.cadastrar_produto(Insumo(cod, nome))
    else:
        empresa.cadastrar_produto(ProdutoFinal(cod, nome))
    print("✅ Produto registrado!")

def criar_estrutura_ui(empresa):
    print("\n[Definir Estrutura/Receita]")
    cod_f = input("Código do Produto Final: ")
    pf = empresa.buscar_produto(cod_f)
    if isinstance(pf, ProdutoFinal):
        while True:
            cod_i = input("Código do Insumo (ou '0' para sair): ")
            if cod_i == '0': break
            insumo = empresa.buscar_produto(cod_i)
            if isinstance(insumo, Insumo):
                qtd = int(input(f"Quantos(as) {insumo.nome} cada {pf.nome} leva? "))
                pf.estrutura.append(ItemEstrutura(insumo, qtd))
                print(f"➕ {insumo.nome} adicionado.")
            else:
                print("❌ Insumo inválido.")
    else:
        print("❌ Produto não é um Produto Final.")

def registrar_compra_ui(empresa):
    print("\n[Registrar Compra/Entrada]")
    cod = input("Código: ")
    p = empresa.buscar_produto(cod)
    if p:
        qtd = int(input(f"Quantidade comprada de {p.nome}: "))
        empresa.estoque.adicionar(p, qtd)
        print("✅ Entrada registrada!")
    else:
        print("❌ Produto não cadastrado.")

def produzir_ui(empresa):
    print("\n[Ordem de Produção]")
    cod = input("Código do Produto Final: ")
    pf = empresa.buscar_produto(cod)
    if pf:
        qtd = int(input("Quantidade a produzir: "))
        from services import realizar_producao
        realizar_producao(pf, qtd, empresa.estoque)
    else:
        print("❌ Produto não encontrado.")