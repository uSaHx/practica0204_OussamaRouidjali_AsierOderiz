edad = int(input("Introduzca su edad: \n"))
ingresos_mensuales = int(input("Introduzca sus ingresos mesuales: \n"))

if edad > 16 and ingresos_mensuales >= 1000:
    print("Usted debe tributar")
else:
    print("Usted no tiene la obligacion de tributar")