# Classe de uma pessoa
class Person:
    def __init__(self, name, cpf):
        self.personName = name
        self.personCpf = cpf
    
    def to_dict(self):
        return {'name': self.personName, 'cpf': self.personCpf}
    
# Classe de um produto
class Product:
    def __init__(self, name, quantity, price):
        self.productName = name
        self.productQuantity = quantity
        self.productPrice = price
    
    def to_dict(self):
        return {'name': self.productName, 'quantity': self.productQuantity, 'price': self.productPrice}