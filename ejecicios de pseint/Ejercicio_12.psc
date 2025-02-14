Algoritmo  Ejecicio_12
	// Definici�n de variables
	Definir nombre_alumno Como Cadena
	Definir nota_examen_matematica Como Real
	Definir nota_tarea1_matematica Como Real
	Definir nota_tarea2_matematica Como Real
	Definir nota_tarea3_matematica Como Real
	Definir promedio_tareas_matematica Como Real
	Definir promedio_matematica Como Real
	
	Definir nota_examen_fisica Como Real
	Definir nota_tarea1_fisica Como Real
	Definir nota_tarea2_fisica Como Real
	Definir promedio_tareas_fisica Como Real
	Definir promedio_fisica Como Real
	
	Definir nota_examen_quimica Como Real
	Definir nota_tarea1_quimica Como Real
	Definir nota_tarea2_quimica Como Real
	Definir nota_tarea3_quimica Como Real
	Definir promedio_tareas_quimica Como Real
	Definir promedio_quimica Como Real
	
	Definir promedio_general Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el nombre del alumno: "
	Leer nombre_alumno
	
	// Datos para Matem�tica
	Escribir "Ingrese la nota del examen de Matem�tica: "
	Leer nota_examen_matematica
	Escribir "Ingrese la nota de la tarea 1 de Matem�tica: "
	Leer nota_tarea1_matematica
	Escribir "Ingrese la nota de la tarea 2 de Matem�tica: "
	Leer nota_tarea2_matematica
	Escribir "Ingrese la nota de la tarea 3 de Matem�tica: "
	Leer nota_tarea3_matematica
	
	// Datos para F�sica
	Escribir "Ingrese la nota del examen de F�sica: "
	Leer nota_examen_fisica
	Escribir "Ingrese la nota de la tarea 1 de F�sica: "
	Leer nota_tarea1_fisica
	Escribir "Ingrese la nota de la tarea 2 de F�sica: "
	Leer nota_tarea2_fisica
	
	// Datos para Qu�mica
	Escribir "Ingrese la nota del examen de Qu�mica: "
	Leer nota_examen_quimica
	Escribir "Ingrese la nota de la tarea 1 de Qu�mica: "
	Leer nota_tarea1_quimica
	Escribir "Ingrese la nota de la tarea 2 de Qu�mica: "
	Leer nota_tarea2_quimica
	Escribir "Ingrese la nota de la tarea 3 de Qu�mica: "
	Leer nota_tarea3_quimica
	
	// C�lculo del promedio de Matem�tica
	promedio_tareas_matematica <- (nota_tarea1_matematica + nota_tarea2_matematica + nota_tarea3_matematica) / 3
	promedio_matematica <- (nota_examen_matematica * 0.9) + (promedio_tareas_matematica * 0.1)
	
	// C�lculo del promedio de F�sica
	promedio_tareas_fisica <- (nota_tarea1_fisica + nota_tarea2_fisica) / 2
	promedio_fisica <- (nota_examen_fisica * 0.8) + (promedio_tareas_fisica * 0.2)
	
	// C�lculo del promedio de Qu�mica
	promedio_tareas_quimica <- (nota_tarea1_quimica + nota_tarea2_quimica + nota_tarea3_quimica) / 3
	promedio_quimica <- (nota_examen_quimica * 0.85) + (promedio_tareas_quimica * 0.15)
	
	// C�lculo del promedio general
	promedio_general <- (promedio_matematica + promedio_fisica + promedio_quimica) / 3
	
	// Mostrar resultados
	Escribir "Alumno: ", nombre_alumno
	Escribir "Promedio en Matem�tica: ", promedio_matematica
	Escribir "Promedio en F�sica: ", promedio_fisica
	Escribir "Promedio en Qu�mica: ", promedio_quimica
	Escribir "Promedio General: ", promedio_general
FinAlgoritmo

