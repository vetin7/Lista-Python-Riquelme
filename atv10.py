num = int(input("Diga um numero inteiro maior que 1: "))

primo = True
for i in range(2, int(num**0.5) + 1):
        if n % i == 0:
            primo = False
            break
          
if primo:
 print("Este numero é primo.")
 
else: 
 print("Este numero nao é primo.")
