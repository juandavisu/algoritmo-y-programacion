def convertir_divisas():
    # Tasas de cambio dadas
    chelines_a_pesetas = 956.871 / 100
    dracmas_a_pesetas = 88.607 / 100
    francos_franceses_a_pesetas = 20.110
    pesetas_a_dolares = 1 / 122.499
    pesetas_a_liras_italianas = 100 / 9.289

    # Leer cantidad en chelines austríacos y convertir a pesetas
    chelines_austriacos = float(input("Ingrese la cantidad en chelines austríacos: "))
    pesetas_chelines = chelines_austriacos * chelines_a_pesetas
    print(f"{chelines_austriacos} chelines austríacos son {pesetas_chelines:.2f} pesetas.")

    # Leer cantidad en dracmas griegos y convertir a francos franceses
    dracmas_griegos = float(input("Ingrese la cantidad en dracmas griegos: "))
    pesetas_dracmas = dracmas_griegos * dracmas_a_pesetas
    francos_franceses = pesetas_dracmas / francos_franceses_a_pesetas
    print(f"{dracmas_griegos} dracmas griegos son {francos_franceses:.2f} francos franceses.")

    # Leer cantidad en pesetas y convertir a dólares y liras italianas
    pesetas = float(input("Ingrese la cantidad en pesetas: "))
    dolares = pesetas * pesetas_a_dolares
    liras_italianas = pesetas * pesetas_a_liras_italianas
    print(f"{pesetas} pesetas son {dolares:.2f} dólares y {liras_italianas:.2f} liras italianas.")

# Llamar a la función
convertir_divisas()
