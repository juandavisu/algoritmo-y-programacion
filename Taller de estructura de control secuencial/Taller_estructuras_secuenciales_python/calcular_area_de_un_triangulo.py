import math

def calcular_area_triangulo():
    # Solicitar las longitudes de los lados del triángulo
    a = float(input("Ingrese la longitud del lado a: "))
    b = float(input("Ingrese la longitud del lado b: "))
    c = float(input("Ingrese la longitud del lado c: "))

    # Calcular el semiperímetro
    s = (a + b + c) / 2

    # Calcular el área utilizando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Mostrar el resultado
    print(f"El área del triángulo es: {area:.2f} unidades cuadradas")

# Llamar a la función para ejecutar el programa
calcular_area_triangulo()
