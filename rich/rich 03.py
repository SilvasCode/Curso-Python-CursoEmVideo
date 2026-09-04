from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome")
tabela.add_column("Preço")

tabela.add_row("Lápis", "[green]R$1,50[/]")
tabela.add_row("Boracha", "[green]R$5,00[/]")
tabela.add_row("Caderno", "[green]R$19,70[/]")
tabela.add_row("Mochila", "[green]R$79,90[/]")

print(tabela)