from models.produto import Produto

class Insumo(Produto):
   def __init__(self, codigo, nome):
      super().__init__(codigo, nome)
      self.estrutura = []
      self.eh_composto = False
