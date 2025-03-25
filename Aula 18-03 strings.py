curso = "Sistemas de Informação"
print(type(curso))
print(curso[0])
print(curso[2])
print(curso[-1])
# print(curso[22]) ocorre um erro pois o índice é inválido

print("Tamanho da string:", len(curso))

# concatenação - junção de strings
instituicao = " da Fafram"
print(curso + instituicao)

nome = "Guilherme"
print(nome * 2)  # multiplicação de strings

print(nome * 3 + "!")  # precedência de operadores

# composição de strings com f-strings
print(f"Curso: {curso}, Boa noite {nome}!")  # interpolação

idade = 17
grana = 1000
print(f"{nome} tem {idade} anos e R$ {grana:.2f} no bolso")
