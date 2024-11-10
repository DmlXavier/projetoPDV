from utilities import functions

clients = {}
salespeople = {}
products = {}
mainSwitch = 1

while mainSwitch:
    command = functions.printMainMenu()

    match command:
        case "1":
            switch = 1
            entry = functions.printRegisterMenu('cliente')

            while switch:
                match entry:
                    case 's':
                        functions.addUserToDict(functions.createUser(), clients)
                        entry2 = input("Deseja cadastrar outro cliente? (S/N): ").lower()

                        match entry2:
                            case 's':
                                entry = entry2
                            
                            case 'n':
                                switch = 0
                            
                            case _:
                                print()
                                print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                command = '1'
                    
                    case 'n':
                        switch = 0
                    
                    case _:
                        print()
                        print('ERRO! Comando inválido. Tente novamente.')

                        command = '1'
        
        case '2':
            switch = 1
            entry = functions.printRegisterMenu('vendedor')

            while switch:
                match entry:
                    case 's':
                        functions.addUserToDict(functions.createUser(), salespeople)
                        entry2 = input("Deseja cadastrar outro vendedor? (S/N): ").lower()

                        match entry2:
                            case 's':
                                entry = entry2
                            
                            case 'n':
                                switch = 0
                            
                            case _:
                                print()
                                print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                command = '1'
                    
                    case 'n':
                        switch = 0
                    
                    case _:
                        print()
                        print('ERRO! Comando inválido. Tente novamente.')

                        command = '1'