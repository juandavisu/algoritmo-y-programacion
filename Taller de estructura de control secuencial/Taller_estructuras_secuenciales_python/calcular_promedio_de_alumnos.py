def calcular_promedios_alumno():
    # Solicitar datos al usuario para Matemática
    examen_matematica = float(input("Ingrese la nota del examen de Matemática: "))
    tarea1_matematica = float(input("Ingrese la nota de la tarea 1 de Matemática: "))
    tarea2_matematica = float(input("Ingrese la nota de la tarea 2 de Matemática: "))
    tarea3_matematica = float(input("Ingrese la nota de la tarea 3 de Matemática: "))

    # Solicitar datos al usuario para Física
    examen_fisica = float(input("Ingrese la nota del examen de Física: "))
    tarea1_fisica = float(input("Ingrese la nota de la tarea 1 de Física: "))
    tarea2_fisica = float(input("Ingrese la nota de la tarea 2 de Física: "))

    # Solicitar datos al usuario para Química
    examen_quimica = float(input("Ingrese la nota del examen de Química: "))
    tarea1_quimica = float(input("Ingrese la nota de la tarea 1 de Química: "))
    tarea2_quimica = float(input("Ingrese la nota de la tarea 2 de Química: "))
    tarea3_quimica = float(input("Ingrese la nota de la tarea 3 de Química: "))

    # Cálculo del promedio de Matemática
    promedio_tareas_matematica = (tarea1_matematica + tarea2_matematica + tarea3_matematica) / 3
    promedio_matematica = (examen_matematica * 0.9) + (promedio_tareas_matematica * 0.1)

    # Cálculo del promedio de Física
    promedio_tareas_fisica = (tarea1_fisica + tarea2_fisica) / 2
    promedio_fisica = (examen_fisica * 0.8) + (promedio_tareas_fisica * 0.2)

    # Cálculo del promedio de Química
    promedio_tareas_quimica = (tarea1_quimica + tarea2_quimica + tarea3_quimica) / 3
    promedio_quimica = (examen_quimica * 0.85) + (promedio_tareas_quimica * 0.15)

    # Cálculo del promedio general
    promedio_general = (promedio_matematica + promedio_fisica + promedio_quimica) / 3

    # Mostrar resultados
    print(f"Promedio en Matemática: {promedio_matematica:.2f}")
    print(f"Promedio en Física: {promedio_fisica:.2f}")
    print(f"Promedio en Química: {promedio_quimica:.2f}")
    print(f"Promedio General: {promedio_general:.2f}")

# Llamar a la función
calcular_promedios_alumno()
