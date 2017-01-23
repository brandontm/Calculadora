# =================================================.
# calculadora. py                                  |
# por Barlan, con ayuda de la comunidad Underc0de  |
# underc0de.org                                    |
# =================================================.
from funciones import *
import os, sys # Importamos estas librerias relacionadas con la consola de Windows.

if sys.version_info[0] == 2: # TODO: Solucionar problemas de compatibilidad con Python 2
	input("Este programa fue diseñado para Python 3")
	sys.exit(1)

os.system("TITLE Calculadora v1.0 por Barlan")
os.system("color 1f")
while True:
	os.system("cls") # Limpiamos la consola para "ver mejor" xD
	print("""
# Calculadora v2
# por Barlan
# Creada el 9 de Octubre del 2014
# Revision #1: 20 de Octubre del 2014, a las 12:44 am
# Revision #2: 20 de Octubre del 2014, a las 10 pm
# Revision #3: 25 de Octubre del 2014, a las 4:05 pm

== Menu ==

Opciones:
[1] Sumar
[2] Restar
[3] Multiplicar
[4] Dividir
[5] Teorema de Pitagoras
[6] Ecuacion Cuadratica (o de segundo grado)
[7] Potencia
[8] Raiz Cuadrada
""")
	try:
		op = int(input("\nElige una opcion escribiendo su inciso, 0 para salir:\n>> "))
		os.system("cls") # Se limpia la consola en cada iteracion
		if op == 0:	# Funcion para salir
			input("Gracias por usar mi calculadora!")
			sys.exit(1)

		elif op == 1:
			print("== SUMA ==\n")
			num1 = int(input("Ingresa el primer entero:>> "))
			num2 = int(input("Ingresa el segundo entero:>> "))
			print("\nLa suma de las 2 variables es: ", num1 + num2)

		elif op == 2:
			print("== RESTA ==\n")
			num1 = int(input("Ingresa el primer entero:>> "))
			num2 = int(input("Ingresa el segundo entero:>> "))
			print("\nLa resta de las 2 variables es: ", num1 - num2)			

		elif op == 3:
			print("== MULTIPLICACION ==\n")
			num1 = int(input("Ingresa el primer entero:>> "))
			num2 = int(input("Ingresa el segundo entero:>> "))
			print("\nLa multiplicacion de las 2 variables es: ", num1 * num2)			

		elif op == 4:
			print("== DIVISION ==\n")
			num1 = int(input("Ingresa el primer entero:>> "))
			num2 = int(input("Ingresa el segundo entero:>> "))
			try:
				print("\nLa division de las 2 variables es: ", num1 / num2)
			except ZeroDivisionError:
				print("No se puede dividir entre 0")
		elif op == 5:
			print("== TEOREMA DE PITAGORAS ==\n")
			print("a^2 + b^2 = c^2\n")
			print("""
1) Hallar valor de un cateto
2) Hallar valor de hipotenusa
				""")
			try:
				opcion = int(input(">> "))
				if opcion == 1:
					a = int(input("Ingresa el valor de la hipotenusa: "))
					b = int(input("Ingresa el valor del lado b: "))
					resul = cateto(a, b)
					print("El valor del cateto es: ", resul)
				elif opcion == 2:
					a = int(input("Ingresa el valor del primer cateto: "))
					b = int(input("Ingresa el valor del segundo cateto: "))
					resul = hipotenusa(a, b)
					print("El valor de la hipotenusa es: ", resul)
				else:
					print("Ingresa una opcion valida")
			except ValueError:
				print("Ingresa un valor valido")
			finally: # Probablemente ese pedazo de código puede eliminarse. xd
				os.system("pause>nul")

		elif op == 6:
			# Al parecer, contiene errores al calcular todo, pero para soluciones futuras, lo dejo.
			print("== ECUACION DE SEGUNDO GRADO O CUADRATICA ==\n")
			print("Ecuacion:\n")
			x = int(input("a >> "))
			y = int(input("b >> "))
			z = int(input("c >> "))
			print(ecuacionCuadratica(x, y, z))
		
		elif op == 7:
			print("== POTENCIA ==\n")
			num1 = int(input("Ingrese un numero: "))
			num2 = int(input("Ingrese el exponente: "))
			resul = num1 ** num2
			print(str(num1)+" a la "+str(num2)+" potencia es igual a: ",resul)
			
		elif op == 8:
			print("== RAIZ CUADRADA ==\n")
			num1 = int(input("Ingrese un numero positivo: "))
			resul = sqrt(num1)
			print("La raiz cuadrada de "+str(num1)+" es: \n",resul)
		else: # En caso de que se ingrese un número (opcion) que no hay.
			print("No hay opciones mas alla del #8, intenta con un numero menor a ese, ok?")

		input() # Esperar entrada del usuario al final de cada iteracion
	except ValueError: # En caso de que no se ingrese un numero.
		print("Ingresa un valor correcto.")
		input()