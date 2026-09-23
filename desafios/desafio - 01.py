from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake: Olá, sou {self.nome} trabalha no setor de ({self.setor}) e tenho cargo de ({self.cargo})."

c1 = Funcionario(nome="[blue]Maria[/]", setor="[blue]Administração[/]", cargo="[blue]Diretora[/]")
print(c1.apresentacao())

c2 = Funcionario(nome="[blue]Pedro[/]", setor="[blue]TI[/]", cargo="[blue]Programador[/]")
print(c2.apresentacao())
