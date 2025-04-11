# Python Packages

from prettytable import PrettyTable  # type: ignore

table = PrettyTable()

# Methods
table.add_column("Pokemon Name" , ["Pikachu" , "Charmander" , "Squirtle"])
table.add_column("Type" , ["Electric" , "Water" , "Fire"])

# Attributes
table.align = 'l'

print(table)

