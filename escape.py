# Ve : corresponde a la Velocidad de Escape en [m/s].
# g: corresponde a la constante gravitacional en [m/s2].
# r: Corresponde al radio del planeta en [m].

# FORMULA: 𝑉𝑒=√2𝑔𝑟
import math

constante_gravitacional = float(input(("Ingrese la constante gravitacional en [m/s2]: \n ")))
radio = float(input("Ingrese el radio del planeta en [Km]: \n "))
Ve = math.sqrt((2 * ((constante_gravitacional * 1000) * radio)))

frase = "La velocidad de escape es: "
frase_2= "[m/s]"
concatenado = frase + str(Ve) + frase_2

print(concatenado)

