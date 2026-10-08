#STRINGS
"""
Un string es de manera sencilla una serie de caracteres en Python, todo
lo que se encuentre en comillas simples '' o dento de comullas dobles "

     EJemplo
    "Esto es un string"
    'Esto tambien es un string'
    'Le dije a un amigo, "python es mi lenguaje fav"'
    "El lenguaje 'pyhton' lleba el nombre por Monty Pyhton, no por la serpiente"
    Ejempo INCORRECTO
    "Esto NO es un string'
    'NI esto"
"""
name = "jaime david sanchez hernanddez"
print(name)
print(name.title())
print(name)
name = name.title()  
"Cambia el contenido permanente de la varible"
print(name)
#MÉTODOS
"""
Un método es una acción que puede hacer python sobre un variable

El punto después de la variable, segiodo del nombre del método, en este caso 'title()'
dice que se tiene que ejecutar el método title() de la variable name

Todos los métdos van seguidos de pareéntesis, pq en ocaciones necesitan info adicionakl para funcionar.
Aquí, el método .tilte() no requiere info adicional para ejecutarse
"""
#OTROS MÉTODOS
print(name.upper())
print(name.lower())
