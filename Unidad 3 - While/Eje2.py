empleados=input("por favor ingrese la cantidad de empleados: ")
sueldo=0;
presupuesto=0;
cantidad300=0;
cantidad500=0;
while (empleados != 0):
	sueldo=input("por favor ingrese el sueldo del empleado: ") + sueldo
	presupuesto=presupuesto+sueldo
	empleado=empleado-1
	if ((sueldo>=100)&&(sueldo <=300)):
		cantidad300=cantidad300+1
	elif (sueldo <= 500):
		cantidad500 = cantidad500+1
	else:
		print "error sueldo fuera de rango"
print "la cantidad total de empleados que cobran entre 100 y 300 es: ",cantidad300
print "la cantidad total de empleados que cobran entre 300 y 500 es: ",cantidad500
print "el personal cuesta: ",presupuesto

