# Números
# Enteros- Integers
"""
   Los números enteros los podemos: 
   sumar (+), 
   restas (-), 
   multiplicar (*)
   dividir (/) 
   División entera (//) 
   potencias (**n)
"""
print("Suma")
print(2+3)
print("Resta")
print(3-2)
print("Multi")
print(2*3)
print("División")
print(3/2)
print("Módulo")
print(10%2) #Módulo (Mod)
print("Edad")
age = 18
print(age)

"""
Python llama flotantes a todos los numeros con punto decimal
"""
print(.2 + .5)
print(.2 - .3)
print(.2 * .4)
#Imprimir la edad de alguien
edad = 34 #varianle del tipo int
#message = "Charly tiene" + age + "años" #Python no puede poner eneteros en un string
""""
BUILD-IN son métodos que vienen integrados a python 
Ejemplos: 
print() 
str() 
type()
"""
message = "Charly tiene " + str(edad) + " años" #STR convierte un int a string
print(message)
#type error
"""
python no puede reconocer el tipo de
 información que se esta uasndo
"""
message_f = f"Charly tiene {edad} años"
print(message_f)

#Método build-in type()
print(type(age), type(edad), type("hola"), type(.5), type(True))