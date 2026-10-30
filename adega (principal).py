import produtos


listaClientes = []
listaVendas = []



def buscarProdutos():
    produtos.listaProdutos.clear() #Limpando a lista para não duplicar
    with open("Produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            produtos.listaProdutos.append(linha.strip())
    print(f"Produtos que já estão cadastrados: {produtos.listaProdutos}")


 
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
        escolha = input("Escolha: ")

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
        escolha = input("Escolha: ")

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
        escolha = input("Escolha: ")
        if (escolha == "1"):
            produtos.cadastrarProdutos()
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

#MENU PRINCIPAL
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
        escolha = input("Escolha: ")
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
