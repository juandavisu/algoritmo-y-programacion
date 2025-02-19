def calcular_descuento_tienda():
    # Solicitar datos al usuario
    total_compra = float(input("Ingrese el total de la compra: "))

    # Calcular el descuento (15% del total de la compra)
    descuento = total_compra * 0.15

    # Calcular el monto final a pagar
    monto_final = total_compra - descuento

    # Mostrar resultados
    print(f"Descuento aplicado: {descuento:.2f} COP")
    print(f"Monto final a pagar: {monto_final:.2f} COP")

# Llamar a la función
calcular_descuento_tienda()
