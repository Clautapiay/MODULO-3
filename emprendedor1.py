# Calcular utilidades del proyecto
# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺𝑇

# P: Precio de Suscripción
# U: Número de Usuarios
# GT: Gastos Totales

import math

precio_suscripcion = int(input("Ingrese el precio de su suscripción: \n"))
numero_usuarios = int(input("Ingrese el número de usuarios: \n"))
gastos_totales = int(input("Ingrese gastos totales: \n"))

utilidades = (precio_suscripcion * numero_usuarios - gastos_totales)

print(int(utilidades)) 