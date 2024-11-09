# Classe do cliente
class Customer:
    def __init__(self, name, cpf):
        self.customerName = name
        self.customerCpf = cpf
    
    def to_dict(self):
        return {'name': self.customerName, 'cpf': self.customerCpf}