def calcular_salario_neto():
    # Solicitar datos al usuario
    horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
    precio_por_hora = float(input("Ingrese el precio por hora: "))

    # Calcular el sueldo base
    sueldo_base = horas_trabajadas * precio_por_hora

    # Calcular el descuento por impuestos (20%)
    descuento_impuestos = sueldo_base * 0.20

    # Calcular el salario neto
    salario_neto = sueldo_base - descuento_impuestos

    # Mostrar resultados
    print(f"Sueldo base: {sueldo_base:.2f} COP")
    print(f"Descuento por impuestos: {descuento_impuestos:.2f} COP")
    print(f"Salario neto: {salario_neto:.2f} COP")

# Llamar a la función
calcular_salario_neto()
