#adega ="c:\\Users\\gusta\\Downloads\\Projeto.py"

arquivo = open("adega", "a", encoding="utf-8")

listaVendas = []

def listarClientes():
    clientes = []

    with open("clientes.txt", "r", encoding="utf-8") as arquivo_listar_clientes:
        for linha in arquivo_listar_clientes:
            if linha != "":
                dados_cli = linha.split(";")
                id_cli = int(dados_cli[0])
                nome_cli = dados_cli[1]
                idade_cli = dados_cli[2]

                clientes.append([id_cli, nome_cli, idade_cli])
    
    return (clientes)

def cadastrarClientes():
    with open("clientes.txt", "a", encoding="utf-8") as arquivo_cadastrar_clientes:
        nome = input("Nome do cliente: ")
        idade = int(input(f"Idade do(a) {nome}: "))
        if (idade < 18):
            print("Cliente não pode ser cadastrado. Apenas se tiver 18 anos ou mais.")
            print("Voltando para o Menu Clientes...")
            return

        listaC = listarClientes()

        if len(listaC) == 0:
            id_cliente = 1
        else:
            maior_id = 0
            for cliente in listaC:
                if cliente[0] > maior_id:
                    maior_id = cliente[0]
            id_cliente = maior_id + 1
                
        arquivo_cadastrar_clientes.write(f"{id_cliente};{nome};{idade}\n")
        print(f"\nCliente '{nome}' cadastrado com sucesso! (ID: {id_cliente})")

def buscarClientes():
    print("""
    ---- OPÇÕES DE BUSCA ----
    1 - Mostrar todos os clientes cadastrados
    2 - Buscar clientes por ID
    3 - Buscar clientes por nome
    0 - Voltar para o Menu Clientes""")

    escolha = input("Digite a opção desejada: ").strip()

    #mostrar todos
    if (escolha == "1"):
        print("""\n---CLIENTES CADRASTADOS---""")
        for cliente in listarClientes():
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]}")

    #buscar por id
    if (escolha == "2"):
        idCliente = int(input("Digite o ID do cliente: ").strip())
        for cliente in listarClientes():
            if (cliente[0] == idCliente):
                print("\n--- CLIENTE ENCONTRADO ---")
                print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]}")
            else:
                print("\nID DE CLIENTE NÃO ENCONTRADO!")
                print("Voltando para o Menu Clientes...")
                return


#ESSA FUNÇÃO LISTA OS PRODUTOS CADASTRADOS NO ARQUIVO "produtos.txt" E RETORNA UMA LISTA COM OS DADOS DE CADA PRODUTO.
def listarProdutos():
    produtos = []

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:

        

        for linha in arquivo:

            if linha != "":

               # print(linha.strip())

                dados = linha.split(";")

                id_p = int(dados[0])

                nome = dados[1]

                qnt = int(dados[2])

                valor = float(dados[3])

                produtos.append([id_p, nome, qnt, valor])

    return (produtos)



def cadastrarProdutos():

    with open("produtos.txt", "a", encoding="utf-8") as arquivoProdutos:

        produto = str(input("Digite o nome do produto: ")).strip()

        qntProduto = int(input("Quantidade do produto: "))
        if qntProduto < 20:
            print("A quantidade mínima de produtos é 20. voltando para o Menu Produtos.")
            return

        valorUni = float(input("Valor unitário do produto: R$"))
        
        

        listaP = listarProdutos()

        # Lógica para garantir que o ID nunca se repita:
        if len(listaP) == 0:
            id_produto = 1
        else:
            maior_id = 0
            for produto in listaP:
                #Compara o id de cada produto com maior_id. Se o iD do produto for maior, atualiza o maior_id.
                if produto[0] > maior_id:
                    maior_id = produto[0]
            id_produto = maior_id + 1
        
        arquivoProdutos.write(f"{id_produto};{produto};{qntProduto};{valorUni}\n")

       

        print(f"\nProduto '{produto}' cadastrado com sucesso! (ID: {id_produto})")



