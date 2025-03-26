preco_alcool = float(input("Digite o preço do álcool: "))
preco_gasolina = float(input("Digite o preço da gasolina: "))

resultado = preco_alcool / preco_gasolina

if resultado < 0.70:
    print("Abasteça com álcool")
else:
    print("Abasteça com gasolina")

# shorthand
print("Abasteça com álcool") if resultado < 0.70 else print("Abasteça com gasolina")
