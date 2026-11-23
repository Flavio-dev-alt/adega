adega ="c:\\Users\\gusta\\Downloads\\Projeto.py"

arquivo = open(adega, "a", encoding="utf-8")
open("produtos.txt", "a", encoding="utf-8").close()
open("clientes.txt", "a", encoding="utf-8").close()
open("vendas.txt", "a", encoding="utf-8").close()

def relatoriosProdutos():
    print("Produtos em estoque:")
    for produto in listarProdutos():
        if (produto[2] > 0):
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Valor unitário: R${produto[3]}")

def relatoriosVendas():
    soma = 0
    print("Vendas realizadas:")
    for venda in listarVendas():
        print(f"ID: {venda[0]} | Cliente: {venda[1]} | Produto: {venda[2]} | Quantidade: {venda[3]} | Valor total: R$ {venda[4]}")
        soma += float(venda[4])
    print(f"Valor total das vendas: R${soma:.2f}")

def listarVendas():
    vendas = []

    with open("vendas.txt", "r", encoding="utf-8") as arquivoListarVendas:
        for linha in arquivoListarVendas:
            if (linha.strip()):
                dadosVenda = linha.split(";")
                idVenda = int(dadosVenda[0])
                nomeClienteVen = dadosVenda[1]
                produtoVen = dadosVenda[2]
                qntProdutoVen = int(dadosVenda[3])
                valorTotalVen = float(dadosVenda[4])

                vendas.append([idVenda, nomeClienteVen, produtoVen, qntProdutoVen, valorTotalVen])

    return (vendas)

def cadastrarVendas():
    print("Clientes cadastrados:")
    for cliente in listarClientes():
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]}")
        
    idCliente = input("Digite o ID do cliente que vai comprar: ").strip()
    
    for cliente in listarClientes():
        if (int(idCliente) == int(cliente[0])):
            print("Cliente encontrado")
            break
    else:
        print("Cliente não encontrado")
        return 

    print("Produtos:")
    for produto in listarProdutos():
        print(f"ID: {produto[0]} | Produto: {produto[1]} | Qnt: {produto[2]} | Valor: R$ {produto[3]}")
        
    nomeProduto = input("Digite o nome do produto que vai comprar: ").strip()   

    listaDasVen = listarVendas()

    if len(listaDasVen) == 0:
        idVenda = 1
    else:
        maiorId = 0
        for venda in listaDasVen:
            if venda[0] > maiorId:
                maiorId = venda[0]
        idVenda = maiorId + 1
        
    produtos = listarProdutos() 

    with open("vendas.txt", "a", encoding="utf-8") as arquivoCadasVen:
        for produto in produtos :
            if (nomeProduto.lower() == produto[1].lower()):
                print("Produto encontrado")
                qntProduto = int(input(f"Digite a quantidade de {nomeProduto} você quer levar: "))
                
                if (qntProduto > int(produto[2])):
                    print("Não há estoque suficiente")
                    return
                elif (qntProduto <= 0):
                    print("Quantidade inválida")
                    return
                
                arquivoCadasVen.write(f"{idVenda};{cliente[1]};{produto[1]};{qntProduto};{float(produto[3]) * qntProduto}\n")
                print("Venda cadastrada")
                print(f"ID: {idVenda} | Cliente: {cliente[1]} | Produto: {produto[1]} | Quantidade: {qntProduto} | Valor total: R$ {float(produto[3]) * qntProduto}")

                            
                produto[2] = produto[2] - qntProduto
                with open("produtos.txt", "w", encoding="utf-8") as arquivoCadasPro:
                    for p in produtos:
                        arquivoCadasPro.write(f"{p[0]};{p[1]};{p[2]};{p[3]}\n")
                            
                break
        else:
            print("Produto não encontrado.")

