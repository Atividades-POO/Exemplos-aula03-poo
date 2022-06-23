#
# classe Artigo
class Artigo: # classe Artigo
  id = 0 # atributo
  autor = ""
  preco = 0.0

  def __init__(self, id, autor, preco): # inicializador
      self.titulo = id  # atributo
      self.autor = autor
      self.data = preco

  def imprime(self, valor): # método de instância
      print(f"Id: {self.id}")
      print(f"Autor: {self.autor}")
      print(f"preço: {self.preco + valor}") # soma o valor ao preço + valor

  def imprime2(self): # método de instância
    print(f"preço: {self.preco}")   # imprime o preço
    