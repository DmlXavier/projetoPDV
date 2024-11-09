from . import classes

# Imprime o menu principal
def printMenu():
    print("MENU PRINCIPAL")
    print()
    print("[1] Cadastrar um cliente")
    print("[2] Cadastrar um vendedor")
    print("[3] Cadastrar um produto")
    print("[4] Lista de clientes cadastrados")
    print("[5] Lista de vendedores")
    print("[6] Estoque")
    print("[7] Realizar uma compra")
    print("[8] Relatório de vendas")
    print()
    
    return input("Digite o número da opção escolhida: ")

# Retorna um dicionário com os dados do cliente
def registerCustomer():
    switch = True

    while switch:
        entry = input("Digite o nome do cliente: ")
        
        if (entry.isalpha()):
            name = entry

            while switch:
                entry = input("Digite o cpf do cliente: ")

                if(entry.isdigit() and len(entry) == 11):
                    cpf = entry
                    customer = classes.Customer(name, cpf)
                    
                    return customer.to_dict()
                
                else:
                    print("ERRO! Entrada inválida!")
                    print("CPF não pode conter letras, caracteres especiais, pontuação ou espaços e deve conter apenas 11 dígitos.")
        
        else:
            print("ERRO! Entrada inválida!")
            print("Nome não pode conter números, caracteres especiais, pontuação ou espaços. Tente novamente.")


