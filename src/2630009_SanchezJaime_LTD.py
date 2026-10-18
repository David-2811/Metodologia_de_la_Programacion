# Manejo de Listas, Tuplas y Diccionarios en Python

'''
    Nombre: Jaime David Sanchez Hernandez
    Matricula: 2630009
    Grupo: IM - 1
'''
"""
    Resumen ejecutivo:
El tipo de dato int representa números enteros, mientras que float permite 
representar números con decimales.
Los valores booleanos pueden ser True (verdadero) o False (falso).
Las comparaciones, como >=, < e ==, generan resultados booleanos.
Los operadores lógicos, como and y or, permiten combinar condiciones 
para tomar decisiones.
La validación de rangos ayuda a detectar valores no válidos antes de realizar
los cálculos.
Es importante comprobar los datos antes de realizar divisiones para evitar
la división entre cero.
Este documento presenta seis problemas que utilizan tipos de datos numéricos
y booleanos en Python.
Cada problema incluye descripción, entradas, salidas, validaciones y tres casos
de prueba.
Los programas realizan cálculos numéricos y utilizan condiciones booleanas
para determinar resultados.
"""
"""
    Principios y buenas practicas:
- Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar.
- Usar diccionarios cuando necesites buscar información por una clave.
- Evitar modificar una lista mientras la recorres con un for,
a menos que sepas exactamente lo que haces.
- Usar nombres de claves descriptivos en los diccionarios.
- Escribir código legible y mensajes claros para el usuario.
"""

"""
Problem 1: Shopping list basics (list operations)
 
Description:
This program builds a list of products from a text separated by commas.
It adds a new product at the end of the list, shows the total number
of items and checks (is_in_list) whether a product is in the list.
The search is done after the new item has been added.
 
Inputs:
- initial_items_text: A string with items separated by commas.
- new_item: A string with the item to add.
- search_item: A string with the item to search.
 
Outputs:
- "Items list: <items_list>"
- "Total items: <len_list>"
- "Found item: true|false"
- "Error: invalid input" if the input is invalid.
 
Validations:
- initial_items_text, new_item and search_item must not be
  empty after strip().
- The text is split by commas and extra spaces are removed from
  each item. Items are saved in lowercase.
- Decision: an initial list that ends up empty (for example ",,")
  is not accepted and shows "Error: invalid input".
 
Test cases:
1) Normal: "apple,banana,orange", new_item = "grape",
   search_item = "banana"
   -> Items list: ['apple', 'banana', 'orange', 'grape']
   -> Total items: 4
   -> Found item: true
2) Border: " Apple ", new_item = "pear", search_item = "PEAR"
   (one item, extra spaces and uppercase letters)
   -> Items list: ['apple', 'pear']
   -> Total items: 2
   -> Found item: true
3) Error: "   ", new_item = "kiwi", search_item = "kiwi"
   -> Error: invalid input
"""

print('---Problem 1: Shopping list basics (list operations)---')
# Input
initial_items_text = input("Enter initial items separated by commas: ").strip()
new_item = input("Enter the new item to add: ").strip().lower()
search_item = input("Enter the item to search: ").strip().lower()
 
# Validation
if not initial_items_text or not new_item or not search_item:
    print("Error: invalid input")
else:
    # Create the list: split by commas and remove extra spaces
    items_list = []
    for raw_item in initial_items_text.lower().split(","):
        clean_item = raw_item.strip()
        if clean_item:
            items_list.append(clean_item)
 
    # Validate that the initial list is not empty
    if len(items_list) == 0:
        print("Error: invalid input")
    else:
        # Add the new item at the end
        items_list.append(new_item)
 
        # Count the items and search the item
        len_list = len(items_list)
        is_in_list = search_item in items_list
 
        # Output
        print("Items list:", items_list)
        print("Total items:", len_list)
        print("Found item:", str(is_in_list).lower())
 


