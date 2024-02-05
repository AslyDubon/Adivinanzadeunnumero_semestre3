import random

numero_secreto = random.randint(1, 10)
intentos = 0

nombre_usuario = input("¡Bienvenido al juego de adivinanza de números! Por favor, ingresa tu nombre: ")
print(f"Hola {nombre_usuario}! Intenta adivinar el número secreto, que está entre 1 y 10.")

while True:
    intento_usuario = int(input("Ingresa tu número: "))
    intentos += 1

    if intento_usuario == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
        break
    elif intento_usuario < numero_secreto:
        print("El número es demasiado bajo. ¡Intenta de nuevo!")
    else:
        print("El número es demasiado alto. ¡Intenta de nuevo!")

print(f"Muchas gracias por jugar. El número secreto era: {numero_secreto}. ¡Bien jugado!, vuelve pronto.")
