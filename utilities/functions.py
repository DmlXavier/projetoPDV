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
    
    return input("Digite o número da opção escolhida: ")

# Mostra o menu de cadastro
def printRegisterMenu(typeOfUser):
        print()
        print(f'CADASTRO DE {typeOfUser.upper()}')
        print()
        return input(f'Cadastrar um {typeOfUser}? (S/N): ').lower()

# Retorna um dicionário com os dados do usuário cadastrado
def createUser():
    while True:
        entry = input("Digite o nome do usuário: ")
        
        if entry.isalpha():
            name = entry

            while True:
                entry = input("Digite o cpf do usuário: ")

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