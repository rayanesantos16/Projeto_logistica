estoque = []

def adicionar_produto():
    print("\n===== ADICIONAR PRODUTO =====")
    produto_id = int(input("Digite o ID do produto (apenas números): "))
    
    id_existe = False
    for produto in estoque:
        if produto[0] == produto_id:
            id_existe = True
