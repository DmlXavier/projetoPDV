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
    # Valida a entrada do nome do usuário
    def validateUserName(entry):
        if entry.replace(' ', '').isalpha():
            return entry.title()
        elif entry == '':
            print()
            print("ERRO! Entrada inválida!")
            print("O campo não pode estar vazio.")
            print("Exemplo: Nome Sobrenome")
            
            return
        else:
            print()
            print("ERRO! Entrada inválida!")
            print("Nome não pode conter números, caracteres especiais ou pontuação.")
            print("Exemplo: Nome Sobrenome")
            
            return
        
    # Valida a entrada do CPF do usuário
    def validateCpf(entry):
        if entry.isdigit() and len(entry) == 11:
            return entry
        elif entry == '':
            print()
            print("ERRO! Entrada inválida!")
            print("O campo não pode estar vazio.")
            print("Exemplo: 01234567890")
            
            return
        else:
            print()
            print("ERRO! Entrada inválida!")
            print("CPF não pode conter letras, caracteres especiais, pontuação ou espaços e deve conter apenas 11 dígitos.")
            print("Exemplo: 01234567890")
            
            return

    while True:
        entry = input("Digite o nome do usuário: ").strip()
        
        if isExitInput(entry):
            return
        else:
            name = validateUserName(entry)

            if name:
                while True:
                    entry = input("Digite o cpf do usuário: ").strip()
                   
                    if isExitInput(entry):
                        return
                    else:
                        cpf = validateCpf(entry)

                        if cpf:
                            user = classes.Person(name, cpf)
                            return user.to_dict()

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
    # Converte uma string (se possível) em int ou float
    def parseNumber(entry, numberType):
        try:
            if numberType == 'int':
                return int(entry)
            elif numberType == 'float':
                return float(entry)
        except ValueError:
            return
    
    # Valida a entrada do nome do produto
    def validateProductName(entry):
        if entry.replace(' ', '').isalpha():
            return entry.capitalize()
        elif entry == '':
            print()
            print("ERRO! Entrada inválida!")
            print("O campo não pode estar vazio.")
            print("Exemplo: Novo produto")
            
            return
        else:
            print()
            print("ERRO! Entrada inválida!")
            print("Nome não pode conter números, caracteres especiais ou pontuação.")
            print("Exemplo: Novo produto")
            
            return
    
    # Valida a entrada da quantidade do produto
    def validateProductQuantity(entry):
        entry = parseNumber(entry, 'int')

        if entry:
            if entry > 0:
                return entry
            else:
                print()
                print("ERRO! Entrada inválida!")
                print("Quantidade não pode ser menor ou igual a zero.")
                print("Exemplo: 5")

                return
        elif entry == '':
            print()
            print("ERRO! Entrada inválida!")
            print("O campo não pode estar vazio.")
            print("Exemplo: 5")
            
            return
        else:
            print()
            print("ERRO! Entrada inválida!")
            print("Quantidade não pode conter letras, caracteres especiais, pontuação ou espaços e deve ser um número inteiro.")
            print("Exemplo: 5")

            return
    
    # Valida a entrada do preço do produto
    def validateProductPrice(entry):
        entry = parseNumber(entry, 'float')

        if entry:
            if entry > 0:
                return round(entry, 2)
            else:
                print()
                print("ERRO! Entrada inválida!")
                print("Preço não pode ser menor ou igual a zero.")
                print("Exemplo: 5.00")

                return
        elif entry == '':
            print()
            print("ERRO! Entrada inválida!")
            print("O campo não pode estar vazio.")
            print("Exemplo: 5.50")
            
            return
        else:
            print()
            print("ERRO! Entrada inválida!")
            print("Preço não pode conter letras, caracteres especiais ou espaços e deve ser um número decimal, com até duas casas decimais.")
            print("Exemplo: 5.50")

            return

    while True:
        entry = input('Digite o nome do produto: ').strip()

        if isExitInput(entry):
            return
        else:
            name = validateProductName(entry)

            if name:
                while True:
                    entry = input('Digite a quantidade: ').strip()
                        
                    if isExitInput(entry):
                        return
                    else:
                        quantity = validateProductQuantity(entry)
                            
                        if quantity:
                            while True:
                                entry = input('Digite o preço: ').strip()
                                                
                                if isExitInput(entry):
                                    return
                                else:
                                    price = validateProductPrice(entry)

                                    if price:
                                        product = classes.Product(name, quantity, price)    
                                        return product.to_dict()
                                        
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