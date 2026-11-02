#arquivo = open(r"d:\Flavinho\Projeto Adega\Adega.txt", "a")
adega ="c:\\Users\\gusta\\Downloads\\Projeto.py"
arquivo = open(adega, "a", encoding="utf-8")
listaProdutos = []
listaClientes = []
listaVendas = []

def cadastrarProdutos():
    with open("produtos.txt", "a", encoding="utf-8") as arquivoProdutos:
        produto = str(input("Digite o nome do produto: ")).strip()
        qntProduto = int(input("Quantidade do produto: "))
        valorUni = float(input("Valor unitário do produto: R$"))
        
        
        id_produto = len(listaProdutos) + 1
        
        
        listaProdutos.append([id_produto, produto, qntProduto, valorUni])
        
        
        arquivoProdutos.write(f"{id_produto};{produto};{qntProduto};{valorUni}\n")
        
        print(f"\nProduto '{produto}' cadastrado com sucesso! (ID: {id_produto})")
"""def cadastrarProdutos():
    with open("produtos.txt", "a", encoding="utf-8") as arquivoProdutos:
        produto = str(input("Digite o nome do produto: "))
        qntProduto = int(input("Quantidade do produto: "))
        valorUni = float(input("Valor unitário do produto: R$"))
     
        listaProdutos.append(produto)
        listaProdutos.append(qntProduto)
        listaProdutos.append(valorUni)
        arquivoProdutos.write(f"{produto};{qntProduto};{valorUni}\n")"""
def buscarProdutos():
    listaProdutos.clear()
    
    # Abre e lê o arquivo direto para a memória RAM
    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            listaProdutos.append(linha.strip())

    print(""" 
    ---- LISTA DE PRODUTOS CADASTRADOS ----
    1- Mostrar todos os produtos
    2- Buscar produto por ID
    3- Buscar produto por nome
    0- Voltar para o menu Produtos""")
    
    escolha = input("Digite a opção desejada: ").strip()
    
    # 1. Mostrar todos
    if (escolha == "1"):
        print("\n--- TODOS OS PRODUTOS ---")
        for produto in listaProdutos:
            dados = produto.split(";")
            print(f"ID: {dados[0]} | Nome: {dados[1]} | Quantidade: {dados[2]} | Valor unitário: R${dados[3]}")
    
    # 2. Buscar por ID
    elif (escolha == "2"):
        idProduto = input("Digite o ID do produto: ").strip()
        encontrado = False
        
        for produto in listaProdutos:
            dados = produto.split(";")
            if dados[0] == idProduto:
                print("\n--- PRODUTO ENCONTRADO ---")
                print(f"ID: {dados[0]} | Nome: {dados[1]} | Quantidade: {dados[2]} | Valor unitário: R${dados[3]}")
                encontrado = True
                break
                
        if not encontrado:
            print("\nProduto não encontrado com esse ID.")

    # 3. Buscar por Nome
    elif (escolha == "3"):
        nomeProduto = input("Digite o nome do produto: ").strip()
        encontrado = False
        
        for produto in listaProdutos:
            dados = produto.split(";")
            if dados[1].lower() == nomeProduto.lower():
                print("\n--- PRODUTO ENCONTRADO ---")
                print(f"ID: {dados[0]} | Nome: {dados[1]} | Quantidade: {dados[2]} | Valor unitário: R${dados[3]}")
                encontrado = True
                break
                
        if not encontrado:
            print("\nProduto não encontrado.")
            
    elif (escolha == "0"):
        print("Voltando para o menu Produtos...")
    else:
        print("Opção inválida.")
    
