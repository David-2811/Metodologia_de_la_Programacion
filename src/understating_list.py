
"""
Las listas nos permiten almacenar informacion en un lugar 
la cantidad que dese : ya sean pocos elementos 
o millones de elementos 

Una lista es una coleccion de items (elemntos) que tienen un
orden patricular se pueden crear listas que incluyan strings,
enteros,floats, los nombres de las personas de tu familia, etc
Podemos almacenar (los tipos de datos permitidos en python) 
lo que queramos en una lista 

Son elementos Mutables: Puede modificarse el tamaño de la lista

Se recomienda nombrar una varianle del tipo lista en plural 

En python, los corchets [] indican una lista,
sus elementos se separan por comas.

Ejemplo:

"""

bicycles = ['trak','cannondale','redline','Sepecializaed',"apache" ]
print(bicycles)

#Como podemos acceder a los elementos de una lista 

"""
Las listas son colecciones ordenadas.Se pueden acceder a un elemntos
de una lista diciendole a python la posicion o indice del
elemento deseado 

Para obtener el valor deseado, se debe escribir el nombre de 
la lista, seguido del indice del elemento entre corchetes 

"""

print(bicycles[0],bicycles[1], bicycles[2])

print(bicycles[0].upper())

#Los indices comienzan en 0, no 1 
#bicycles = ['trak','cannondale','redline','Sepecializaed',"apache" ]

# ejemplo 
print(bicycles[1]) # = cannondale
print(bicycles[3]) # = specializated

# accediendo al ultimo elemento de una lista

print(bicycles[-1]) # = apache
print(bicycles[-2]) # = specializaed

# Utilizando valores individuales de una lista 
message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)
