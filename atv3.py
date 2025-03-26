valor_total = int(input("Diga o valor total das compras:"))

if valor_total > 500:
    taxa = (valor_total - 500) * 1.5
    valor_taxado = taxa + 500
    print(f"Valor acima de R$500. Valor com taxa de 50%: {valor_taxado}")

else:
    print("Livre de taxa")