def atualizarProdutos():
     listaProdutos.clear()
     with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            listaProdutos.append(linha.strip())
        idBusca = input("Digite o ID do produto que deseja atualizar: ").strip()
        encontrado = False
        
        for i in range(len(listaProdutos)):
            dados = listaProdutos[i].split(";")
            if dados[0] == idBusca:
                encontrado = True

                print(f"\nproduto encontrado : ID: {dados[0]} | Nome: {dados[1]} | Quantidade: {dados[2]} | Valor unitario: R${dados[3]}")

                novoNome = input(" Digite o novo nome do produto (ou aperte enter para manter o atual): ").strip()

                novaQuantidade = input("Digite a nova quantidade do produto (ou aperte enter para manter a atual): ").strip()

                novoValor = input("Digite o novo valor unitário do produto (ou aperte enter para manter o atual): ").strip()
                if novoNome:

                    dados[1] = novoNome
                if novaQuantidade:

                    dados[2] = novaQuantidade
                if novoValor:

                    dados[3] = novoValor

                listaProdutos[i] = ";".join(dados)
                break

        if not encontrado:
            print("Produto não encontrado.")
            return

                    

        with open("produtos.txt", "w", encoding="utf-8") as arquivo:
            for produto in listaProdutos:
                arquivo.write(produto + "\n")
            print("Produto atualizado com sucesso!")
     

                 

def menuRelatorios():
    escolha= ""
    while (escolha != "0"):
        print("""
----- RELATÓRIOS -----
[1] - Relatório de Produtos
[2] - Relatório de Clientes
[3] - Relatório de Vendas
[0] - Voltar para o menu principal""")
        escolha = input("Escolha:").strip()

        if (escolha == "1"):
                  
             print("fazendo...")
        elif (escolha == "2"):
             
             print("fazendo...")
        elif (escolha == "3"):
             
             print("fazendo...")
        elif (escolha == "0"):

            print("Voltando para o menu principal...")
            break
        else:
            print("Opção inválida.")
            continue
   


def menuVendas():
    escolha = ""
    while (escolha != "0"):
        print("""
----- VENDAS -----
[1] - Cadastrar
[2] - Atualizar 
[3] - Buscar 
[4] - Excluir
[0] - Voltar para o menu principal""")
        escolha = input("Escolha: ").strip()

        if (escolha == "1"):
                print("fazendo...")

        elif (escolha == "2"):
                print("fazendo...")

        elif (escolha == "3"):
                print("fazendo...")

        elif (escolha == "4"):
                print("fazendo...")   

        elif (escolha == "0"):
                print("Voltando para o menu principal...")
                break
        else:
                print("Opção inválida.")      
                continue


def menuClientes():
    escolha = ""
    while (escolha != "0"):
        print("""
----- CLIENTES -----
[1] - Cadastrar
[2] - Atualizar
[3] - Buscar
[4] - Excluir
[0] - Voltar para o menu principal""")
        escolha = input("Escolha: ").strip()

        if (escolha == "1"):

            print("fazendo...")

        elif (escolha == "2"):
            print("fazendo...")

        elif (escolha == "3"):

            print("fazendo...")
        elif (escolha == "4"):
             
             print("fazendo...")
        elif (escolha == "0"):
            
            print("Voltando para o menu principal...")
            break
        else:
            print("Opção inválida.")      
            continue  

def menuProdutos():
    escolha = ""
    while (escolha != "0"):
        print("""
----- PRODUTOS -----
[1] - Cadastrar
[2] - Buscar
[3] - Atualizar
[4] - Excluir
[0] - Voltar para o menu principal""")
        escolha = input("Escolha: ").strip()
        if (escolha == "1"):
            cadastrarProdutos()
        
        elif (escolha == "2"):
            buscarProdutos()

        elif (escolha == "3"):
            atualizarProdutos()

        elif (escolha == "4"):

            print("fazendo...")
        elif (escolha == "0"):

            print("Voltando para o menu principal...")
            break
        else:
            print("Opção inválida.")      
            continue  


def menuPrincipal():
    escolha = ""
    while (escolha != "0"):
        print("""
----- ADEGA DO FLÁVIO E GUSTAVO -----
(MENU PRINCIPAL)
[1] - Produtos
[2] - Clientes
[3] - Vendas
[4] - Relatórios
[0] - Sair""")
        escolha = input("Escolha: ").strip()
        if (escolha == "1"):

            menuProdutos()
        elif (escolha == "2"):

            menuClientes()
        elif (escolha == "3"):

            menuVendas()
        elif (escolha == "4"):

            menuRelatorios()
        elif(escolha == "0"):

            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

menuPrincipal()
print("Programa finalizado.")
