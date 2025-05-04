import time

while True:
    numero = int(input("Digite um número: "))

    if numero <= 0:
        continue

    print("Contagem regressiva iniciada!")

    while numero >= 0:
        print(numero)
        time.sleep(1)
        numero -= 1

    opcao = input("Deseja continuar? ").lower()
    if opcao != "s":
        break

