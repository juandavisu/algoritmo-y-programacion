def calcular_porcentaje_genero():
    # Solicitar datos al usuario
    total_estudiantes = int(input("Ingrese el total de estudiantes en el grupo: "))
    num_hombres = int(input("Ingrese el número de hombres en el grupo: "))

    # Calcular el número de mujeres
    num_mujeres = total_estudiantes - num_hombres

    # Calcular los porcentajes
    porcentaje_hombres = (num_hombres / total_estudiantes) * 100
    porcentaje_mujeres = (num_mujeres / total_estudiantes) * 100

    # Mostrar resultados
    print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
    print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")

# Llamar a la función
calcular_porcentaje_genero()
