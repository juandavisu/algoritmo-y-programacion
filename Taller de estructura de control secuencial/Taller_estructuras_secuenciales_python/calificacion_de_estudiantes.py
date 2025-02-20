def calcular_calificacion_final():
    # Solicitar datos al usuario
    parcial1 = float(input("Ingrese la calificación del primer parcial: "))
    parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
    parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
    examen_final = float(input("Ingrese la calificación del examen final: "))
    trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

    # Calcular el promedio de los parciales
    promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

    # Calcular la calificación final
    calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

    # Mostrar resultado
    print(f"La calificación final en la materia de computación es: {calificacion_final:.2f}")

# Llamar a la función
calcular_calificacion_final()
