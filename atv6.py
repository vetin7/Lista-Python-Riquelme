def analise_primo(n):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []
num = 2

while len(primos) < 100:
    if analise_primo(num):
        primos.append(num)
    num += 1

print(" ".join(map(str, primos)))
