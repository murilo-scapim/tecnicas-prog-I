cor_semaforo = input("Informe a cor: ").lower()

match cor_semaforo:
    case "verde" | "Verde":
        print("Siga!")
    case "amarelo":
        print("Atenção")
    case "vermelho":
        print("Pare!")
    case _:  # case default wildcard
        print("Cor não reconhecida!")
