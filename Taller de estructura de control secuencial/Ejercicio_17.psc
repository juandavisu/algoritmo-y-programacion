Algoritmo Ejercicio_17
	// Definici�n de variables
	Definir presupuesto_total Como Real
	Definir presupuesto_ginecologia Como Real
	Definir presupuesto_pediatria Como Real
	Definir presupuesto_traumatologia Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el presupuesto total anual del hospital: "
	Leer presupuesto_total
	
	// C�lculo del presupuesto para cada �rea
	presupuesto_ginecologia <- presupuesto_total * 0.40
	presupuesto_pediatria <- presupuesto_total * 0.30
	presupuesto_traumatologia <- presupuesto_total * 0.30
	
	// Mostrar resultados
	Escribir "Presupuesto para Ginecolog�a: ", presupuesto_ginecologia, " COP"
	Escribir "Presupuesto para Pediatr�a: ", presupuesto_pediatria, " COP"
	Escribir "Presupuesto para Traumatolog�a: ", presupuesto_traumatologia, " COP"
FinAlgoritmo

