class Produto:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def __str__(self):
        return f"[{self.codigo}] {self.nome}"