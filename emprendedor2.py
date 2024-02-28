# A usuarios premmium se le cobra 50% + en la suscripción

import math

suscripcion_normal = int(input("Ingrese el precio de su suscripción: \n"))
usuarios_normal = int(input("Ingrese el número de usuarios: \n"))
usuarios_premium = int(input("Ingrese el número de usuarios premium: \n"))
gastos_totales = int(input("Ingrese gastos totales: \n"))

# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺𝑇
 

#UTILIDADES NORMAL
utilidades_normal = (suscripcion_normal * usuarios_normal)

#UTILIDADES PREMIUM
utilidades_premium = ((suscripcion_normal * 0.5 + suscripcion_normal) * usuarios_premium) 

utilidades = ((utilidades_normal + utilidades_premium) - (gastos_totales))

print(int(utilidades))

