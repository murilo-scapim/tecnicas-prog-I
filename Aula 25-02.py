nome = "Gabriel"
peso = 56.5
altura = 1.77
idade = 18
aprovado = True

print(type(nome))
print(type(peso))
print(type(idade))
print(type(aprovado))

# imc = peso / altura ** 2
imc = peso / (altura * altura)
print("O IMC é:", round(imc, 2))

a = 1
b = 5
c = 2
d = 1

# Operadores relacionais
print(a == b)  # Igualdade
print(b > a)
print(a < b)
print(a == d)
print(a >= b)
print(c <= b)
print(d != a)  # Diferente
print(altura >= 1.70)  # Retorna um booleano (True ou False)

print(not aprovado)
baixo_peso = imc < 18.5
# peso_normal = imc >= 18.6 and imc <= 24.9
peso_normal = 18.6 <= imc <= 24.9
