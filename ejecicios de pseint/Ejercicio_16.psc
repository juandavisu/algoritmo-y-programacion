Algoritmo Ejercicio_16
	// Definici�n de variables
	Definir galones_surtidos Como Real
	Definir precio_por_litro Como Real
	Definir litros_equivalentes Como Real
	Definir monto_a_cobrar Como Real
	Definir litros_por_galon Como Real
	
	// Constante de conversi�n de galones a litros
	litros_por_galon <- 3.785
	
	// Precio del litro de gasolina
	precio_por_litro <- 50000
	
	// Solicitar datos al usuario
	Escribir "Ingrese la cantidad de galones surtidos: "
	Leer galones_surtidos
	
	// C�lculo de los litros equivalentes
	litros_equivalentes <- galones_surtidos * litros_por_galon
	
	// C�lculo del monto a cobrar
	monto_a_cobrar <- litros_equivalentes * precio_por_litro
	
	// Mostrar resultado
	Escribir "La cantidad de litros equivalentes es: ", litros_equivalentes, " litros"
	Escribir "El monto a cobrar es: ", monto_a_cobrar, " COP"
FinAlgoritmo

