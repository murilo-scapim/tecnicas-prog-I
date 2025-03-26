altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: M ou F ")

match sexo:
    case "M" | "m":
        peso_ideal = (72.7 * altura) - 58
        print(f"Seu peso ideal é {peso_ideal:.2f} quilos")
    case "F" | "f":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é {round(peso_ideal, 2)} quilos")
    case _:
        print("Sexo inválido!")
