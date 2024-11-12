from utilities import functions

clients = {}
salespeople = {}
products = {}

while True:
    # Menu principal
    command = functions.printMainMenu()

    match command:
        # Cadastrar um usuário (cliente ou vendedor)
        case '1':
            selectedUser = functions.selectUserType()
            
            while True: 
                if selectedUser:
                    entry = functions.printRegisterMenu(selectedUser)

                    while selectedUser:
                        match selectedUser:
                            case 'cliente':
                                userList = clients
                            case 'vendedor':
                                userList = salespeople
                        
                        if entry == functions.isExitInput(entry):
                            selectedUser = functions.selectUserType()
                        else:
                            user = functions.collectUserInfo(entry)

                            if user:
                                functions.addUserToDict(user, userList)
                                new_entry = input(f'Deseja cadastrar outro {selectedUser}? (S/N): ').lower().strip()

                                match new_entry:
                                    case 's':
                                        entry = input(f'Digite o nome do {selectedUser}: ').strip()
                                    case 'n':
                                        selectedUser = functions.selectUserType()
                                        break
                                    case _:
                                        print()
                                        print('ERRO! Comando inválido. Voltando ao menu de cadastro de usuário.')
                                        selectedUser = functions.selectUserType()
                                        break
                            else:
                                selectedUser = functions.selectUserType()
                else:
                    break
        
        # Cadastrar um produto
        case '2':
            switch = 1
            entry = functions.printRegisterMenu('produto')

            while switch:
                match entry:
                    case 's':
                        product = functions.collectProductInfo()
                        
                        if product:
                            functions.addProductToDict(product, products)
                            new_entry = input("Deseja cadastrar outro produto? (S/N): ").lower().strip()

                            match new_entry:
                                case 's':
                                    entry = new_entry
                                case 'n':
                                    switch = 0
                                case _:
                                    print()
                                    print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                    entry = functions.printRegisterMenu('produto')
                        else:
                            switch = 0
                    case _:
                        if entry == 'n' or functions.isExitInput(entry):
                            switch = 0
                        else:
                            print()
                            print('ERRO! Comando inválido. Tente novamente.')
                            entry = input('Cadastrar um produto? (S/N): ').lower().strip()
        
        # Encerrar o programa
        case '0':
            break