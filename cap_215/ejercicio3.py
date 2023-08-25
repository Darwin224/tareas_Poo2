#Ejercicio3: Escribe un programa para pedire al usuario el numero de horas y la tarifa por hora para calcular el salario bruto




def calcular(horas, tarifa):
    print("Salarios: {}".format(horas*tarifa))

horas= int(input("Ingrese el numero de horas: "))
tarifa= float(input("Ïngrese la tarifa: "))
calcular(horas,tarifa)