def buscarVendas():
    print("""
    ---- OPÇÕES DE BUSCA ----
    1 - Mostrar todas as vendas cadastradas
    2 - Buscar vendas por ID
    3 - Buscar vendas por nome do cliente
    0 - Voltar para o Menu Vendas""")

    escolha = input("Digite a opção desejada: ").strip()
    vendas = listarVendas()
    # pra mostrar todos 
    if (escolha == "1"):
        print("""\n---VENDAS CADRASTADAS---""")
        for venda in vendas:
            print(f"ID: {venda[0]} | Cliente: {venda[1]} | Produto: {venda[2]} | Quantidade: {venda[3]} | Valor total: R$ {venda[4]}")

    #buscar por id
    elif (escolha == "2"):
        idVenda =input("Digite o ID da venda: ").strip()
        for venda in vendas:
            if (str(venda[0]) == idVenda):
                print("\n--- VENDA ENCONTRADA ---")
                print(f"ID: {venda[0]} | Cliente: {venda[1]} | Produto: {venda[2]} | Quantidade: {venda[3]} | Valor total: R$ {venda[4]}")
                break
        else:
            print("\nID DE VENDA NÃO ENCONTRADO!")
            print("Voltando para o Menu Vendas...")
            return

    # buscar pelo nome  
    elif (escolha == "3"):
        nomeClienteVenda = input("Digite o nome do cliente da venda: ").strip()
        for venda in vendas:
            if (nomeClienteVenda.lower() == venda[1].lower()):
                print("\n--- VENDA ENCONTRADA ---")
                print(f"ID: {venda[0]} | Cliente: {venda[1]} | Produto: {venda[2]} | Quantidade: {venda[3]} | Valor total: R$ {venda[4]}")
                break
        else:
            print("\nNOME DO CLIENTE NÃO ENCONTRADO NA VENDA!")
            print("Voltando para o Menu Vendas...")
            return

    elif (escolha == "0"):
        print("Voltando para o Menu Vendas...")
        return

    else:
        print("Opção inválida.")
        return
        
def atualizarVendas():
    vendas = listarVendas()
    print("Vendas cadastradas:")
    for venda in vendas:
        print(f"ID: {venda[0]} | Comprador: {venda[1]} | Produto: {venda[2]} | Qnt: {venda[3]} | Total: R${venda[4]}")

    idVenda = input("Digite o ID da venda que deseja atualizar: ").strip()

    for venda in vendas:
        if (int(idVenda) == int(venda[0])):
            print("Venda encontrada")

            produtoAntigo = venda[2]
            qntAntiga = int(venda[3])

            novoCliente = input("Novo cliente: ").strip()
            if (novoCliente != ""):
                venda[1] = novoCliente

            novoProduto = input("Novo produto: ").strip()
            
            produtos = listarProdutos()
            
            for p in produtos:
                if (p[1].lower() == produtoAntigo.lower()):
                    p[2] += qntAntiga
                    break

            for produto in produtos:
                if (novoProduto.lower() == produto[1].strip().lower()):
                    novaQnt = int(input("Nova quantidade: "))

                    if (novaQnt <= 0) or (novaQnt > int(produto[2])):
                        print("Quantidade inválida ou estoque insuficiente")
                        return

                    venda[2] = produto[1].strip()
                    venda[3] = novaQnt
                    venda[4] = novaQnt * float(produto[3])
                    
                    produto[2] -= novaQnt
                    break
            else:
                print("Produto não encontrado")
                return

            with open("vendas.txt", "w", encoding="utf-8") as arquivoVendas:
                for v in vendas:
                    arquivoVendas.write(f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]}\n")

            with open("produtos.txt", "w", encoding="utf-8") as arquivoProdutos:
                for p in produtos:
                    arquivoProdutos.write(f"{p[0]};{p[1]};{p[2]};{p[3]}\n")

            print("Venda atualizada e estoque sincronizado com sucesso!")
            break
    else:
        print("Venda não encontrada")

def excluirVendas():
    vendas = listarVendas()

    print("\n--- VENDAS CADASTRADAS ---")
    for venda in vendas:
        print(f"ID: {venda[0]} | Cliente: {venda[1]} | Produto: {venda[2]} | Quantidade: {venda[3]} | Valor total: R$ {venda[4]}")

    idBuscvnd = input("\nDigite o ID da venda que deseja excluir: ").strip()
    encontrado = False

    for venda in vendas:
        if (str(venda[0]) == idBuscvnd):
            encontrado = True
            print(f"\nVenda encontrada: ID: {venda[0]} | Cliente: {venda[1]} | Produto: {venda[2]} | Quantidade: {venda[3]} | Valor total: R$ {venda[4]}")
            
            confirmacao = input("Tem certeza que deseja excluir esta venda? (s/n): ").strip().lower()
            
            if (confirmacao == "s"):
                produtos = listarProdutos()
                for p in produtos:
                    if (p[1].lower() == venda[2].lower()):
                        p[2] += int(venda[3])
                        break
                
                with open("produtos.txt", "w", encoding="utf-8") as arquivoCadasPro:
                    for p in produtos:
                        arquivoCadasPro.write(f"{p[0]};{p[1]};{p[2]};{p[3]}\n")

                vendas.remove(venda)
                
                with open("vendas.txt", "w", encoding="utf-8") as arquivoExVenda:
                    for v in vendas:
                        arquivoExVenda.write(f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]}\n")
                
                print("Venda excluída!")
            else:
                print("Exclusão cancelada.")
            
            break

    if (not encontrado):
        print("Venda não encontrada.")
      
