def calcular_sueldo_neto():
    # Solicitar datos al usuario
    nombre = input("Ingrese el nombre del trabajador: ")
    horas_normales = float(input("Ingrese el número de horas normales trabajadas: "))
    pago_hora_normal = float(input("Ingrese el pago por hora normal: "))
    horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
    num_hijos = int(input("Ingrese el número de hijos: "))

    # Cálculo del sueldo base
    sueldo_base = horas_normales * pago_hora_normal

    # Cálculo del pago por horas extras
    pago_hora_extra = pago_hora_normal * 1.25
    pago_horas_extras = horas_extras * pago_hora_extra

    # Cálculo del sueldo bruto
    sueldo_bruto = sueldo_base + pago_horas_extras

    # Cálculo de las deducciones
    deduccion_pago_forzoso = sueldo_base * 0.05
    deduccion_politica_habitacional = sueldo_base * 0.02
    deduccion_caja_ahorro = sueldo_base * 0.07
    total_deducciones = deduccion_pago_forzoso + deduccion_politica_habitacional + deduccion_caja_ahorro

    # Cálculo de las asignaciones
    asignacion_actualizacion_academica = 250000
    asignacion_por_hijo = 173000 * num_hijos
    prima_por_hogar = 180000
    total_asignaciones = asignacion_actualizacion_academica + asignacion_por_hijo + prima_por_hogar

    # Cálculo del sueldo neto
    sueldo_neto = sueldo_bruto + total_asignaciones - total_deducciones

    # Mostrar resultados
    print(f"Trabajador: {nombre}")
    print(f"Sueldo Base: {sueldo_base:,.0f} COP")
    print(f"Pago por Horas Extras: {pago_horas_extras:,.0f} COP")
    print(f"Sueldo Bruto: {sueldo_bruto:,.0f} COP")
    print(f"Total Deducciones: {total_deducciones:,.0f} COP")
    print(f"Total Asignaciones: {total_asignaciones:,.0f} COP")
    print(f"Sueldo Neto: {sueldo_neto:,.0f} COP")

# Llamar a la función
calcular_sueldo_neto()
