numero = int(input("Introduzca el numero del triangulo: \n"))
for asterisco in range(0, numero):
    for j in range(0, asterisco + 1):
        print("* ", end="")

    print("\r")