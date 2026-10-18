age = input ("\n Ingresa tu edad: ")
print(age)
#rint(type(age))
age = int(age)
#rint(type(age))

if age <= 4:
    cost=0

if age > 4 and age < 18:
    cost = 200

if age >= 18:
    cost = 500

print(f"El costo de boleto es: {cost}")

# Bloque if-elf-else

if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost = 200
elif age > 18:
    cost = 500
elif age >= 65:
    cost = 0
else:
    cost = 0

print("Bloque if-elf-else")
print(f"El costo del boleto es: {cost}")

