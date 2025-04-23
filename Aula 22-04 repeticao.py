i = 0
while i <= 10:
    print(i)
    i += 1  # atribuição simplificada, mesmo que i = i + 1

# Tabuada de um número informado pelo usuário
numero = int(input("Digite um número: "))
i = 0
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1

# Tabuadas do 1 ao 10
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i:2} x {j} = {i * j:2}", end="   ")
        j += 1
    print()
    i += 1

# Receber uma string e contar a quantidade de vogais
# print("a" in "sistemas")  # True
# print("a" not in "sistemas")  # False


curso = input("Digite a string:").lower()
i = 0
vogais = 0
while i < len(curso):
    if curso[i] in "aeiouáéíóúãõ":
        print(f"Vogal: {curso[i]}")
        vogais += 1
    i += 1
print(f"A string tem {vogais} vogais")

# Exibir apenas os números pares de 1 até 100
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
