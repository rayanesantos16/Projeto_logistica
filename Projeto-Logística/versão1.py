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
             nome = input("Digite o nome do produto: ")
             quantidade = int(input("Digite a quantidade de produtos: "))
             localizacao = input("Digite a localização do produto: ")

        novo_produto = [produto_id, nome, quantidade, localizacao]
        estoque.append(novo_produto)
        print("Sucesso: Produto cadastrado com êxito!")

def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")
    if len(estoque) == 0:
        print("O estoque está vazio.")
    else:
        print("ID        | Nome                      | Qtd        | Localização    ")
        print("--------------------------------------------------------------------")

        for p in estoque:
            print(f"{p[0]:<9} | {p[1]:<25} | {p[2]:<10} | {p[3]:<15}")