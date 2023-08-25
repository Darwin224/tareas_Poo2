#Ejercicio 5: Escribe un programa que le pida al usuario una temperatura en grados Celsius,
#la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.





def convertir(Celsius):
    temperaturaFahrenheit = (Celsius * 9/5) + 32
    print("La temperatura en grados Fahrenheit es: {}".format(temperaturaFahrenheit))

temperaturaCelsius = float(input("Ingrese la temperatura en grados Celsius: "))
convertir(temperaturaCelsius)