def listarClientes():
    clientes = []

    with open("clientes.txt", "r", encoding="utf-8") as arquivoListarCli:
        for linha in arquivoListarCli:
            if (linha.strip()):
                dadosCli = linha.split(";")
                idCli = int(dadosCli[0])
                nomeCli = dadosCli[1]
                idadeCli = dadosCli[2].strip()

                clientes.append([idCli, nomeCli, idadeCli])
    
    return (clientes)

def cadastrarClientes():
    with open("clientes.txt", "a", encoding="utf-8") as arquivoCadasCli:
        nome = input("Nome do cliente: ")
        idade = int(input(f"Idade do(a) {nome}: "))
        if (idade < 18):
            print("Cliente não pode ser cadastrado. Apenas se tiver 18 anos ou mais.")
            print("Voltando para o Menu Clientes...")
            return

        listaDosCl = listarClientes()

        if (len(listaDosCl) == 0):
            idCliente = 1
        else:
            maiorId = 0
            for cliente in listaDosCl:
                if (cliente[0] > maiorId):
                    maiorId = cliente[0]
            idCliente = maiorId + 1
                
        arquivoCadasCli.write(f"{idCliente};{nome};{idade}\n")
        print(f"\nCliente '{nome}' cadastrado com sucesso! (ID: {idCliente})")

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
    elif (escolha == "2"):
        idCliente = int(input("Digite o ID do cliente: ").strip())
        for cliente in listarClientes():
            if (cliente[0] == idCliente):
                print("\n--- CLIENTE ENCONTRADO ---")
                print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]}")
                break
        else:
            print("\nID DE CLIENTE NÃO ENCONTRADO!")
            print("Voltando para o Menu Clientes...")
            return

    #buscar por nome
    elif (escolha == "3"):
        nomeCliente = input("Digite o nome do cliente: ").strip()
        for cliente in listarClientes():
            if (nomeCliente.lower() == cliente[1].lower()):
                print("\n--- CLIENTE ENCONTRADO ---")
                print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]}")
                break
        else:
            print("\nNOME DO CLIENTE NÃO ENCONTRADO!")
            print("Voltando para o Menu Clientes...")
            return

def atualizarClientes():
    clientes = listarClientes()

    print("""\n---CLIENTES CADRASTADOS---""")
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]}| Idade: {cliente[2]}")

    idBuscaCliente = input("Digite o ID do cliente que quer atualizar: ").strip()

    for cliente in clientes:
        if (int(idBuscaCliente) == int(cliente[0])):
            print("----CLIENTE ENCONTRADO----")
            novoNome = input("Novo nome: ")
            novaIdade = int(input("Nova idade: "))
            if (novaIdade < 18):
                print("Só pode cadastrar maiores ou iguais a 18.")
                print("Voltando para o Menu Clientes...")
                return

            if (novoNome != ""):
                cliente[1] = novoNome
            if (novaIdade >= 18):
                cliente[2] = novaIdade
            break 
    else:
        print("ID não encontrado")
        print("Voltando para o Menu Clientes...")
        return

    with open("clientes.txt", "w", encoding="utf-8") as arquivoAtualiCli:
        for cliente in clientes:
            arquivoAtualiCli.write(f"{cliente[0]};{cliente[1]};{cliente[2]}\n")
            
            
