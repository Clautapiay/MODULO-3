# W : corresponde al peso de la persona en Kg.
# H: corresponde a la altura en metros.
# IMC: EL valor del IMC, en [Kg/m2]

import math

peso = float(input("Ingrese su peso en Kg: "))
altura = int(input("Ingrese su altura en centimetros: "))

#Calcular IMC y pasar cm a metros
indiceMC = (peso / ((altura/100) * (altura/100)))

#Mostrar IMC con solo dos decimales 

indiceMasaCorporal = "{:.2f}".format(indiceMC)
print("Su indice de masa corporal es:", indiceMasaCorporal)

#Clasificación por OMS
if indiceMC < 18.5:
    print("La clasificación OMS es Bajo Peso")
elif 18.5 <= indiceMC < 25:
    print("La clasificación OMS es Adecuado")

elif 25 <= indiceMC < 30:
    print("La clasificación OMS es Sobrepeso")

elif 30 <= indiceMC < 35:
    print("La clasificación OMS es Obesidad grado I")

elif 35 <= indiceMC < 40:
    print("La clasificación OMS es Obesidad grado II")

else:
    print("La clasificación OMS es Obesidad grado III")
