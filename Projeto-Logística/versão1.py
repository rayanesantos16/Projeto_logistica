estoque = []


def adicionar_produto():
    print("\n--- ADICIONAR PRODUTO ---")
    id_produto = int(input("ID: "))
    nome_produto = input("Nome: ")
    quantidade_produto = int(input("Quantidade: "))
    local_produto = input("Localização: ")
    