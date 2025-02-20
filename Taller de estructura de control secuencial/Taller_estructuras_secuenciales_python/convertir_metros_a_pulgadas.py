def convertir_metros_a_pies_pulgadas():
    # Solicitar datos al usuario
    metros = float(input("Ingrese la cantidad en metros: "))

    # Constantes de conversión
    pulgadas_por_metro = 39.27
    pies_por_pulgada = 1 / 12

    # Convertir metros a pulgadas
    pulgadas = metros * pulgadas_por_metro

    # Convertir pulgadas a pies y pulgadas
    pies = int(pulgadas // 12)
    pulgadas_restantes = pulgadas % 12

    # Mostrar resultados
    print(f"{metros} metros son equivalentes a {pies} pies y {pulgadas_restantes:.2f} pulgadas.")

# Llamar a la función
convertir_metros_a_pies_pulgadas()
