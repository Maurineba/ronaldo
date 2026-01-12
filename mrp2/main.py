from models import Empresa
from ui import mostrar_menu_principal, processar_opcao

def main():
    print("--- SISTEMA DE PRODUÇÃO (Eng. Computação IFCE) ---")
    nome_emp = input("Nome da sua Empresa: ")
    empresa = Empresa(nome_emp)

    while True:
        mostrar_menu_principal(empresa)
        op = input("Opção: ")
        if not processar_opcao(op, empresa):
            break

if __name__ == "__main__":
    main()