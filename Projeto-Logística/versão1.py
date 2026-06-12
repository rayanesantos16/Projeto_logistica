estoque = []

def adicionar_produto():
    print("\n===== ADICIONAR PRODUTO =====")
    produto_id = int(input("Digite o ID do produto (apenas números): "))
    
    id_existe = False
    for produto in estoque:
        if produto[0] == produto_id:
            id_existe = True

        if id_existe:
            print("Já existe um produto com este ID.")
        else:
             nome = input("Digite o nome do produto: ")
             quantidade = int(input("Digite a quantidade de produtos: "))
             localizacao = input("Digite a localização do produto: ")

        novo_produto = [produto_id, nome, quantidade, localizacao]
        estoque.append(novo_produto)
        print("Sucesso: Produto cadastrado com êxito!")

def listar_produtos():
    print("\n===== LISTA DE PRODUTOS =====")
    if len(estoque) == 0:
        print("O estoque está vazio.")
    else:
        print("ID        | Nome                      | Qtd        | Localização    ")
        print("====================================================================")

        for p in estoque:
            print(f"{p[0]:<9} | {p[1]:<25} | {p[2]:<10} | {p[3]:<15}")


def buscar_produto():
    print("\n===== BUSCAR PRODUTO POR ID =====")
    produto_id = int(input("Digite o ID do produto que deseja buscar: "))

    achou = False
    for produto in estoque:
        if produto[0] == produto_id:
            print("\n===== Produto Encontrado =====")
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Quantidade: {produto[2]}")
            print(f"Localização: {produto[3]}")
            achou = True

    if not achou:
        print("Produto não está no estoque.")

def atualizar_estoque():
    print("\n===== ADICIONAR AO ESTOQUE =====")
    produto_id = int(input("Digite o ID do produto: "))

    achou = False
    for i in range(len(estoque)):
        if estoque[i][0] == produto_id:
            achou = True
            
            produto_removido = estoque.pop(i)
            
            id_produto = produto_removido[0]
            nome_produto = produto_removido[1]
            quantidade_p = produto_removido[2]
            local_produto = produto_removido[3]

            print(f"Produto selecionado: {nome_produto} (Quantidade atual: {quantidade_p}i)ade")
            print("1. Entrada (+)")
            print("2. Saída (-)")
            opcao = input("Escolha uma operação: ")
            quantidade_alterar = int(input("Digite a quantidade: "))

            sucesso = False
            if opcao == '1':
                quantidade_p = quantidade_p + quantidade_alterar
                print(f"Sucesso! Nova quantidade: {quantidade_p}")
                sucesso = True
            elif opcao == '2':
                if quantidade_p >= quantidade_alterar:
                    quantidade_p = quantidade_p - quantidade_alterar
                    print(f"Sucesso! Nova quantidade: {quantidade_p}")
                    sucesso = True
                else:
                    print("Erro: Estoque insuficiente.")
            else:
                print("Opção inválida.")

            produto_atualizado = [id_produto, nome_produto, quantidade_p, local_produto]
            estoque.insert(i, produto_atualizado)

    if not achou:
        print("Produto não esta no estoque.")

