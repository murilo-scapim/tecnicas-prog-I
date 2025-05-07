import random

opcoes = ["pedra", "papel", "tesoura"]
vitorias_jogador = 0
vitorias_maquina = 0
empates = 0
jogando = True

print("*"*45)
print("Jokenpô!".center(45))
print("*"*45)

while jogando:
    print("1 - Jogar")
    print("2 - Placar")
    print("3 - Sair")

    escolha = input("Informe a opção: ")
    if escolha == "1":
        player = input("Escolha uma opção: pedra, papel ou tesoura: ").lower()

        if player not in opcoes:
            print("Jogada inválida!")
            continue

        maquina = random.choice(opcoes)

        print(f"Você escolheu: {player}")
        print(f"Máquina: {maquina}")

        if maquina == player:
            print("Empatou!")
            empates += 1
        elif (player == "pedra" and maquina == "tesoura") or\
                (player == "papel" and maquina == "pedra") or\
                (player == "tesoura" and maquina == "papel"):
            print("Parabéns! Você venceu.")
            vitorias_jogador += 1
        else:
            print("Você perdeu!")
            vitorias_maquina += 1
    elif escolha == "2":
        print("Placar")
        print(f"Empates: {empates}")
        print(f"Vitórias da máquina: {vitorias_maquina}")
        print(f"Suas vitórias: {vitorias_jogador}")
    elif escolha == "3":
        print("Saindo do jogo...")
        print("Placar")
        print(f"Empates: {empates}")
        print(f"Vitórias da máquina: {vitorias_maquina}")
        print(f"Suas vitórias: {vitorias_jogador}")
        jogando = False
    else:
        print("Opção inválida!")
