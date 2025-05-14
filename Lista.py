lista_de_compras = []

lista_de_compras.append("Café")
lista_de_compras.append("Pão")
lista_de_compras.append("Papel Higiênico")
lista_de_compras.append("Pasta de dente")

lista_de_compras.pop()
lista_de_compras.pop(1)

lista_de_compras.remove("Papel Higiênico")

print(f"Índice do café", lista_de_compras.index("Café"))

print(lista_de_compras)

lista_de_compras.append("Macarrão")
lista_de_compras.append("Bolacha Nikito de Morango")
lista_de_compras.append("Arroz")
lista_de_compras.append("Feijão")

for item in lista_de_compras:
    print(f"Item: {item}")

for i, item in enumerate(lista_de_compras):
    print(f"{i} - {item}")
