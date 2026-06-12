# Matriz global: [ID, Nome, Quantidade, Localização]
estoque = []

def adicionar_produto():
    print("\n--- ADICIONAR PRODUTO ---")
    id_p = int(input("ID: "))
    nome = input("Nome: ")
    qtd = int(input("Quantidade: "))
    local = input("Localização: ")
    
    estoque.append([id_p, nome, qtd, local])
    print("Produto adicionado!")

def listar_produtos():
    print("\n--- PRODUTOS CADASTRADOS ---")
    if not estoque:
        print("Estoque vazio.")
        return
    for p in estoque:
        print(f"ID: {p[0]} | Nome: {p[1]} | Qtd: {p[2]} | Local: {p[3]}")

def buscar_produto():
    print("\n--- BUSCAR POR ID ---")
    id_busca = int(input("Digite o ID: "))
    for p in estoque:
        if p[0] == id_busca:
            print(f"Encontrado -> Nome: {p[1]} | Qtd: {p[2]} | Local: {p[3]}")
            return
    print("Produto não encontrado.")

def atualizar_estoque():
    print("\n--- ATUALIZAR ESTOQUE ---")
    id_busca = int(input("Digite o ID: "))
    for p in estoque:
        if p[0] == id_busca:
            print("1. Entrada (+)\n2. Saída (-)")
            opcao = input("Escolha: ")
            qtd_alterar = int(input("Quantidade: "))
            
            if opcao == "1":
                p[2] += qtd_alterar
            elif opcao == "2":
                p[2] -= qtd_alterar
            print("Estoque atualizado!")
            return
    print("Produto não encontrado.")

while True:
    print("\n=== MENU SCES ===")
    print("1. Adicionar | 2. Listar | 3. Buscar | 4. Atualizar | 5. Sair")
    opcao = input("Opção: ")
    
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        buscar_produto()
    elif opcao == "4":
        atualizar_estoque()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
