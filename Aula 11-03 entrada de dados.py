# input sempre retorna uma string
nome = input("Informe o seu nome: ")
print("Boa noite", nome)
print(type(nome))

print(nome[0])  # String é uma estrutura indexada
print(nome[1])
print(nome[-1])  # último caracter

# casting é a conversão de um tipo de dados para outro
idade = int(input("Informe sua idade: "))
print("Idade:", idade)
print(type(idade))

peso = float(input("Informe seu peso: "))
print("Peso:", peso)
print(type(peso))
