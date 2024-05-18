#Ejemplo 1 if simple

#color=input("Ingresa un color: ")

#if color=="rojo":
#    print("Soy el color rojo")

#Ejemplo 2 if compuesto

#color=input("Ingresa un color: ")

#if color=="rojo":
#    print("Soy el color rojo")
#else:
#    print("No soy el color rojo, soy otra cosa")

#Ejemplo 3 if anidado

#color=input("Ingresa un color: ")

#if color=="rojo":
#    print("Soy el color rojo")
#    if color!="rojo":
#     print("No soy el color rojo")
#else:
#    print("No soy el color rojo, soy otra cosa")

#Ejemplo 4 if y elif

#color=input("Ingresa un color: ")

#if color=="rojo":
#    print("Soy el color rojo")
#elif color=="amarillo":
#    print("Soy el color amarillo")
#elif color=="azul":
#    print("Soy el color azul")
#elif color=="morado":
#    print("Soy el color morado")
#else:
#    print("No soy ninguno de los anteriores")

#Ejemplo numero 5: Crear un programa que solicite el número de la semana
#e imprimir en pantalla el día que corresponde

dia=int(input("Ingresa el día de la semana (1 al 7)"))

if dia=="1":
    print("Domingo")
elif dia=="2":
    print("Lunes")
elif dia=="3":
    print("Martes")
elif dia=="4":
    print("Miércoles")
elif dia=="5":
    print("Jueves")
elif dia=="6":
    print("Viernes")
elif dia=="7":
    print("Sábado")
else:
    print("No coincide a ningún día de la semana, inténtelo de nuevo")