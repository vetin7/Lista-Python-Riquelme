num1 = int(input("Diga um numero: "))
num2 = int(input("Diga outro numero: "))
num3 = int(input("Diga mais outro numero: "))

numeros = [num1, num2, num3]

def bubble_sort_desc(lista):
    num = len(lista)
    for i in range(num - 1):  
        for j in range(num - 1 - i):  
            if lista[j] < lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

bubble_sort_desc(numeros)

print(f"Lista do maior para o menor: {numeros}")
