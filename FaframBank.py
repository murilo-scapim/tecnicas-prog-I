saldo = 0.0
sair = False

print("Boas vindas ao Fafram Bank\n")
print("Escolha uma operação:")
print("1 - Fazer deposito")
print("2 - Sacar")
print("3 - Consultar o saldo")
print("4 - Sair")

while sair != True:
    operacao = input("Informe a operação: ")

    match operacao:
        case "1":
            valor_deposito = float(input("Informe o valor para deposito: "))
            if valor_deposito > 0 and type(valor_deposito) == float:
                saldo += valor_deposito
                print(f"R$ {valor_deposito:.2f} depositado com sucesso")
            else:
                print("Erro: Valor inválido!")
        case 2:
            valor_saque = float(input("Informe o valor para saque: "))
            if valor_saque > 0 and type(valor_saque) == float:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    print(f"R$ {valor_saque:.2f} sacado com sucesso")
                    print(f"Saldo atual: R$ {saldo:.2f}")
                else:
                    print("Erro: Saldo insuficiente!")
            else:
                print("Erro: Valor inválido!")
        case 3:
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
        case 4:
            print("Até logo!")
            sair = True
        case _:
            print("Operação inválida!")
