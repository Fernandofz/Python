print "--------Ejercicio2--------"
print ""
print "-----Promedio de 3 numeros------"

num1=input("ingrese primer numero ")
num2=input("ingrese segundo numero ")
num3=input("ingrese tercer numero ")
prom=(float(num1)+float(num2)+float(num3))/3
print ("el promedio es %.2f")%(prom)
if (num1==prom):
	print ("el primer numero %s igual al promedio") %(num1)
if (num2==prom):
	print ("el segundo numero %s igual al promedio") %(num2)
if (num3==prom):
	print ("el tercer numero %s igual al promedio") %(num3)
if (num1>prom):
	print ("el primer numero %s es mayor al promedio") %(num1)
if (num2>prom):
	print ("el segundo numero %s es mayor al promedio") %(num2)
if (num3>prom):
	print ("el tercer numero %s es mayor al promedio") %(num3)
print ""
print "--------FIN--------"