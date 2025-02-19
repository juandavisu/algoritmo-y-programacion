def calcular_promedio_edad():
    # Solicitar datos al usuario
    edad1 = int(input("Ingrese la edad de la primera persona: "))
    edad2 = int(input("Ingrese la edad de la segunda persona: "))
    edad3 = int(input("Ingrese la edad de la tercera persona: "))

    # Cálculo de la suma de las edades
    suma_edades = edad1 + edad2 + edad3

    # Cálculo del promedio de edad
    promedio_edad = suma_edades / 3

    # Mostrar resultado
    print(f"El promedio de edad de las tres personas es: {promedio_edad}")

# Llamar a la función para ejecutar el programa
calcular_promedio_edad()
