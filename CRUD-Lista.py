produtos = []

while True:
    print("---- Menu de opcões ----")
    print("1 - Cadastrar produto")
    print("2 - Exibir produtos")
    print("3 - Atualizar produto")
    print("4 - Excluir produto")
    print("5 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ").capitalize()
        if produto not in produtos:
            produtos.append(produto)
            print(f"Produto {produto} cadastrado!")
        else:
            print(f"Produto {produto} já existe!")
    elif opcao == "2":
        if produtos:
            for i, item in enumerate(produtos):
                print(f"{i} - {item}")
        else:
            print("Lista de produtos está vazia!")
    elif opcao == "3":
        produto_antigo = input("Digite o nome do produto para atualizar: ").capitalize()
        if produto_antigo in produtos:
            novo_produto = input("Digite o novo nome do produto: ").capitalize()
            indice = produtos.index(produto_antigo)
            produtos[indice] = novo_produto
            print(f"Produto {produto_antigo} atualizado para {novo_produto}")
        else:
            print(f"Produto {produto_antigo} não encontrado!")
    elif opcao == "4":
        produto = input("Digite o nome do produto para apagar: ").capitalize()
        if produto in produtos:
            produtos.remove(produto)
            print(f"Produto {produto} apagado com sucesso!")
        else:
            print(f"Produto {produto} não encontrado.")
    elif opcao == "5":
        print("Saindo do programa... Até logo!")
        break
    else:
        print(f"Opção inválida!")