def excluirClientes():
    clientes = listarClientes()

    print("\n--- CLIENTES CADASTRADOS ---")
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]}")

    idBuscaCliente = input("\nDigite o ID do cliente que deseja excluir: ").strip()
    encontrado = False

    for cliente in clientes:
        if (str(cliente[0]) == idBuscaCliente):
            encontrado = True
            print(f"\nCliente encontrado: ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]}")

            confirmacao = input("Tem certeza que deseja excluir este cliente? (s/n): ").strip().lower()
            
            if (confirmacao == "s"):
                clientes.remove(cliente)
                
                with open("clientes.txt", "w", encoding="utf-8") as arquivoExCli:
                    for cli in clientes:
                        arquivoExCli.write(f"{cli[0]};{cli[1]};{cli[2]}\n")
                
                print("Cliente excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            
            break

    if (not encontrado):
        print("Cliente não encontrado.")

def listarProdutos():
    produtos = []
    with open("produtos.txt", "r", encoding="utf-8") as arquivo:        
        for linha in arquivo:
            if (linha.strip()):
                dados = linha.split(";")
                idProduto = int(dados[0])
                nome = dados[1]
                qnt = int(dados[2])
                valor = float(dados[3])
                produtos.append([idProduto, nome, qnt, valor])
    return (produtos)



def cadastrarProdutos():
    produto = input("Digite o nome do produto: ").strip()
    qntProdutoStr = input("Quantidade do produto: ").strip()
    
    if (qntProdutoStr == ""):
        print("Quantidade inválida.")
        return
        
    qntProduto = int(qntProdutoStr)
    if (qntProduto < 20):
        print("A quantidade mínima de produtos é 20. Voltando para o Menu Produtos.")
        return

    valorUniStr = input("Valor unitário do produto: R$").strip().replace(",", ".")
    if (valorUniStr == ""):
        print("Valor inválido.")
        return
        
    valorUni = float(valorUniStr)
    
    listaP = listarProdutos()

    if (len(listaP) == 0):
        idProdutoroduto = 1
    else:
        maiorId = 0
        for p in listaP:
            if (p[0] > maiorId):
                maiorId = p[0]
        idProdutoroduto = maiorId + 1
    
    with open("produtos.txt", "a", encoding="utf-8") as arquivoProdutos:
        arquivoProdutos.write(f"{idProdutoroduto};{produto};{qntProduto};{valorUni}\n")

    print(f"\nProduto '{produto}' cadastrado com sucesso! (ID: {idProdutoroduto})")


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
            if (str(produto[0]) == idProduto):
                print("\n--- PRODUTO ENCONTRADO ---")
                print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Valor unitário: R${produto[3]}")
                break
        else:
            print("\nPRODUTO NÃO ENCONTRADO!")
            print("Voltando para o Menu Produtos...")
            
                         
    #buscar por nome
    elif (escolha == "3"):
        nomeProduto = input("Digite o nome do produto: ").strip()
        for produto in listarProdutos():
            if (produto[1].lower() == nomeProduto.lower()):
                print("\n--- PRODUTO ENCONTRADO ---")
                print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Valor unitário: R${produto[3]}")
                break
    
        else:
            print("\nPRODUTO NÃO ENCONTRADO!")
            print("Voltando para o Menu Produtos...")
        

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
        if (str(dados[0]) == idBusca):
            encontrado = True
            
            print(f"\nProduto encontrado : ID: {dados[0]} | Nome: {dados[1]} | Quantidade: {dados[2]} | Valor unitario: R${dados[3]}")
            
            novoNome = input(" Digite o novo nome do produto (ou aperte enter para manter o atual): ").strip()
            novaQuantidade = input("Digite a nova quantidade do produto (ou aperte enter para manter a atual): ")
            if (novaQuantidade == ""):
                novaQuantidade = dados[2]
            if (int(novaQuantidade) < 20):
                print("A quantidade mínima de produtos é 20. voltando para o Menu Produtos.")
                return

            novoValor = input("Digite o novo valor unitário do produto (ou aperte enter para manter o atual): ").strip()

            if (novoNome):
                dados[1] = novoNome

            if (novaQuantidade):
                dados[2] = int(novaQuantidade)

            if (novoValor):
                dados[3] = float(novoValor)
            break

    if (not encontrado):
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

    for p in produtos:
        if (str(p[0]) == idBusca):
            encontrado = True
            print(f"\nProduto encontrado: ID: {p[0]} | Nome: {p[1]} | Quantidade: {p[2]} | Valor unitário: R${p[3]}")
            
            confirmacao = input("Tem certeza que deseja excluir este produto? (s/n): ").strip().lower()
            
            if (confirmacao == "s"):
                produtos.remove(p)
                
                with open("produtos.txt", "w", encoding="utf-8") as arquivo:
                    for prod in produtos:
                        linha = f"{prod[0]};{prod[1]};{prod[2]};{prod[3]}\n"
                        arquivo.write(linha)
                
                print("Produto excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            
            break

    if (not encontrado):
        print("Produto não encontrado.")
                 



def menuRelatorios():
    escolha= ""
    while (escolha != "0"):
        print("""

----- RELATÓRIOS -----

[1] - Relatório de produtos em estoque

[2] - Relatório de valor total das vendas realizadas

[0] - Voltar para o menu principal""")

        escolha = input("Escolha:").strip()

        if (escolha == "1"):                 
            relatoriosProdutos()

        elif (escolha == "2"):             
            relatoriosVendas()

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
            cadastrarVendas()

        elif (escolha == "2"):
            atualizarVendas()
                
        elif (escolha == "3"):
            buscarVendas()

        elif (escolha == "4"):
            excluirVendas()                 

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
            atualizarClientes()

        elif (escolha == "4"): 
            excluirClientes()

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
            continue

menuPrincipal()
print("Programa finalizado.")
