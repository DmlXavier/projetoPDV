from utilities import functions

command = functions.printMenu()

if (command == "1"):
    client = functions.registerCustomer()
    print(client)