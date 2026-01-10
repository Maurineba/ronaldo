# =========================
# MODELS
# =========================

class Produto:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Insumo(Produto):
    pass


class ProdutoFinal(Produto):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.estrutura = []  # Lista de ItemEstrutura


class ItemEstrutura:
    def __init__(self, insumo, quantidade):
        self.insumo = insumo
        self.quantidade = quantidade


class Estoque:
    def __init__(self):
        self.itens = {}

    def adicionar(self, produto, quantidade):
        if produto.codigo in self.itens:
            self.itens[produto.codigo]["quantidade"] += quantidade
        else:
            self.itens[produto.codigo] = {
                "produto": produto,
                "quantidade": quantidade
            }

    def remover(self, produto, quantidade):
        self.itens[produto.codigo]["quantidade"] -= quantidade

    def quantidade(self, produto):
        return self.itens.get(produto.codigo, {}).get("quantidade", 0)

    def listar(self):
        print("\n--- ESTOQUE ---")
        if not self.itens:
            print("Estoque vazio")
        for item in self.itens.values():
            print(f"{item['produto']} | Qtde: {item['quantidade']}")


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []
        self.estoque = Estoque()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None


# =========================
# SERVICES
# =========================

def produzir(produto_final, quantidade, estoque):
    if not isinstance(produto_final, ProdutoFinal):
        print("❌ Produto não é um produto final")
        return

    # Verifica insumos
    for item in produto_final.estrutura:
        qtd_necessaria = item.quantidade * quantidade
        if estoque.quantidade(item.insumo) < qtd_necessaria:
            print(f"❌ Insumo insuficiente: {item.insumo.nome}")
            return

    # Baixa insumos
    for item in produto_final.estrutura:
        estoque.remover(item.insumo, item.quantidade * quantidade)

    # Adiciona produto final
    estoque.adicionar(produto_final, quantidade)
    print("✅ Produção realizada com sucesso!")


# =========================
# UI (MENU)
# =========================

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


def cadastrar_produto(empresa):
    print("\n--- CADASTRO DE PRODUTO ---")
    codigo = input("Código: ")
    nome = input("Nome: ")
    tipo = input("1 - Insumo | 2 - Produto Final: ")

    if tipo == "1":
        produto = Insumo(codigo, nome)
    elif tipo == "2":
        produto = ProdutoFinal(codigo, nome)
    else:
        print("❌ Tipo inválido")
        return

    empresa.adicionar_produto(produto)
    empresa.estoque.adicionar(produto, 0)
    print("✅ Produto cadastrado com sucesso!")


def criar_estrutura(empresa):
    print("\n--- ESTRUTURA DE PRODUTO ---")
    codigo_pf = input("Código do Produto Final: ")
    produto_final = empresa.buscar_produto(codigo_pf)

    if not isinstance(produto_final, ProdutoFinal):
        print("❌ Produto não encontrado ou não é produto final")
        return

    while True:
        codigo_insumo = input("Código do Insumo (0 para sair): ")
        if codigo_insumo == "0":
            break

        insumo = empresa.buscar_produto(codigo_insumo)
        if not isinstance(insumo, Insumo):
            print("❌ Insumo inválido")
            continue

        quantidade = int(input("Quantidade: "))
        produto_final.estrutura.append(ItemEstrutura(insumo, quantidade))
        print("➕ Insumo adicionado à estrutura")

    print("✅ Estrutura criada com sucesso!")


def produzir_produto(empresa):
    print("\n--- PRODUÇÃO ---")
    codigo = input("Código do Produto Final: ")
    quantidade = int(input("Quantidade a produzir: "))

    produto = empresa.buscar_produto(codigo)
    produzir(produto, quantidade, empresa.estoque)


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    nome_empresa = input("Digite o nome da empresa: ")
    empresa = Empresa(nome_empresa)
    menu_principal(empresa)
    try:
        print("\n\n👋 Programa encerrado.")
    except Exception as e:
        print(f"\n❌ Erro fatal: {e}")
        print("O sistema será encerrado.")
