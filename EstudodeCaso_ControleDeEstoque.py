# Desenvolvendo um Sistema de Controle de Estoque com Python

# 1 - Adicionar produto, o sistema deve solicitar as seguintes informações:
# Nome do produto
# Preço do produto
# Quantidade em estoque

# 2 - Atualizar produto: o sistema deve pedir o nome do produto para atualizar e
# solicitar as seguintes informações para atualizar
# Preço do produto
# Quantidade em estoque

# 3 - Excluir produto
# o sistema deve pedir o nome para excluir o produto

# 4 - Visualizar estoque: o sistema deverá mostrar a lista de
# produtos, com as seguinte informações:
# Nome do produto
# Preço do produto
# Quantidade em estoque

# Lista para armazenar os produtos
estoque = []

# Função para exibir o menu
def exibir_menu():
    print("___________Empório dos Eletrônicos___________ \n")
    print("(1) Adicionar produto")
    print("(2) Atualizar produto")
    print("(3) Excluir produto")
    print("(4) Visualizar Estoque")
    print("(5) Sair \n")

# Função para adicionar ou atualizar um produto
def adicionar_ou_atualizar_produto(nome, preco, quantidade):
    for produto in estoque:
        if produto["Nome"] == nome:
            produto["Preço"] = preco
            produto["Quantidade"] = quantidade
            print(f"Produto {nome} atualizado com sucesso! \n")
            return
    estoque.append({"Nome": nome, "Preço": preco, "Quantidade": quantidade})
    print(f"Produto {nome} adicionado com sucesso! \n")

# Função para exibir o estoque atual
def exibir_estoque():
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("Estoque Atual:")
        contador = 1
        for produto in estoque:
            print(f"{contador} - Produto: {produto['Nome']}, Preço: R$ {produto['Preço']}, Quantidade: {produto['Quantidade']}")
            contador += 1
        print()

# Loop principal do programa
while True:
    exibir_menu()
    
    # Verificação do input para evitar erros
    while True:
        try:
            escolha_opcao = int(input("Quais das opções você deseja? "))
            break  # Sai do loop se a entrada for um número válido
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    
    if escolha_opcao == 1:
        nome_produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o valor do produto: "))
        quantidade = int(input("Digite a quantidade desejada: "))
        adicionar_ou_atualizar_produto(nome_produto, preco, quantidade)

    elif escolha_opcao == 2:
        exibir_estoque()  # Exibir o estoque antes de atualizar
        try:
            numero_produto = int(input("Digite o número do produto que deseja atualizar: "))
            produto = estoque[numero_produto - 1]
            preco = float(input("Digite o valor do produto: "))
            quantidade = int(input("Digite a quantidade desejada: "))
            adicionar_ou_atualizar_produto(produto["Nome"], preco, quantidade)
        except (IndexError, ValueError):
            print("Produto não encontrado. Verifique o número e tente novamente.\n")

    elif escolha_opcao == 3:
        exibir_estoque()  # Exibir o estoque antes de excluir
        try:
            numero_produto = int(input("Digite o número do produto que deseja excluir: "))
            produto = estoque.pop(numero_produto - 1)
            confirmacao = input(f"Gostaria de excluir {produto['Nome']}? (S/N): ").lower()
            if confirmacao == "s":
                print(f"Produto {produto['Nome']} excluído com sucesso!\n")
            else:
                estoque.insert(numero_produto - 1, produto)
                print("Exclusão cancelada. Produto não foi removido.\n")
        except (IndexError, ValueError):
            print("Produto não encontrado. Verifique o número e tente novamente.\n")

    elif escolha_opcao == 4:
        exibir_estoque()  # Exibir o estoque na opção 4 também
        input("Pressione Enter para voltar ao menu principal...")

    elif escolha_opcao == 5:
        print("Fim do menu \n")
        break

    else:
        print("Opção inválida\n")