"""
Problem 2: Points and distances with tuples
 
Description:
This program creates two points in a 2D plane using tuples,
point_a = (x1, y1) and point_b = (x2, y2). It calculates the
Euclidean distance between them and creates a new tuple
midpoint with the middle point.
 
Inputs:
- x1: A float with the x coordinate of point A.
- y1: A float with the y coordinate of point A.
- x2: A float with the x coordinate of point B.
- y2: A float with the y coordinate of point B.
 
Outputs:
- "Point A: (x1, y1)"
- "Point B: (x2, y2)"
- "Distance: <distance>" (2 decimals)
- "Midpoint: (mx, my)" (2 decimals)
- "Error: invalid input" if the input is invalid.
 
Validations:
- The four inputs must be convertible to float.
- Values like nan or inf are rejected, and so are numbers so large
  that the distance cannot be calculated (for example 1e200).
- No additional restrictions on the range (negatives are allowed).
 
Test cases:
1) Normal: x1 = 0, y1 = 0, x2 = 3, y2 = 4
   -> Point A: (0.0, 0.0)
   -> Point B: (3.0, 4.0)
   -> Distance: 5.0
   -> Midpoint: (1.5, 2.0)
2) Border: x1 = 2, y1 = 2, x2 = 2, y2 = 2 (same point)
   -> Point A: (2.0, 2.0)
   -> Point B: (2.0, 2.0)
   -> Distance: 0.0
   -> Midpoint: (2.0, 2.0)
3) Error: x1 = 1, y1 = abc, x2 = 3, y2 = 4
   -> Error: invalid input
"""
 
print('\n---Problem 2: Points and distances with tuples---')
INFINITY = float("inf")
 
# Input
is_valid_input = True
x1 = 0.0
y1 = 0.0
x2 = 0.0
y2 = 0.0
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
except ValueError:
    is_valid_input = False
 
# Validation: reject nan and inf
if is_valid_input:
    for coordinate in (x1, y1, x2, y2):
        if not (-INFINITY < coordinate < INFINITY):
            is_valid_input = False
 
if is_valid_input:
    # Create the tuples
    point_a = (x1, y1)
    point_b = (x2, y2)
 
    # Euclidean distance (very large values overflow, so they are rejected)
    distance = 0.0
    try:
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    except OverflowError:
        is_valid_input = False
 
if is_valid_input:
    # Midpoint
    midpoint = (round((x1 + x2) / 2, 2), round((y1 + y2) / 2, 2))
 
    # Output
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)
else:
    print("Error: invalid input")
 
 
"""
Problem 3: Product catalog with dictionary
 
Description:
This program manages a small catalog of products using a dictionary
(key: product name, value: unit price as float). It reads a product
name and a quantity and calculates the total to pay if the product
exists in the catalog.
 
Catalog (product_prices):
- "apple": 10.0, "banana": 5.5, "orange": 8.0, "milk": 22.5
 
Inputs:
- product_name: A string with the name of the product.
- quantity: An int with the quantity to buy.
 
Outputs:
- If the product exists:
  - "Unit price: <unit_price>"
  - "Quantity: <quantity>"
  - "Total: <total_price>"
- If the product does not exist: "Error: product not found"
- If the input is invalid: "Error: invalid input"
 
Validations:
- product_name must not be empty after strip().
- product_name is saved in lowercase before searching it.
- quantity must be convertible to int and be greater than 0.
- Use "in" to check that product_name is a key of the dictionary.
 
Test cases:
1) Normal: product_name = "apple", quantity = 3
   -> Unit price: 10.0
   -> Quantity: 3
   -> Total: 30.0
2) Border: product_name = " Banana ", quantity = 1
   -> Unit price: 5.5
   -> Quantity: 1
   -> Total: 5.5
3) Error: product_name = "pizza", quantity = 2
   -> Error: product not found
   Error: product_name = "apple", quantity = 0
   -> Error: invalid input
"""
 
print('\n---Problem 3: Product catalog with dictionary---')
# Catalog
product_prices = {
    "apple": 10.0,
    "banana": 5.5,
    "orange": 8.0,
    "milk": 22.5
}
 
# Input
product_name = input("Enter the product name: ").strip().lower()
quantity_text = input("Enter the quantity to buy: ").strip()
 
# Validation
is_valid_input = True
quantity = 0
if not product_name:
    is_valid_input = False
else:
    try:
        quantity = int(quantity_text)
        if quantity <= 0:
            is_valid_input = False
    except ValueError:
        is_valid_input = False
 
if not is_valid_input:
    print("Error: invalid input")
elif product_name in product_prices:
    # Calculate the total
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
 
    # Output
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", round(total_price, 2))
else:
    print("Error: product not found")
 
 
 
