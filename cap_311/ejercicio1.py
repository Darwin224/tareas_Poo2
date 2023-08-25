#Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
#1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

def calcular(horas, tarifa):
    if horas>40:
        salNormal = 40*tarifa
        horasExtra= horas-40
        SalarioExtra = horasExtra*tarifa*1.5
        print("Salario: {}".format(salNormal+SalarioExtra))
    else:
        salNormal = horas*tarifa
        print("Salarios: {}".format(salNormal))
        
horas= int(input("Ingrese el numero de horas: "))
tarifa= float(input("Ïngrese la tarifa: "))

calcular(horas,tarifa)