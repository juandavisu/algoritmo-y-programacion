Algoritmo Ejercicio_14
	// Definici�n de variables
	Definir lectura_anterior Como Entero
	Definir lectura_actual Como Entero
	Definir costo_por_kilovatio Como Real
	Definir consumo_kilovatios Como Entero
	Definir monto_total Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese la lectura anterior del medidor (kWh): "
	Leer lectura_anterior
	Escribir "Ingrese la lectura actual del medidor (kWh): "
	Leer lectura_actual
	Escribir "Ingrese el costo por kilovatio (COP/kWh): "
	Leer costo_por_kilovatio
	
	// C�lculo del consumo en kilovatios
	consumo_kilovatios <- lectura_actual - lectura_anterior
	
	// C�lculo del monto total a pagar
	monto_total <- consumo_kilovatios * costo_por_kilovatio
	
	// Mostrar resultado
	Escribir "El consumo en kilovatios es: ", consumo_kilovatios, " kWh"
	Escribir "El monto total a pagar es: ", monto_total, " COP"
FinAlgoritmo

