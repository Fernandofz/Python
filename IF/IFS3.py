print "--------Ejercicio3--------"
print ""
print "-----orden ascendente------"

num1=input("ingrese primer numero ")
num2=input("ingrese segundo numero ")
if (num2>num1):
	aux=num1
	num1=num2
	num2=aux

num3=input("ingrese tercer numero ")
if (num3>num1):
	aux=num1
	num1=num3
	num3=num2
	num2=aux
	
if (num3>num2):
	aux=num2
	num2=num3
	num3=aux



print ("%s >> %s >> %s") % (num3,num2,num1)