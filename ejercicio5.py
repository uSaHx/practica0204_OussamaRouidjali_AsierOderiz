nombre = input("Introduzca su nombre: \n")
sexo = input("Hombre o Mujer \n")

if sexo.upper() == "MUJER" and nombre[0].upper() < "M":
    print("Perteneces al Grupo A ")
elif sexo.upper() == "HOMBRE" and nombre[0].upper() > "N":
    print("Perteneces al Grupo A ")
else:
    print("Perteneces al Grupo B ")