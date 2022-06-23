# importe a classe dataetime
from datetime import date

# crie uma classe colaborador
#
class Colaborador:
    def __init__(self, nome, cargo = 'vendedor', cpf = '1234567890', anoNascimento = 0): # Construtor ou inicializador
        self.nome = nome # Atributo
        self.cargo = cargo
        self.cpf = cpf
        self.anoNascimento = anoNascimento
        self.hoje = date.today() # Atributo que recebe a data de hoje
        # Calcula a idade do colaborador por aqui já no atributo ou também pode ser no método de instância
        self.idade = self.hoje.year - self.anoNascimento # Atributo que recebe a idade calculada

    def imprime(self): # Método de instância
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"CPF: {self.cpf}")
        print(f"Ano de Nascimento: {self.anoNascimento}")
        print(f"Idade: {self.idade}")
        print(f"Data de Hoje: {self.hoje}")

    def calculaIdade(self): # Método de instância
        # Calcula a idade do colaborador
        return f"{self.nome}] tem {self.hoje.year - self.anoNascimento} anos" # Retorna a idade calculada

    def futuro(self): # método para ser implementado no futuro
        pass
