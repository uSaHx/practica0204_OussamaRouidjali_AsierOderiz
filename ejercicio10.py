password_real = "oussama"
password_intr = 0
while True:
    password_intr = input("Introduzca su contraseña:\n ")
    print("CONTRSEÑA INCORRECTA")
    if password_intr == password_real:
        print("CONTRSEÑA CORRECTA")
        break