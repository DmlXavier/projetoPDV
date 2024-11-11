from . import classes

# Mostra o menu principal
def printMainMenu():
    print()
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
    print("[0] Sair")
    print()
    
    return input("Digite o número da opção escolhida: ").strip()

# Mostra o menu de cadastro
def printRegisterMenu(typeOfUser):
        print()
        print(f'CADASTRO DE {typeOfUser.upper()}')
        print()
        return input(f'Cadastrar um {typeOfUser}? (S/N): ').lower().strip()

# Coleta as informações do usuário a ser cadastrado
def collectUserInfo():
    while True:
        entry = input("Digite o nome do usuário: ").strip()
        
        if entry.isalpha():
            name = entry

            while True:
                entry = input("Digite o cpf do usuário: ").strip()

                if entry.isdigit() and len(entry) == 11:
                    cpf = entry
                    user = classes.Person(name, cpf)
                    return user.to_dict()
                
                else:
                    print()
                    print("ERRO! Entrada inválida!")
                    print("CPF não pode conter letras, caracteres especiais, pontuação ou espaços e deve conter apenas 11 dígitos.")
                    print("Exemplo: 01234567890")
        
        else:
            print()
            print("ERRO! Entrada inválida!")
            print("Nome não pode conter números, caracteres especiais, pontuação ou espaços.")
            print("Exemplo: NomeSobrenome")
            
# Adiciona o usuário a um dicionário
def addUserToDict(user, dictionary):
    for key in dictionary.keys():
        if user["cpf"] == key:
            print()
            print('ERRO! Usuário já cadastrado.')

            return

    dictionary[f'{user["cpf"]}'] = user
    
    print()
    print('Usuário cadastrado com sucesso!')

    return dictionary

# Coleta as informações do produto a ser cadastrado
def collectProductInfo():
    while True:
        entry = input('Digite o nome do produto: ').strip()

        if entry.isalpha():
            name = entry

            while True:
                entry = input('Digite a quantidade: ').strip()
                
                try:
                    int(entry)
                except ValueError:
                    print()
                    print("ERRO! Entrada inválida!")
                    print("Quantidade não pode conter letras, caracteres especiais, pontuação ou espaços e deve ser um número inteiro.")
                    print("Exemplo: 5")
                else:
                    quantity = int(entry)

                    while True:
                        entry = input('Digite o preço: ').strip()

                        try:
                            float(entry)
                        except ValueError:
                            print()
                            print("ERRO! Entrada inválida!")
                            print("Preço não pode conter letras, caracteres especiais ou espaços e deve ser um número decimal ou inteiro.")
                            print("Exemplo: 5.00")
                        else:
                            price = round(float(entry), 2)
                            product = classes.Product(name, quantity, price)
                            
                            return product.to_dict()
        else:
            print()
            print("ERRO! Entrada inválida!")
            print("Nome não pode conter números, caracteres especiais, pontuação ou espaços.")
            print("Exemplo: Produto")

# Adiciona o produto a um dicionário
def addProductToDict(product, dictionary):
    for key in dictionary.keys():
        if product["name"] == key:
            print()
            print('ERRO! Produto já cadastrado.')

            return
    
    dictionary[f'{product["name"]}'] = product

    print()
    print('Produto cadastrado com sucesso!')

    return dictionary