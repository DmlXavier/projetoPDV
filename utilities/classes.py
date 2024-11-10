# Classe de uma pessoa
class Person:
    def __init__(self, name, cpf):
        self.personName = name
        self.personCpf = cpf
    
    def to_dict(self):
        return {'name': self.personName, 'cpf': self.personCpf}