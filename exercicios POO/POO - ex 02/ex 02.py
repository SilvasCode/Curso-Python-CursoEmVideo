# Declaração de classe
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use variavel = Gafonhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): # Construtor
        #Atributos de Instancia
        self.nome = nome
        self.idade = idade

    # Instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)

g2 = Gafanhoto("Mauro", 53)
print(g2)

