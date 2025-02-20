Algoritmo Ejercicio_18
	// Definición de variables
	Definir capital Como Real
	Definir intereses Como Real
	Definir tiempo Como Entero
	Definir razon Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el monto del préstamo (Capital) en Bolívares: "
	Leer capital
	Escribir "Ingrese los intereses pagados en Bolívares: "
	Leer intereses
	
	// Tiempo en años
	tiempo <- 4
	
	// Cálculo del tanto por ciento anual
	razon <- (intereses * 100) / (capital * tiempo)
	
	// Mostrar resultado
	Escribir "El tanto por ciento anual cobrado es: ", razon, "%"
FinAlgoritmo