"""
Problem 4: Student grades with dict and list
 
Description:
This program manages the grades of a group using a dictionary
(key: student name, value: list of grades as float). It reads a
student name, calculates the average of the grades and uses the
boolean is_passed (average >= 70.0) to show if the student passed.
 
Grades (grades_dict):
- "Alice": [90.0, 85.0, 78.5]
- "Bob": [60.0, 70.0, 80.0]
- "Carla": [55.0, 60.0, 65.0]
- "Diego": [] (a student without grades)
 
Inputs:
- student_name: A string with the name of the student.
 
Outputs:
- If the student exists:
  - "Grades: <grades_list>"
  - "Average: <average>"
  - "Passed: true|false"
- If the student does not exist: "Error: student not found"
- If the name is empty: "Error: invalid input"
- If the list of grades is empty: "Error: no grades available"
 
Validations:
- student_name must not be empty after strip().
- student_name is converted to Title Case before searching it.
- Use "in" to check that student_name is a key of the dictionary.
- The list of grades must not be empty before calculating
  the average (this avoids dividing by zero).
 
Test cases:
1) Normal: student_name = "alice"
   -> Grades: [90.0, 85.0, 78.5]
   -> Average: 84.5
   -> Passed: true
2) Border: student_name = " Bob " (average exactly 70.0)
   -> Grades: [60.0, 70.0, 80.0]
   -> Average: 70.0
   -> Passed: true
3) Error: student_name = "Zoe"
   -> Error: student not found
   Error: student_name = "Diego"
   -> Error: no grades available
   Error: student_name = "   "
   -> Error: invalid input
"""
 
print('\n---Problem 4: Student grades with dict and list---')
# Grades
grades_dict = {
    "Isa": [90.0, 85.0, 78.5],
    "Bob": [60.0, 70.0, 80.0],
    "Carla": [55.0, 60.0, 65.0],
    "Diego": []
}
PASSING_GRADE = 70.0
 
# Input
student_name = input("Enter the student name: ").strip().title()
 
# Validation
if not student_name:
    print("Error: invalid input")
elif student_name not in grades_dict:
    print("Error: student not found")
else:
    grades_list = grades_dict[student_name]
 
    if len(grades_list) == 0:
        print("Error: no grades available")
    else:
        # Calculate the average and the boolean
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= PASSING_GRADE
 
        # Output
        print("Grades:", grades_list)
        print("Average:", round(average, 2))
        print("Passed:", str(is_passed).lower())
 

 
"""
Problem 5: Word frequency counter (list + dict)
 
Description:
This program counts how many times each word appears in a sentence.
It converts the sentence to lowercase, removes simple punctuation
marks and creates a list of words and a dictionary of frequencies.
It also shows the most common word.
 
Inputs:
- sentence: A string with a sentence.
 
Outputs:
- "Words list: <words_list>"
- "Frequencies: <freq_dict>"
- "Most common word: <word>"
- "Error: invalid input" if the input is invalid.
 
Validations:
- sentence must not be empty after strip().
- Decision: the punctuation marks . , ; : ! ? ¿ ¡ " ( ) are
  replaced with a space using replace().
- The list of words must not be empty (for example "!!!").
- If there is a tie, the first word that reached the highest
  frequency is shown (any of them is valid).
 
Test cases:
1) Normal: "The cat and the dog and the bird"
   -> Words list: ['the', 'cat', 'and', 'the', 'dog', 'and', 'the', 'bird']
   -> Frequencies: {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}
   -> Most common word: the
2) Border: "Hello, hello!" (punctuation and uppercase letters)
   -> Words list: ['hello', 'hello']
   -> Frequencies: {'hello': 2}
   -> Most common word: hello
3) Error: "   "
   -> Error: invalid input
   Error: "!!!"
   -> Error: invalid input
"""
 

print('\n---Problem 5: Word frequency counter (list + dict)---')
PUNCTUATION_MARKS = '.,;:!?¿¡"()'
 
# Input
sentence = input("Enter a sentence: ").strip()
 
# Validation
if not sentence:
    print("Error: invalid input")
else:
    # Normalize: lowercase and no punctuation
    clean_sentence = sentence.lower()
    for mark in PUNCTUATION_MARKS:
        clean_sentence = clean_sentence.replace(mark, " ")
 
    # Create the list of words
    words_list = clean_sentence.split()
 
    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        # Build the dictionary of frequencies
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
 
        # Find the most common word
        most_common_word = words_list[0]
        highest_frequency = 0
        for word in freq_dict:
            if freq_dict[word] > highest_frequency:
                highest_frequency = freq_dict[word]
                most_common_word = word
 
        # Output
        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)
 
 