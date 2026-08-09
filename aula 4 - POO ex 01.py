# Declaração de classe
class Gafanhoto:
    def __init__(self): # Construtor
        #Atributos de Instancia
        self.nome = " "
        self.idade = 0

    # Instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 19
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Marcos"
g2.idade = 26
print(g2.mensagem())
