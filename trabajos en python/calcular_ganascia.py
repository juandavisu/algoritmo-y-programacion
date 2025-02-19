def calcular_ganancia_inversion():
    # Solicitar datos al usuario
    capital_inicial = float(input("Ingrese el capital inicial a invertir: "))

    # Tasa de interés mensual
    tasa_interes_mensual = 0.02

    # Cálculo del interés ganado después de un mes
    interes_ganado = capital_inicial * tasa_interes_mensual

    # Cálculo del capital total después de un mes
    capital_total = capital_inicial + interes_ganado

    # Mostrar resultado
    print(f"El capital total después de un mes es: {capital_total:.2f} COP")
    print(f"El interés ganado es: {interes_ganado:.2f} COP")

# Llamar a la función para ejecutar el programa
calcular_ganancia_inversion()
