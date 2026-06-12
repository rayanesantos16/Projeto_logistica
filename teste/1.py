estoque = []

def adicionar_produto():
    print("\n===== ADICIONAR PRODUTO =====")
    produto_id = int(input("Digite o ID do produto (apenas números): "))
    
    id_existe = False
    for produto in estoque:
        if produto[0] == produto_id:
            id_existe = True

    if id_existe:
        print("Erro: Já existe um produto com este ID.")
    else:
        nome = input("Digite o nome do produto: ").strip()
        quantidade = int(input("Digite a quantidade inicial: "))
        localizacao = input("Digite a localização (ex: A-01-03): ").strip()

        # Cria a linha da matriz e adiciona ao estoque
        novo_produto = [produto_id, nome, quantidade, localizacao]
        estoque.append(novo_produto)
        print("Sucesso: Produto cadastrado com êxito!")

def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")
    if len(estoque) == 0:
        print("O estoque está vazio.")
    else:
        # Cabeçalho da tabela
        print("ID        | Nome                      | Qtd        | Localização    ")
        print("--------------------------------------------------------------------")
        
        # Exibe cada linha da matriz
        for p in estoque:
            print(f"{p[0]:<9} | {p[1]:<25} | {p[2]:<10} | {p[3]:<15}")

def buscar_produto():
    print("\n--- BUSCAR PRODUTO POR ID ---")
    produto_id = int(input("Digite o ID do produto que deseja buscar: "))

    achou = False
    for produto in estoque:
        if produto[0] == produto_id:
            print("\nProduto Encontrado:")
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Quantidade: {produto[2]}")
            print(f"Localização: {produto[3]}")
            achou = True

    if not achou:
        print("Erro: Produto não encontrado.")

def atualizar_estoque():
    print("\n--- ATUALIZAR ESTOQUE ---")
    produto_id = int(input("Digite o ID do produto: "))

    achou = False
    for produto in estoque:
        if produto[0] == produto_id:
            achou = True
            print(f"Produto selecionado: {produto[1]} (Quantidade atual: {produto[2]})")
            print("1. Entrada (+)")
            print("2. Saída (-)")
            opcao = input("Escolha a operação: ")
            quantidade_alterar = int(input("Digite a quantidade: "))

            if opcao == '1':
                produto[2] = produto[2] + quantidade_alterar
                print(f"Sucesso! Nova quantidade: {produto[2]}")
            elif opcao == '2':
                if produto[2] >= quantidade_alterar:
                    produto[2] = produto[2] - quantidade_alterar
                    print(f"Sucesso! Nova quantidade: {produto[2]}")
                else:
                    print("Erro: Estoque insuficiente.")
            else:
                print("Opção inválida.")

    if not achou:
        print("Erro: Produto não encontrado.")

def menu_principal():
    opcao = "0"
    while opcao != "5":
        print("\n========================================")
        print("LOGÍSTICA INTEGRADA - MENU SCES")
        print("========================================")
        print("1. Adicionar Produto")
        print("2. Listar Todos os Produtos")
        print("3. Buscar Produto por ID")
        print("4. Atualizar Estoque")
        print("5. Sair do Programa")
        
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            buscar_produto()
        elif opcao == '4':
            atualizar_estoque()
        elif opcao == '5':
            print("Encerrando o sistema. Até logo!")
        else:
            print("Opção inválida! Tente novamente.")

# Ponto de partida do programa
menu_principal()
