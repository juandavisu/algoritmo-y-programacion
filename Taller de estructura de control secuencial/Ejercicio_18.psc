Algoritmo Ejercicio_18
	// Definici�n de variables
	Definir capital Como Real
	Definir intereses Como Real
	Definir tiempo Como Entero
	Definir razon Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el monto del pr�stamo (Capital) en Bol�vares: "
	Leer capital
	Escribir "Ingrese los intereses pagados en Bol�vares: "
	Leer intereses
	
	// Tiempo en a�os
	tiempo <- 4
	
	// C�lculo del tanto por ciento anual
	razon <- (intereses * 100) / (capital * tiempo)
	
	// Mostrar resultado
	Escribir "El tanto por ciento anual cobrado es: ", razon, "%"
FinAlgoritmo

