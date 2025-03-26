usuario = input("Informe seu login: ")
senha = input("Informe sua senha: ")

while usuario == senha:
    print("Sua senha e login nao podem ser iguais, tente de novo.")
    usuario = input("Informe seu login: ")
    senha = input("Informe sua senha: ")

else:
    print("Conta criada!")
