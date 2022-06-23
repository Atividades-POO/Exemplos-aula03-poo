#
# 1 - importe a classe criada no arquivo arquivo.py;
from artigo import Artigo

# 1.1 - crie um objeto da classe Artigo;
a1 = Artigo(1, "Autor 1", 500)
# chame o método imprime do objeto criado;
a1.imprime(100)
# chame o método imprime2 do objeto criado;
a1.imprime2()

#
print("-" * 20)
#


# 2 - importe a classe colocada no arquivo colaborador.py
from colaborador import Colaborador as C # crie um alias para a classe Colaborador como C

# 2.1 crie uma instância da classe colaborador
c1 = C("João", "gerente", "1234567890", 1990) # cria um objeto da classe colaborador com valores "João", "gerente", "1234567890", 1990

#
# Imprime os dados do colaborador c1
print(c1.nome) # vai imprimir "João"
print(c1.cargo) # vai imprimir "gerente"
print(c1.cpf) # vai imprimir "1234567890"
print(c1.anoNascimento) # vai imprimir "1990"
print(c1.idade) # vai imprimir "28"
#
# chame o método imprime da instância c1
c1.imprime() # vai imprimir todos os dados do colaborador c1

#
# chama o método calculaIdade da instância c1
c1.calculaIdade() # vai calcular a idade do colaborador c1 e vai atualizar o atributo idade

