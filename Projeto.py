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
        
        # 1. Gera o ID automático
        id_produto = len(listaProdutos) + 1
        
        # 2. Salva na RAM como uma sub-lista [ID, Nome, Quantidade, Valor]
        listaProdutos.append([id_produto, produto, qntProduto, valorUni])
        
        # 3. Grava no arquivo incluindo o ID no início
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
    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            listaProdutos.append(linha.strip())
    print(f"Produtos que já estão carregados: {listaProdutos}")


                 

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

            print("fazendo...")
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
