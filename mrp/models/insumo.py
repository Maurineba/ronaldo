from models.produto import Produto
#produto com nome de insumo
class Insumo(Produto):
   def __init__(self, codigo, nome):
      super().__init__(codigo, nome)

