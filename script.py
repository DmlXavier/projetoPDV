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
                        functions.addUserToDict(client, clients)
                        entry2 = input("Deseja cadastrar outro cliente? (S/N): ").lower().strip()

                        match entry2:
                            case 's':
                                entry = entry2
                            case 'n':
                                switch = 0
                            case _:
                                print()
                                print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                entry = functions.printRegisterMenu('cliente')
                    case 'n':
                        switch = 0
                    case _:
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
                        functions.addUserToDict(salesperson, salespeople)
                        entry2 = input("Deseja cadastrar outro vendedor? (S/N): ").lower().strip()

                        match entry2:
                            case 's':
                                entry = entry2
                            case 'n':
                                switch = 0
                            case _:
                                print()
                                print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                entry = functions.printRegisterMenu('vendedor')
                    case 'n':
                        switch = 0
                    case _:
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
                        functions.addProductToDict(product, products)
                        entry2 = input("Deseja cadastrar outro produto? (S/N): ").lower().strip()

                        match entry2:
                            case 's':
                                entry = entry2
                            case 'n':
                                switch = 0
                            case _:
                                print()
                                print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                entry = functions.printRegisterMenu('produto')
                    case 'n':
                        switch = 0
                    case _:
                        print()
                        print('ERRO! Comando inválido. Tente novamente.')
                        entry = input('Cadastrar um produto? (S/N): ').lower().strip()