# gerenciador_arquivos/main.py

from core.renomeador import renomear_arquivos
from core.organizador import organizar_arquivos
from core.duplicados import mover_duplicados


def menu():
    print("\n=== Gerenciador de Arquivos ===")
    print("1 - Renomear arquivos")
    print("2 - Organizar arquivos")
    print("3 - Remover duplicados")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()
    return opcao


def executar():
    while True:
        opcao = menu()

        if opcao == "1":
            pasta = input("Informe o caminho da pasta: ").strip()
            prefixo = input("Informe o prefixo para os arquivos: ").strip()
            extensao = input("Informe a extensão (ou deixe vazio para todas): ").strip()
            extensao = extensao if extensao else None

            try:
                logs = renomear_arquivos(pasta, prefixo, extensao)
                print("\n--- Resultado ---")
                for log in logs:
                    print(log)
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            pasta = input("Informe o caminho da pasta: ").strip()
            try:
                logs = organizar_arquivos(pasta)
                print("\n--- Resultado ---")
                for log in logs:
                    print(log)
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "3":
            pasta = input("Informe o caminho da pasta: ").strip()
            try:
                logs = mover_duplicados(pasta)
                print("\n--- Resultado ---")
                for log in logs:
                    print(log)
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar()
