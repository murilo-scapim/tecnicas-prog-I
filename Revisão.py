# comandos de repetição
i = 1
while i <= 10:
    if i % 2 == 0:
        break
    print(i)
    i += 1

for i in range(5):
    print(i)

lista_de_compras = ["Café", "Miojo", "Bolacha", "Maça"]
print(type(lista_de_compras))
print(f"Tamanho da lista {len(lista_de_compras)}")
print(f"Item no índice 0 {lista_de_compras[0]}")
# print(f"Item no índice 5 {lista_de_compras[5]}") ErrorIndex
print(f"Item no índice -1 {lista_de_compras[-1]}")

lista_de_compras[2] = "Biscoito"

for item in lista_de_compras:
    print(f"Vamos comprar {item}")

item = input("Digite o item para compra: ")
lista_de_compras.append(item)
print(f"Elemento removido {lista_de_compras.pop()}")
print(f"Índice do café: {lista_de_compras.index('Café')}")
lista_de_compras.remove('Miojo')
print(lista_de_compras)

i = 0
while i < len(lista_de_compras):
    print(f"Item da compra: {lista_de_compras[i]}")
    i += 1

for i, item in enumerate(lista_de_compras):
    print(f"{i} - {item}")