def buscarProdutos():

    print("""

    ---- OPÇÕES DE BUSCA ----

    1 - Mostrar todos os produtos

    2 - Buscar produto por ID

    3 - Buscar produto por nome

    0 - Voltar para o Menu Produtos""")

   

    escolha = input("Digite a opção desejada: ").strip()

    #mostrar todos
    if (escolha == "1"):
        print(""" \n---PRODUTOS CADRASTADOS---""")        
        for produto in listarProdutos():
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Valor unitário: R${produto[3]}")
    
    #buscar por id
    elif (escolha == "2"):
        idProduto = (input("Digite o ID do produto: ").strip())
        for produto in listarProdutos():
            if produto[0] == idProduto:
                print("\n--- PRODUTO ENCONTRADO ---")
                print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Valor unitário: R${produto[3]}")
            else:
                print("\nPRODUTO NÃO ENCONTRADO!")
                print("Voltando para o Menu Produtos...")
                return
                         
    #buscar por nome
    elif (escolha == "3"):
        nomeProduto = input("Digite o nome do produto: ").strip()
        for produto in listarProdutos():
            if produto[1].lower() == nomeProduto.lower():
                print("\n--- PRODUTO ENCONTRADO ---")
                print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Valor unitário: R${produto[3]}")
            else:
                print("\nPRODUTO NÃO ENCONTRADO!")
                print("Voltando para o Menu Produtos...")
                return

    elif (escolha == "0"):
        print("Voltando para o menu Produtos...")

    else:
        print("Opção inválida.")

   

def atualizarProdutos():
    
    produtos = listarProdutos()

    print(""" \n---PRODUTOS CADRASTADOS---""")
    
    for produto in produtos:

        print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Valor unitário: R${produto[3]}")

    idBusca = input("Digite o ID do produto que deseja atualizar: ").strip()        

    encontrado = False

    for produto in produtos:

        dados = produto

        if str(dados[0]) == idBusca:

            encontrado = True

            
            print(f"\nproduto encontrado : ID: {dados[0]} | Nome: {dados[1]} | Quantidade: {dados[2]} | Valor unitario: R${dados[3]}")

            
            novoNome = input(" Digite o novo nome do produto (ou aperte enter para manter o atual): ").strip()

            novaQuantidade = input("Digite a nova quantidade do produto (ou aperte enter para manter a atual): ")
            if int(novaQuantidade) <20:
                print("A quantidade mínima de produtos é 20. voltando para o Menu Produtos.")
                return

            novoValor = input("Digite o novo valor unitário do produto (ou aperte enter para manter o atual): ").strip()

            if novoNome:
                
                    dados[1] = novoNome

            if novaQuantidade:
                
                     dados[2] = int(novaQuantidade)
            if novoValor:
                

                    dados[3] = novoValor
            break

    if not encontrado:

        print("Produto não encontrado.")

        return



    with open("produtos.txt", "w", encoding="utf-8") as arquivo:

        for produto in produtos:

            arquivo.write(f"{produto[0]};{produto[1]};{produto[2]};{produto[3]}\n")

        print("Produto atualizado com sucesso!")

     


def excluirProdutos():
    produtos = listarProdutos()

    print("\n--- PRODUTOS CADASTRADOS ---")
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Quantidade: {p[2]} | Valor unitário: R${p[3]}")

    idBusca = input("\nDigite o ID do produto que deseja excluir: ").strip()
    encontrado = False

    # Percorre a lista de produtos item por item
    for p in produtos:
        # Garante a comparação correta convertendo o ID para texto
        if str(p[0]) == idBusca:
            encontrado = True
            print(f"\nProduto encontrado: ID: {p[0]} | Nome: {p[1]} | Quantidade: {p[2]} | Valor unitário: R${p[3]}")
            
            confirmacao = input("Tem certeza que deseja excluir este produto? (s/n): ").strip().lower()
            
            if confirmacao == "s":
                # Remove o produto encontrado da lista na memória
                produtos.remove(p)
                
                # Reescreve o arquivo apenas com os produtos restantes
                with open("produtos.txt", "w", encoding="utf-8") as arquivo:
                    for prod in produtos:
                        linha = f"{prod[0]};{prod[1]};{prod[2]};{prod[3]}\n"
                        arquivo.write(linha)
                
                print("Produto excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            
            break

    if not encontrado:
        print("Produto não encontrado.")
                 



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
[2] - Buscar
[3] - Atualizar
[4] - Excluir
[0] - Voltar para o menu principal""")
        escolha = input("Escolha: ").strip()

        if (escolha == "1"):
            cadastrarClientes()

        elif (escolha == "2"):
            buscarClientes()

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

            excluirProdutos()



           

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

======= Ａｄｅｇａ Ｃｏｒｄｅｎｎｅ =======
        __________________________
        ==== MENU PRINCIPAL ====
        __________________________

           [1] - Produtos

           [2] - Clientes

           [3] - Vendas

           [4] - Relatórios

           [0] - Sair 
 ========================================""")

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