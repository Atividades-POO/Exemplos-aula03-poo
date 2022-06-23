#
# Implemente uma classe que seja uma calculadora para
# estima qual seria a idade de uma pessoa em outros
# planetas.
# https://olhardigital.com.br/2020/09/01/ciencia-e-espaco/calculadora-estima-qual-seria-a-sua-idade-em-outros-planetas/

from datetime import date

class CalculadoraIdade:
    def __init__(self, anoNascimento):
        self.anoNascimento = anoNascimento
        self.hoje = date.today() # Atributo que recebe a data de hoje
        self.idade = self.hoje.year - self.anoNascimento # Atributo que recebe a idade calculada

    def idadeEmPlaneta(self, planeta):
        if planeta == 'Terra':
            return self.idade  # Retorna a idade calculada
        elif planeta == 'Mercurio':
            return self.idade * .24 # Mercurio é um planeta muito mais veloz que a Terra
        elif planeta == 'Venus':
            return self.idade * .62
        elif planeta == 'Marte':
            return self.idade * 1.88
        elif planeta == 'Jupiter':
            return self.idade * 11.86
        elif planeta == 'Saturno':
            return self.idade * 29.46
        elif planeta == 'Urano':
            return self.idade * 84.01
        elif planeta == 'Netuno':
            return self.idade * 164.8
        elif planeta == 'Plutao':
            return self.idade * 247.7 # Plutão é um planeta muito mais lento que a Terra