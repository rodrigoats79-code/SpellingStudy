# Spelling Study

import random
import time
import pyttsx3


# Voz
def decir_palabra(palabra):
    voz = pyttsx3.init()
    voz.setProperty("rate", 150)
    voz.say(palabra)
    voz.runAndWait()
    voz.stop()


# Lecciones
lecciones_spelling = {
    1: [
        "completely",
        "fierce",
        "doesn't",
        "lieutenant",
        "thirtieth"
    ]
}


# Nombre
nombre = input("Hola, dime tu nombre: ").strip()

if nombre == "":
    nombre = "Estudiante"


print()
print(f"¡Hola, {nombre}! 👋")
print("Bienvenido a Spelling Study.")
print()


# Lecciones disponibles
print("📚 LECCIONES DISPONIBLES")

for numero in lecciones_spelling:
    print(f"   Lección {numero}")

print()


# Elegir lección
while True:

    try:
        leccion = int(input("¿Qué lección quieres estudiar?: "))

        if leccion in lecciones_spelling:
            break

        print("❌ Esa lección no existe.")

    except ValueError:
        print("❌ Escribe solamente el número de la lección.")


print()
print(f"✅ Seleccionaste la Lección {leccion}.")
print()


# Confirmar
while True:

    confirmar = input(
        "¿Quieres comenzar la lección? (si/no): "
    ).strip().lower()

    if confirmar == "si":
        break

    elif confirmar == "no":
        print()
        print("👋 ¡Hasta luego!")
        exit()

    else:
        print("❌ Escribe 'si' o 'no'.")


# Mezclar palabras
palabras = lecciones_spelling[leccion].copy()
random.shuffle(palabras)


# Elegir delay
while True:

    try:
        delay = float(
            input(
                "⏱️ ¿Cuántos segundos quieres de delay?: "
            )
        )

        if delay >= 0:
            break

        print("❌ El delay no puede ser negativo.")

    except ValueError:
        print("❌ Escribe un número.")


# Variables para resultados
correctas = 0
incorrectas = 0
errores = []


# Examen
for numero, palabra in enumerate(palabras, start=1):

    print()
    print("------------------------------------------")
    print(f"🔤 PALABRA {numero} DE {len(palabras)}")
    print("------------------------------------------")
    print()

    print("🔊 Escucha atentamente...")

    decir_palabra(palabra)

    time.sleep(delay)

    print()

    respuesta = input("✏️ Escribe la palabra: ").strip()


    # Comprobar respuesta
    if respuesta.lower() == palabra.lower():

        print()
        print("✅ ¡CORRECTO! 🎉")

        correctas += 1

    else:

        print()
        print("❌ INCORRECTO")
        print(f"La palabra correcta era: {palabra}")

        incorrectas += 1
        errores.append(palabra)


    print()

    input("Presiona ENTER para continuar...")


# Resultados
total = len(palabras)

porcentaje = (correctas / total) * 100


print()
print("==========================================")
print("              RESULTADOS")
print("==========================================")
print()

print(f"👤 Estudiante: {nombre}")
print(f"📚 Lección: {leccion}")
print()

print(f"🔤 Palabras: {total}")
print(f"✅ Correctas: {correctas}")
print(f"❌ Incorrectas: {incorrectas}")
print()

print(f"⭐ Calificación: {porcentaje:.0f}%")
print()


# Palabras incorrectas
if errores:

    print("📝 PALABRAS PARA PRACTICAR")
    print()

    for palabra in errores:
        print(f"   • {palabra}")

else:

    print(f"🎉 ¡Perfecto, {nombre}! No tuviste errores.")


print()
print("👋 ¡Gracias por usar Spelling Study!")