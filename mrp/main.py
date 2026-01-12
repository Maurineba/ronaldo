import sys
import os

# Adiciona o diretório atual ao sys.path para garantir que os imports funcionem
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.empresa import Empresa
from ui.menu import menu_principal

def iniciar_sistema():
    try:
        print("--- SISTEMA MRP (Eng. Computação IFCE) ---")

        nome_empresa = input("Digite o nome da empresa: ").strip() #variável para receber o nome da empresa

        if not nome_empresa:
            nome_empresa = "Empresa Padrão"

        empresa = Empresa(nome_empresa) #objeto empresa criado

        # Chama o menu principal
        menu_principal(empresa)

        print("\nPrograma encerrado com sucesso.")

    except KeyboardInterrupt:
        print("\n\nSaindo... (Interrompido pelo usuário)")
    except Exception as e:
        print(f"\nErro fatal no sistema: {e}")
        print("O sistema será encerrado.")

if __name__ == "__main__":
    iniciar_sistema()
