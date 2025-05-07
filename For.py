for i in range(6):
    print(i)

notas = [7.0, 5.5, 4.5, 8.0]
print(type(notas))
print(notas[0])
# print(notas[4])
print(len(notas))  # tamanho é quantidade de elementos

notas[2] = 6.7  # atribuição de valor
print(notas)

pessoas = ["Guilherme", "Kauã", "Igor", "Bruno"]
print(f"Tamanho da lista pessoas {len(pessoas)}")
print(f"Tamanho da string {len(pessoas[0])}")

print(pessoas[0][4])

# percorrendo a lista com estrutura de repetição
for pessoa in pessoas:
    print(pessoa)

i = 0
while i < len(pessoas):
    print(pessoas[i])
    i += 1

# Tabuada do 1 ao 10 usando for
