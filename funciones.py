# =================================================.
# funciones.py
# Funciones para:                                  |
# calculadora.py                                   |
# por Barlan, con ayuda de la comunidad Underc0de  |
# underc0de.org                                    |
# =================================================.
from math import sqrt # Importamos desde la librería math la función para raices cuadradas.

# Creamos funciones para resolver los problemas:
def hipotenusa(a, b):	# Esta función sirve para calcular el lado mayor del triangulo.
	# c^2 = a^2 + b^2
	return sqrt((a * a) + (b * b))

def cateto(a, b):	# Y con esta función calculamos uno de los 2 lados.
	# El lado a calcular, es la resta del cuadrado de la hipotenusa menos el cuadrado del otro cateto.
	return sqrt((a * a) - (b * b))

def ecuacionCuadratica(a, b, c): # Función (eso espero xD) para resolver Ecuaciónes cuadrácticas
	# x = [ -b ± √(b2-4ac) ] / 2a
	try:
		x1 = (-b + (sqrt(b ** 2 - 4 * a * c))) / (a * 2)
		x2 = (-b - (sqrt(b ** 2 - 4 * a * c))) / (a * 2)
		return ("(+) = " + str(x1) + "\n(-) = " + str(x2))
	except:
		print("La ecuacion no tiene solucion.")

if __name__ == "__main__":
	print("Este no es un programa standalone, es una libreria.")