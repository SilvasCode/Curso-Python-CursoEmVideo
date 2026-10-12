from rich import print
from rich.table import Table

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        texto = f"{self.nome}\n"
        texto += f"R${self.preco:,.2f}"
        return texto


produto1 = Produto("Arroz", 25.90)
produto2 = Produto("Feijão", 8.50)
produto3 = Produto("Macarrão", 6.99)

tabela = Table(title="Lista de Produtos")

tabela.add_column("Etiqueta")

tabela.add_row(produto1.etiqueta())
tabela.add_row(produto2.etiqueta())
tabela.add_row(produto3.etiqueta())

print(tabela)