tempo = int(input("Diga o valor dos segundos:"))

minutos = tempo // 60
horas = minutos // 60
dias = horas // 24

print(f"Dias: {dias}, Horas: {horas}, Minutos: {minutos}")
