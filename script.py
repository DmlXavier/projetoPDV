from utilities import functions

clientes = {}
vendedores = {}
produtos = {}
mainSwitch = 1

while mainSwitch:
    command = functions.printMainMenu()

    match command:
        case "1":
            registerCustomerSwitch = 1
            entry = functions.printCustomerMenu()

            while registerCustomerSwitch:
                match entry:
                    case 's':
                        customer = functions.createUser()
                        functions.addUserToDict(customer, clientes)
                        print(clientes)
                        
                        entry2 = input("Deseja cadastrar outro cliente? (S/N): ").lower()

                        match entry2:
                            case 's':
                                entry = entry2
                            
                            case 'n':
                                registerCustomerSwitch = 0
                            
                            case _:
                                print()
                                print('ERRO! Comando inválido. Voltando ao menu de cadastro.')
                                command = '1'
                    
                    case 'n':
                        registerCustomerSwitch = 0
                    
                    case _:
                        print()
                        print('ERRO! Comando inválido. Tente novamente.')

                        command = '1'