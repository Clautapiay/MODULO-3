import math

precio_suscripcion = int(input("Ingrese el precio de su suscripción: \n"))
numero_usuarios = int(input("Ingrese el número de usuarios: \n"))
gastos_totales = int(input("Ingrese gastos totales: \n"))
utilidades_año_anterior = int(input("Ingrese las utilidades del año anterior: \n"))


utilidades = (precio_suscripcion * numero_usuarios - gastos_totales)
print(int(utilidades)) 

razon_utilidades = (utilidades / utilidades_año_anterior)

#dejar con dos decimales
dos_decimales = "{:.2f}".format(razon_utilidades)

print(float(dos_decimales))


