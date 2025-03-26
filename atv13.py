primeiro_salario = int(input("Informe seu primeiro salario : "))
tempo = int(input("Informe o tempo que voce trabalha: "))


salario_final = primeiro_salario * (2 ** tempo)


print(f"Seu salario apos {tempo} anos de servico sera: {salario_final}.")
