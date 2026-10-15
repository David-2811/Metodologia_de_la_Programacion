# If Statement
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car)



# El condicional
# El condicional es el corazon del IF

# Para determinar igualdad ==
# Condicional True
# Condicional Verdadero
truck = "ford"
print(truck == "ford") # 

# Condicional False 
# Condicional Falso

print('Condicional Falso')
print(truck ==  'cheyenne')


# Condicional != para determinar desigualdad 
print('Condicional de desigualdad')
print(truck!= 'tacoma') # True
print(truck!= 'ford') # False

print('\nComparaciones numericas')
age = 34
print(age == 34) # True
print(age == 18) # False
print(age == '34') # False

answer = 17
if answer != 42:
    print('Esa no es la resuesta correcta')

age = 19
# Simbolo menor que  
print(age < 21) #True
print(age <= 21) #True
print(age > 21) #True
print(age >= 21) #False
