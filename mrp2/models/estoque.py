class Estoque:
    def __init__(self):
        self.itens = {}

    def adicionar(self, produto, quantidade):
        if produto.codigo in self.itens:
            self.itens[produto.codigo]["quantidade"] += quantidade
        else:
            self.itens[produto.codigo] = {"produto": produto, "quantidade": quantidade}

    def definir_quantidade(self, produto_codigo, nova_qtd):
        if produto_codigo in self.itens:
            self.itens[produto.codigo]["quantidade"] = nova_qtd
            return True
        return False

    def remover_do_sistema(self, codigo):
        if codigo in self.itens:
            del self.itens[codigo]

    def remover(self, produto, quantidade):
        if self.itens[produto.codigo]["quantidade"] >= quantidade:
            self.itens[produto.codigo]["quantidade"] -= quantidade
            return True
        return False

    def obter_quantidade(self, produto):
        if produto.codigo in self.itens:
            return self.itens[produto.codigo]["quantidade"]
        return 0

    def listar(self):
        print("\n--- STATUS DO ESTOQUE ---")
        if not self.itens:
            print("Estoque vazio.")
        for item in self.itens.values():
            tipo = "Insumo" if isinstance(item['produto'], Insumo) else "Prod. Final"
            print(f"{item['produto']} | Tipo: {tipo} | Qtd: {item['quantidade']}")