print("El dia de hoy voy a trabajar con listas".upper())

magicans = ['harry','ron','hermione','snape','voldemort']

print(magicans)

print("imprimir a la mala")

print(magicans[0],magicans[1],magicans[2],magicans[3],magicans[4])

#ciclo for
#for tiene salto de linea 
print("imprimir con un for")
for magican in magicans:
    #se agrega el end para que se imprima en una sola lineal 
    #y se le agrega end y comillias mas espacio para que no 
    #este junto 
    print(magican, end= " ")

"""
a esto se le conoce como un looping 

magicans = ['harry','ron','hermione','snape','voldemort']
ahora cada mago imprimira un mensaje
"""


for magican in magicans:
   print(f"{magican.title()} ese fue un gran echizo " )
   print(f"No puedo esperar a ver el siguiente echizo ,{magican.upper()}\n" )
print("Graciaas a todos eso fue un gran espectaculo")

print(" ")

#identacion
"""
Pyton utiliza la identacion para determinar cuando una linea de codigo
esta conectado a la linea del codigo anterior 

Basicamente, se utilizan 4 espacios en blanco para obligarnos a escribir
codigo ordenado y estructurado.
"""

"""
#no olvidemos identar 
magicans = ["Alice","david","caroline"]
for magican in magicans:
print(magican) error de identacion 

"""
# error de identacion -identation error 
magicans = ["Alice","david","caroline"]
for magican in magicans:
print(magican) 


#Error de logica - logic error 
for magician in magicans:
   print(magician)
   #el print no esta bien identado ya que el print solo funciona con el ultimo 
   #elemento de la lista 
print (f"No puedo esperar a ver el siguiente truco",)


#identacion inecesaria - identacion error 
#no es necesaria la idetacion ya que no lleva un for un if etc.
message = "hello python world"
    print(message)

#Np olvidar los dos puntos - Syntax error 
for magician in magicans
    print(magician)