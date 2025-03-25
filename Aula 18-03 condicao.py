disciplina = input("Informe a disciplina: ")
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

# validação da entrada das notas
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10")
    exit()

frequencia = int(input("Informe a frequência: "))

media = (nota1 + nota2) / 2

# Estrutura condicional
if media >= 5 and frequencia >= 75:
    situacao = "Aprovado"
elif media < 5 and frequencia >= 75:
    situacao = "Exame"
else:
    situacao = "Reprovado"

print(f"Disciplina: {disciplina}")
print(f"Situação: {situacao}")


cor_semaforo = input("Digite a cor (vermelho, verde ou amarelo)").lower()
# lower coloca o texto em caixa baixa
if cor_semaforo == "vermelho":
    print("Pare!")
elif cor_semaforo == "verde":
    print("Siga!")
elif cor_semaforo == "amarelo":
    print("Atenção!")
else:
    print("Cor inválida!")


idade = 20
if idade >= 16:
    pode_votar = True
else:
    pode_votar = False

# shorthand - forma abreviada do if else
pode_votar = True if idade >= 16 else False
print(pode_votar)
