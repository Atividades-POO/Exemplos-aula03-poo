#
# criar a classe pessoa
class Pessoa:
  pessoa1 = "padrão"
  # pessoa1 faz referência ao atributo nome da classe
  # pessoa1 é um atributo dp escorpo global da classe Pessoa
  # pessoa1 é instanciado no escopo global da classe Pessoa

  def __init__(self, pessoa2):
    self.pessoa2 = pessoa2
    # pessoa2 faz referência ao atributo nome da classe
    # pessoa2 é um atributo dp escorpo do método de inicialização
    # pessoa2 é acessível dentro e fora desse método de inicialização
    pessoa3 = "usuário"
    # pessoa3 faz parte do escopo do método de inicialização
    # pessoa3 é acessível dentro desse método de inicialização