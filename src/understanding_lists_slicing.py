players = ["peter", "mercado", "aron", "fatima", "renata"]
print("Lista original: ", players)

#Slicing
print(players[3:5]) # ["fatima", "renata"]


"""

El slicing me  permite trabajar con un grupo especifico de una lista: al resultado se le conoce como 
'un slice'.
players = [peter, mercado, aron, fatima, renata]

"""
print("1:4", players[1:4]) 
print(":3", players[:3])
print("2: ", players[2:])
print("[-3:]", players[-3:])

# Casos Especiales
print("Casos Especiales")
print(players[1:10])
print(players[-10:10])
print(players[6:1])
print(players[6:1])
print(players[:0])
print(players[0:1])

    #Looping
print("Looping through a slice")
students = ["peter", "mercado", "aron", "fatima", "renata"]

#Slicing [::] Tarea
for student in students[3:5]:
    print(f"El estudiante {student}, va a pasar la materia.")

print(student)

# ¿Como podemos hacer un copia de un lista?
my_food = ["pizza", "tacos", "flautas"] 
my_friend_food = my_food # Manera erronea de copiar una lista


# Tres maneras de copiar una lista 

# Metodo 1 - Utilizando Slicing 
my_friend_food = my_food[:]

# Metodo 2 - Utilizando el metodo de listas .copy()
my_friend_food = my_food.copy()

# Metodo 3 - Utilizando el metodo Build-In list()
my_friend_food = list(my_food)

