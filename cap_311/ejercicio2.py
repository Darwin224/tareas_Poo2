#Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
#programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
#un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones

def calcular(horas, tarifa):
    if horas>40:
        salNormal = 40*tarifa
        horasExtra= horas-40
        SalarioExtra = horasExtra*tarifa*1.5
        print("Salario: {}".format(salNormal+SalarioExtra))
    else:
        salNormal = horas*tarifa
        print("Salarios: {}".format(salNormal))
        

try:
    horas= int(input("Ingrese el numero de horas: "))
    tarifa= float(input("Ïngrese la tarifa: "))
    calcular(horas,tarifa)
except ValueError:
    print("Error, por favor introduzca un número")