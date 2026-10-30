listaProdutos = []

def cadastrarProdutos():
    with open("Produtos.txt", "a", encoding="utf-8") as arquivo:
        qnt = int(input("Qnt de Produtos para cadastrar: "))
        for c in range(1, qnt+1):
            produto = input(f"{c}º produto: ")
            if (produto in listaProdutos):
                print("Esse produto já está na lista.")
            else:
                listaProdutos.append(produto)
                arquivo.write(produto + "\n")