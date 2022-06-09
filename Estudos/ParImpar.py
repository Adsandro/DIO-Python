def parImpar():
    num = int(input("informe um valor para verificarmos se é par: "))
    verificar = num % 2
    if verificar == 1:
        print("Este valor é impar")
    else:
        print("Este valor é par")
parImpar()