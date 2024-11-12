from utilities import functions

clients = {}
salespeople = {}
products = {}
mainSwitch = 1

while mainSwitch:
    # Menu principal
    command = functions.printMainMenu()

    match command:
        # Cadastrar um cliente
        case '1':
            switch = 1
            entry = functions.printRegisterMenu('cliente')

            while switch:
                match entry:
                    case 's':
                        client = functions.collectUserInfo()

                        if client:
                            functions.addUserToDict(client, clients)
                            new_entry = input("Deseja cadastrar outro cliente? (S/N): ").lower().strip()

                            match new_entry:
                                case 's':
                                    entry = new_entry
                                case 'n':
                                    switch = 0
                                case _:
                                    print()
                                    print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                    entry = functions.printRegisterMenu('cliente')
                        else:
                            switch = 0
                    case _:
                        if entry == 'n' or functions.isExitInput(entry):
                            switch = 0
                        else:
                            print()
                            print('ERRO! Comando inválido. Tente novamente.')
                            entry = input('Cadastrar um cliente? (S/N): ').lower().strip()
        
        # Cadastrar um vendedor
        case '2':
            switch = 1
            entry = functions.printRegisterMenu('vendedor')

            while switch:
                match entry:
                    case 's':
                        salesperson = functions.collectUserInfo()
                        
                        if salesperson:
                            functions.addUserToDict(salesperson, salespeople)
                            new_entry = input("Deseja cadastrar outro vendedor? (S/N): ").lower().strip()

                            match new_entry:
                                case 's':
                                    entry = new_entry
                                case 'n':
                                    switch = 0
                                case _:
                                    print()
                                    print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                    entry = functions.printRegisterMenu('vendedor')
                        else:
                            switch = 0
                    case _:
                        if entry == 'n' or functions.isExitInput(entry):
                            switch = 0
                        else:
                            print()
                            print('ERRO! Comando inválido. Tente novamente.')
                            entry = input('Cadastrar um vendedor? (S/N): ').lower().strip()
        
        # Cadastrar um produto
        case '3':
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