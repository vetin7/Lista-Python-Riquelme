num1 = int(input("Diga o primeiro numero: "))
num2 = int(input("Diga o segundo numero: "))
num3 = int(input("Diga o terceiro numero: "))

media_arit = (num1 + num2 + num3) / 3

media_pond1 = (num1 * 2), (num2 * 2), (num3 * 3)

media_pond2 = (num1 * 1), (num2 * 2), (num2 * 2)

print("Media aritmetica:", media_arit)
print("Media ponderada peso 2, 2 e 3", media_pond1)
print("Media ponderada peso 1, 2 e 2:", media_pond2)
