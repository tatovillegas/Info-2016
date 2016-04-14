# -*- coding: utf-8 -*-
"""num1 = input ("Ingrese un numero: ")
num2 = input ("Ingrese otro numero: ")
result = num1 + num2
print "El resultado de la suma es:", result"""


"""Nac = input ("Ingrese su año de nacimiento: ")
Fut = input ("Ingrese el año que desea saber: ")
Edad = Fut - Nac
print "Su edad en el futuro sera:", Edad"""

"""Realice el programa que permita ingresar un precio y devuelva como resultado el precio con el IVAincluido (+21)
Num = input ("Ingrese el precio a calcular: ")
Result = Num + Num * 0.21
print "El precio con IVA incluido es: ", Result""" 

"""La presión, el volumen y la temperatura de una masa de aire se relacionan por 
la fórmulade masa= (presión x volumen) / ((0,37 x (Tº + 460)). El programa debe obtener los datos para calcular la masa

Pres = float (input ("Ingrese el valor de la presion atmosferica: "))
Vol = float (input ("Ingrese el valor del volumen: "))
Temp = float (input ("Ingrese el valor de la temperatura actual: "))
Masa =  (Pres * Vol) / (0.37 * (Temp + 460))
print "La masa es de: ", Masa """

"""Calcular el nuevo salario de un obrero si obtuvo un incremento de un 25% sobre su salario anterior

salario = float (input ("Ingrese su salario anterior:"))
newsal = salario + salario * 0.25
print "Su salario actual es: ", newsal """

"""En un hospital existen tres áreas: Odontología, pediatría y traumatología. 
El presupuesto anual del hospital se reparte conforme a la siguiente tabla:
Área   % Presupuesto
Odontología   40%
Traumatología 30%
Pediatría     30%
Obtener la cantidad de dinero que recibiría cada área para
cualquier monto de presupuesto.

Presu = float (input ("Ingrese el presupuesto anual del hospital: "))
Odonto = Presu * 0.40
Trauma = Presu * 0.30
Pedia = Presu * 0.30
print "El area de Odontología recibira: ", Odonto 
print "El area de Traumatología recibira: ", Trauma 
print "El area de Pediatría recibira: ", Pedia """

""" Se compra un artículo a un precio determinado. 
Obtener el precio en el que se lo debe vender
para obtener una ganancia de un 30% 

Prod = float (input ("Ingrese el valor de costo del producto: "))
Sugerido = Prod + (Prod * 0.30)
print "El valor sugerido de venta es de: ", Sugerido """

""" Tres personas deciden invertir su dinero para fundar una empresa,
cada una de ellas invierte una cantidad  distinta.  Obtener  el  
porcentaje  que  cada  cual  invierte  con  respecto  a  la  
cantidad  total invertida 

Inv1 = float (input ("Ingrese el monto que invirtio la primera persona: "))
Inv2 = float (input ("Ingrese el monto que invirtio la segunda persona: "))
Inv3 = float (input ("Ingrese el monto que invirtio la tercera persona: "))
Total = float (Inv1 + Inv2 + Inv3)
print  "La invercion es de: ", Total
Porc1 = float ((Total * Inv1) / 100 )
Porc2 = float ((Total * Inv2) / 100 )
Porc3 = float ((Total * Inv3) / 100 )
print  "La primera persona invirtio el: ", Porc1
print  "La segunda persona invirtio el: ", Porc2
print  "La tercera persona invirtio el: ", Porc3 """

"""Un alumno desea saber cuál va a ser su promedio general en las
tres materias que cursa y cuál va a ser el promedio que obtendrá en cada 
una de ellas.Estas materias se evalúan como se muestra a continuación:
Matemática. El examen pesa 90 % de la nota, promedio de tareas 10% y
se pidieron un total de tres tareas.
Física. El examen 80 %, promedio de tareas 20 % y se pidieron dos tareas.
Química. El examen 85 %, promedio de tareas 15% y se pidieron un total
de tres tareas """

ExaMat = float (input ("Ingrese la nota del examen de matematicas: "))
TarMat1 = float (input ("Ingrese la nota de la primer tarea de matematicas: "))
TarMat2 = float (input ("Ingrese la nota de la segunda tarea de matematicas: "))
TarMat3 = float (input ("Ingrese la nota de la tercer tarea de matematicas: "))
PromTar = float (TarMat1 + TarMat2 + TarMat3)/3
NotaMat = float (ExaMat * 0.90 + PromTar * 0.10)
ExaFis = float (input ("Ingrese la nota del examen de fisica: "))
TarFis1 = float (input ("Ingrese la nota de la primer tarea de fisica: "))
TarFis2 = float (input ("Ingrese la nota de la segunda tarea de fisica: "))
PromTarFis = float (TarFis1 + TarFis2 )/2
NotaFis = float (ExaFis * 0.80 + PromTar * 0.20) 
ExaQuim = float (input ("Ingrese la nota del examen de quimica: "))
TarQuim1 = float (input ("Ingrese la nota de la primer tarea de quimica: "))
TarQuim2 = float (input ("Ingrese la nota de la segunda tarea de quimica: "))
TarQuim3 = float (input ("Ingrese la nota de la tercer tarea de quimica: "))
PromTarQuim = float (TarQuim1 + TarQuim2 + TarQuim3)/3
NotaQuim = float (ExaMat * 0.90 + PromTar * 0.10)
PromGral = float (NotaMat + NotaQuim + NotaFis)/3
print "Su promedio de Matemáticas es: ", NotaMat
print "Su promedio de Fisica es: ", NotaFis
print "Su promedio de Química es: ", NotaQuim
print "Su promedio de general es: ", PromGral

