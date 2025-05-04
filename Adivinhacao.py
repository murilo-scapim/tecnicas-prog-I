import random

while True:
    print("\n---- MENU -----")
    print("1 - Jogar")
    print("2 - Sair")

    escolha = input("Digite a opcao: ")
    if escolha == "1":
        sorteado = random.randint(1, 100)
        aposta = 0
        tentativas = 0

        print("Tente adivinhar o número entre 1 a 100")
        while aposta != sorteado:
            aposta = input("Qual seu palpite? ")

            if not aposta.isdigit():
                print("Por favor, insira um número válido!")
                continue

            aposta = int(aposta)
            if aposta < 0 or aposta > 100:
                print("Por favor, insira um número entre 1 e 100.")
                continue

            tentativas += 1

            if aposta == sorteado:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            elif aposta < sorteado:
                print("Tente um número mais alto!")
            else:
                print("Tente um número mais baixo!")

    elif escolha == "2":
        print("Saindo do jogo... Até mais!")
        break
    else:
        print("Escolha inválida! Tente novamente.")
