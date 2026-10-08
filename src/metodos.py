"""
Print :
Sintaxis: print(*objects, sep=' ', end='\n', 
file=sys.stdout, flush=False)
Definición: Función integrada (built-in) que imprime/muestra valores u objetos en la salida estándar (consola/pantalla).

# Ejemplo 1: Imprimir texto simple
print("Hola Mundo")

# Ejemplo 2: Imprimir varias variables con un separador personalizado
nombre = "Ana"
edad = 25
print(nombre, edad, sep=" -> ")  # Salida: Ana -> 25

STR :
Sintaxis: str(object='') o métodos como 'texto'.método()
Definición: Clase/tipo de dato integrados que representa cadenas de texto inmutables.
 Contiene métodos como .upper(), .lower(), .strip(), .split(), .join(), .replace(), entre otros.

 texto = "  python es genial  "

# 1. Limpiar espacios alrededor
print(texto.strip())  # "python es genial"

# 2. Convertir a mayúsculas
print(texto.upper())  # "  PYTHON ES GENIAL  "

# 3. Reemplazar palabras
print(texto.replace("genial", "fácil"))  # "  python es fácil  "

# 4. Separar en lista de palabras
print("a,b,c".split(","))  # ['a', 'b', 'c']

Type :
Sintaxis: type(object)
Definición: Función integrada (built-in) que devuelve la clase o
 tipo de dato exacto al que pertenece un objeto especificado.

print(type("Hola"))  # Salida: <class 'str'>
print(type(100))     # Salida: <class 'int'>
print(type(3.14))    # Salida: <class 'float'>
 
""" 