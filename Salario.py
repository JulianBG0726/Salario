salarioB = float(input("Buenas tardes, ingrese su salario bruto mensual: "))
porcentajeImpuesto = float(input("Ahora ingrese el porcentaje de impuesto: "))
deducciones = float(input("Por último, ingrese las deducciones adicionales: "))

impuesto = salarioB*(porcentajeImpuesto/100)

salarioN = salarioB-impuesto-deducciones

print("Su salario neto mensual es de: $", salarioN)