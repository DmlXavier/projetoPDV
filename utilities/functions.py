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
        print('Digite "sair" para voltar ao menu principal')
        print()
        return input(f'Cadastrar um {typeOfUser}? (S/N): ').lower().strip()

# Retorna True se o input for "sair"
def isExitInput(entry):
    return entry.lower() == 'sair'

# Coleta as informações do usuário a ser cadastrado
def collectUserInfo():
    while True:
        entry = input("Digite o nome do usuário: ").strip()
        
        if isExitInput(entry):
            return
        else:
            if entry.replace(' ', '').isalpha():
                name = entry.title()

                while True:
                    entry = input("Digite o cpf do usuário: ").strip()
                   
                    if isExitInput(entry):
                        return
                    else:
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
                print("Exemplo: Nome Sobrenome")
            
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

# Verifica se o input é válido (int e float)
def getValidInput(entry, inputType):
    try:
        if inputType == 'int':
            return int(entry)
        elif inputType == 'float':
            return float(entry)
    except ValueError:
        return

# Coleta as informações do produto a ser cadastrado
def collectProductInfo():
    while True:
        entry = input('Digite o nome do produto: ').strip()

        if isExitInput(entry):
            return
        else:
            if entry.replace(' ', '').isalpha():
                name = entry.capitalize()

                while True:
                    entry = input('Digite a quantidade: ').strip()
                    
                    if isExitInput(entry):
                        return
                    else:
                        quantity = getValidInput(entry, 'int')
                    
                        if quantity:
                            if quantity > 0:
                                while True:
                                    entry = input('Digite o preço: ').strip()
                                    
                                    if isExitInput(entry):
                                        return
                                    else:
                                        price = getValidInput(entry, 'float')

                                        if price:
                                            if price > 0:
                                                price = round(price, 2)
                                                product = classes.Product(name, quantity, price)
                                                
                                                return product.to_dict()
                                            else:
                                                print()
                                                print("ERRO! Entrada inválida!")
                                                print("Preço não pode ser menor ou igual a zero.")
                                                print("Exemplo: 5.00")
                                        else:
                                            print()
                                            print("ERRO! Entrada inválida!")
                                            print("Preço não pode conter letras, caracteres especiais ou espaços e deve ser um número decimal, com até duas casas decimais.")
                                            print("Exemplo: 5.00")
                            else:
                                print()
                                print("ERRO! Entrada inválida!")
                                print("Quantidade não pode ser menor ou igual a zero.")
                                print("Exemplo: 5") 
                        else:
                            print()
                            print("ERRO! Entrada inválida!")
                            print("Quantidade não pode conter letras, caracteres especiais, pontuação ou espaços e deve ser um número inteiro.")
                            print("Exemplo: 5")
            else:
                print()
                print("ERRO! Entrada inválida!")
                print("Nome não pode conter números, caracteres especiais, pontuação.")
                print("Exemplo: Novo produto")

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