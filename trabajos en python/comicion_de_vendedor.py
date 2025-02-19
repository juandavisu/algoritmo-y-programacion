def calcular_comisiones_vendedor():
    # Solicitar datos al usuario
    sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
    venta1 = float(input("Ingrese el monto de la primera venta: "))
    venta2 = float(input("Ingrese el monto de la segunda venta: "))
    venta3 = float(input("Ingrese el monto de la tercera venta: "))

    # Calcular el total de ventas
    total_ventas = venta1 + venta2 + venta3

    # Calcular las comisiones (10% de las ventas)
    comisiones = total_ventas * 0.10

    # Calcular el total que recibirá el vendedor
    total_recibido = sueldo_base + comisiones

    # Mostrar resultados
    print(f"Comisiones obtenidas: {comisiones:.2f} COP")
    print(f"Total recibido (sueldo base + comisiones): {total_recibido:.2f} COP")

# Llamar a la función
calcular_comisiones_vendedor()
