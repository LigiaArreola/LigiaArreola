#Concatenar cadenas de caracteres con contenido de variables

nombre="Ligia Isabela Arreola Galindo"
especialidad="Área de Desarrollo de Software Multiplatafarma"
carrera="Ingeniero en Gestión y Desarrollo de Software"

#1er forma de concatenar
print("Mi nombre es: "+nombre+"estoy en la especialidad de: "+especialidad+",en da carrera de: "+carrera+)

print("/n")

#2da forma de concatenar
print("Mi nombre es: ",nombre,"estoy en la especialidad de: ",especialidad,", en la carrera de: ",carrera)

print("/n")

#3er forma de concatenar COMÚN EN PYTHON

print("Mi nombre es: {nombre} estoy en la especialidad de: {especialidad} , en da carrera de: {carrera}")

print("/n")

#4ta forma de concatenar

print(f"Mi nombre es: {} estoy en la especialidad de: {} ,en da carrera de: {}". format (nombre, especialidad, carrera)) 

print("/n")

#5ta forma de concatenar

print('Mi nombre es:'+nombre+'estoy en la especialidad de:'+especialidad+',en da carrera de:'+carrera+)