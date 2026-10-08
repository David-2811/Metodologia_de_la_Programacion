# Agregando elementos a una lista

motorcycles = ['honda', 'mortalika' , 'yanaha']

print(motorcycles)

motorcycles.append("kawasaki")

print(motorcycles)

"""
El metodo append ayuda a crear listas facilmente 
de manera dinamica 

"""

motorcycles_2 = [] #Lista vacia 
print(motorcycles_2)
motorcycles_2.append ("honda")
motorcycles_2.append ("Yamaha")
motorcycles_2.append ("Susuki")
print(motorcycles_2)



# Metodo .pop() Elimina el ultimo elemento de la lista 
# Pero nos permite utilizar el elemento despues de elminarlo
print("\n\t Aqui aprendi a utilizar el metodo pop".upper())
motorcycles_4 = ['honda','suzuki','hd','mortalika']
print(motorcycles_4) #=('honda','suzuki','hd','mortalika')
deleted_motorcycle = motorcycles_4.pop() #=('honda','suzuki','hd')
print(f"tu motocicleta borrada es {deleted_motorcycle}")
print(motorcycles_4)

#El metodo .pop tambien se puedde utilizar para eliminar un elemento en especifico 
motorcycles_5 = ['honda','suzuki','hd','mortalika']
print(motorcycles_5)

motorcycles_5.pop(0)
print(motorcycles_5) #Lista sin honda