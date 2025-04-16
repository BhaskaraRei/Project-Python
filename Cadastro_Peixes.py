import csv
import re

# Arquivo para armazenamento
arquivo = "especies_peixes_reofilicos.txt"

# Lista de peixes reofílicos populares
peixes_populares = [
    "Tambaqui (Colossoma macropomum)",
    "Pacu (Piaractus mesopotamicus)",
    "Matrinxã (Brycon amazonicus)",
    "Pintado (Pseudoplatystoma corruscans)",
    "Dourado (Salminus brasiliensis)",
    "Surubim (Pseudoplatystoma reticulatum)"
]

# Função para validar se o nome do peixe contém apenas caracteres alfabéticos e espaços
def validar_nome(nome):
    return bool(re.fullmatch(r"[A-Za-z\sáéíóúãõçÊÔÕÁÉÍÓÚ]+", nome))

# Função para exibir a lista de peixes populares e cadastrar uma espécie
def cadastrar_especie():
    print("\nPeixes reofílicos populares:")
    for i, peixe in enumerate(peixes_populares, start=1):
        print(f"{i}. {peixe}")
    print("0. Outro (digitar manualmente)")

    try:
        escolha = int(input("Escolha o número correspondente ao peixe: ").strip())
        if escolha == 0:
            especie = input("Digite o nome da espécie: ").strip()
            if not validar_nome(especie):
                print("Nome inválido! Use apenas letras e espaços.")
                return
        elif 1 <= escolha <= len(peixes_populares):
            especie = peixes_populares[escolha - 1]
        else:
            print("Opção inválida. Tente novamente.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return

    info_extra = ""
    adicionar_info = input("Deseja adicionar uma informação extra sobre o peixe? (s/n): ").strip().lower()
    if adicionar_info == "s":
        info_extra = input("Digite a informação extra: ").strip()
    
    # Armazena os dados em uma lista
    dados = [especie, info_extra]

    # Salva no arquivo .txt
    with open(arquivo, "a", newline='', encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(dados)

    print(f"Espécie '{especie}' cadastrada com sucesso!")

# Função para listar todas as espécies cadastradas
def listar_especies():
    print("\nEspécies cadastradas:")
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                print(f"Nome: {linha[0]}, Informação extra: {linha[1]}")
    except FileNotFoundError:
        print("Nenhuma espécie cadastrada ainda!")

# Função para editar uma espécie
def editar_especie():
    listar_especies()
    try:
        nome_especie = input("\nDigite o nome da espécie que deseja editar: ").strip()
        novas_linhas = []
        encontrado = False

        with open(arquivo, "r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if linha[0].lower() == nome_especie.lower():
                    encontrado = True
                    opcao = input("Deseja editar o nome (1) ou a informação extra (2)? ").strip()
                    if opcao == "1":
                        novo_nome = input("Digite o novo nome da espécie: ").strip()
                        if not validar_nome(novo_nome):
                            print("Nome inválido! Use apenas letras e espaços.")
                            return
                        novas_linhas.append([novo_nome, linha[1]])
                    elif opcao == "2":
                        nova_info = input("Digite a nova informação extra: ").strip()
                        novas_linhas.append([linha[0], nova_info])
                    else:
                        print("Opção inválida.")
                        return
                else:
                    novas_linhas.append(linha)

        if encontrado:
            with open(arquivo, "w", newline='', encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerows(novas_linhas)
            print(f"Edição concluída!")
        else:
            print(f"Espécie '{nome_especie}' não encontrada.")
    except FileNotFoundError:
        print("Nenhuma espécie cadastrada ainda!")

# Função para apagar uma espécie
def apagar_especie():
    listar_especies()
    try:
        nome_especie = input("\nDigite o nome da espécie que deseja apagar: ").strip()
        novas_linhas = []
        encontrado = False

        with open(arquivo, "r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if linha[0].lower() == nome_especie.lower():
                    encontrado = True
                else:
                    novas_linhas.append(linha)

        if encontrado:
            with open(arquivo, "w", newline='', encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerows(novas_linhas)
            print(f"Espécie '{nome_especie}' removida com sucesso!")
        else:
            print(f"Espécie '{nome_especie}' não encontrada.")
    except FileNotFoundError:
        print("Nenhuma espécie cadastrada ainda!")

# Função principal
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar espécie")
        print("2. Listar espécies")
        print("3. Editar espécie")
        print("4. Apagar espécie")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_especie()
        elif opcao == "2":
            listar_especies()
        elif opcao == "3":
            editar_especie()
        elif opcao == "4":
            apagar_especie()
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()