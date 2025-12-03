# Guardar la contraseña correcta
system_password = "admin123"

# Número de intentos permitidos
intentos = 3

# Bucle para permitir varios intentos
while intentos > 0:
    # Pedir la contraseña al usuario
    user_password = input("Ingresa la contraseña, por favor: ")

    # Verificar si es correcta
    if system_password == user_password:
        print("¡Contraseña correcta, bienvenido! 😊")
        break  # Sale del bucle si acierta
    else:
        intentos -= 1  # Resta un intento
        if intentos > 0:
            print(f"¡Contraseña incorrecta! ⛔ Te quedan {intentos} intento(s).")
        else:
            print("Se han agotado los intentos. Acceso denegado. ❌")
