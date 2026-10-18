# Manejo de los Strings en Python

'''
    Nombre: Jaime David Sanchez Hernandez 
    Matricula: 2630009
    Grupo: IM - 1
'''

'''
    Resumen Ejecutico:
Un string es un tipo de dato que almacena texto
y es inmutable. Permite concatenar, medir longiud,
extraer cadenas, buscar patrones y remplazar texto.
Validar y normalizar datos ayuda a evitar errores 
en nombres y correos. El documento incluira la 
descripcion de cada problema, entradas, salidas 
validaciones, metodos usados, casos de pueba y 
el codigo correspondiente.
'''

'''
    Principios y buenas practicas:
-Los strings son inmutables: cualquier cambio genera
una nueva cadena.
-Es una buena practica normalizar entrada con 
strip() y lower() antes de compararla.
-Evitar "numeros magicos en indices; documentar
que extrae cada slice.
-Usar metodos de strings en lugar de reescribir 
logica basica.
-Diseñar validaciones claras: primero que no este
vacio, luego el formato.
-Escribir codigo legible: nombres de variables 
claros y mensajes de error entendibles.
'''

'''
    Problem 1: Full name formatter
-This program reads a text string from the user.
-It removes surrounding whitespace and calculates
its length.

 Inputs:
 -full_name: A string containing the persons full name.
 -It may contain uppercase, lowercase, or extra spaces.
 Outputs:
-The formatted full name in Title Case.
-The initials separated by periods.
-An error message if the input is invalid.
Validations:
-"full_name" must not be empty after "strip()".
-It must contain at least two words.
-Do not accept strings that consist only of spaces.

    Test cases:
1) Normal: "david sanchez Hernandez"
    -> Formatted name: David Sanchez Hernandez
    -> Initials: D.S.H
2) Border: "    Jaime sanchez"
    -> Formatted name: Jaime Sanchez
    -> Initials: J.S.
3) Error: "   "
    -> Error: invalid input
   Error: "Jaime"
    -> Error: enter at least two words
'''

print('---Problem 1: Full name formatter---')
# Input
full_name = input("Enter your full name: ").strip()

# Validation
if not full_name:
    print("Error: invalid input")
else:
    # Normalize whitespace
    name_parts = full_name.split()

    if len(name_parts) < 2:
        print("Error: enter at least two words")
    else:
        # Format the full name
        formatted_name = " ".join(name_parts).title()

        # Generate the initials
        initials = ""
        for name_part in name_parts:
            initials += name_part[0].upper() + "."

        # Output
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")



"""
Problem 2: Simple Email Validator

Description:
This program validates the basic structure of an email address.
It checks the @ symbol, the domain period, and whitespace.
If the email is valid, it displays the domain part.

Inputs:
- email_text: A string containing an email address.

Outputs:
- "Valid email: true" if the email is valid.
- "Valid email: false" if the email is invalid.
- "Domain: <domain_part>" if the email is valid.

Validations:
- Remove leading and trailing whitespace using strip().
- Reject empty input.
- Require exactly one @ symbol.
- Reject email addresses containing spaces.
- Require at least one period after the @ symbol.
- Require text before and after the @ symbol.

Test cases:
1) Normal: 'sanhdzjaime11@gmail.com"
   -> Valid email: true
   -> Domain: gmail.com
2) Border: "a@b.c"
   -> Valid email: true
   -> Domain: b.c
3) Error: 'sanhdzjaime11gmail.com'
   -> Valid email: false
"""

print('\n---Problem 2: Simple Email Validator---')
# Input
email_text = input("Enter an email address: ").strip()

# Initial validation
if not email_text:
    print("Valid email: false")
else:
    # Check the basic email structure
    at_count = email_text.count("@")
    at_position = email_text.find("@")

    is_valid = True

    if at_count != 1:
        is_valid = False
    elif " " in email_text:
        is_valid = False
    else:
        # Extract the local part and domain
        local_part = email_text[:at_position]
        domain_part = email_text[at_position + 1:]

        # Validate the local part and domain
        if not local_part or not domain_part:
            is_valid = False
        elif "." not in domain_part:
            is_valid = False
        elif domain_part.startswith(".") or domain_part.endswith("."):
            is_valid = False

    # Output
    if is_valid:
        print("Valid email: true")
        print(f"Domain: {domain_part}")
    else:
        print("Valid email: false")



"""
Problem 3: Palindrome Checker

Description:
This program determines whether a phrase is a palindrome.
It ignores spaces and uppercase or lowercase differences.
It compares the normalized phrase with its reversed version.

Inputs:
- phrase: A string containing a phrase to check.

Outputs:
- "Is palindrome: true" if the phrase is a palindrome.
- "Is palindrome: false" if the phrase is not a palindrome.
- "Normalized phrase: <normalized_phrase>" showing the cleaned phrase.

Validations:
- Remove leading and trailing whitespace using strip().
- Reject empty input.
- Remove spaces and convert the phrase to lowercase.
- Require at least three characters after removing spaces.

Test cases:
1) Normal: "Anita lava la tina"
   -> Is palindrome: true
   -> Normalized phrase: anitalavalatina
2) Border: " a n a "
   -> Is palindrome: true
   -> Normalized phrase: ana
3) Error: "   "
   -> Error: invalid input
"""

print('\n---Problem 3: Palindrome Checker---')
# Input
phrase = input("Enter a phrase: ").strip()

# Initial validation
if not phrase:
    print("Error: invalid input")
else:
    # Normalize the phrase
    normalized_phrase = phrase.lower().replace(" ", "")

    # Validate the normalized phrase
    if len(normalized_phrase) < 3:
        print("Error: phrase must contain at least 3 characters")
    else:
        # Reverse the normalized phrase
        reversed_phrase = normalized_phrase[::-1]

        # Check whether the phrase is a palindrome
        is_palindrome = normalized_phrase == reversed_phrase

        # Output
        print(f"Is palindrome: {str(is_palindrome).lower()}")
        print(f"Normalized phrase: {normalized_phrase}")



"""
Problem 4: Sentence Word Stats

Description:
This program analyzes a sentence entered by the user.
It removes extra spaces and separates the sentence into words.
It displays the word count, first word, last word,
shortest word, and longest word.

Inputs:
- sentence: A string containing a sentence.

Outputs:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"
- An error message if the input is invalid.

Validations:
- Remove leading and trailing whitespace using strip().
- Reject empty input.
- Split the sentence into words.
- Verify that at least one word exists after splitting.

Test cases:
1) Normal: "Python is very interesting"
   -> Word count: 4
   -> First word: Python
   -> Last word: interesting
   -> Shortest word: is
   -> Longest word: interesting
2) Border: "Hello"
   -> Word count: 1
   -> First word: Hello
   -> Last word: Hello
   -> Shortest word: Hello
   -> Longest word: Hello
3) Error: "   "
   -> Error: invalid input
"""

print('\n---Problem 4: Sentence Word Stats---')
# Input
sentence = input("Enter a sentence: ").strip()

# Initial validation
if not sentence:
    print("Error: invalid input")
else:
    # Split the sentence into words
    words = sentence.split()

    # Validate the word list
    if len(words) == 0:
        print("Error: invalid input")
    else:
        # Initialize the shortest and longest words
        shortest_word = words[0]
        longest_word = words[0]

        # Find the shortest and longest words
        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word

            if len(word) > len(longest_word):
                longest_word = word

        # Calculate the total number of words
        word_count = len(words)

        # Get the first and last words
        first_word = words[0]
        last_word = words[-1]

        # Output
        print(f"Word count: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")



"""
Problem 5: Password Strength Classifier

Description:
This program classifies a password as weak, medium, or strong.
It checks the password length and the types of characters it contains.
It uses uppercase letters, lowercase letters, digits, and symbols
to determine the password strength.

Inputs:
- password_input: A string containing the password.

Outputs:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"
- An error message if the password is empty.

Validations:
- Remove leading and trailing whitespace using strip().
- Reject empty input.
- Check the password length using len().
- Identify uppercase letters, lowercase letters, digits,
  and non-alphanumeric symbols.

Classification rules:
- Weak: The password has fewer than 8 characters.
- Medium: The password has at least 8 characters but does not
  contain all four required character types.
- Strong: The password has at least 8 characters and contains
  at least one uppercase letter, one lowercase letter,
  one digit, and one non-alphanumeric symbol.

Test cases:
1) Normal: "Hello123!"
   -> Password strength: strong
2) Border: "Abc12345"
   -> Password strength: medium
3) Error: ""
   -> Error: invalid input
"""

print('\n---Problem 5: Password Strength Classifier---')
# Input
password_input = input("Enter a password: ")

# Validation
if not password_input.strip():
    print("Error: invalid input")
else:
    # Initialize character type flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    # Check each character
    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    # Check password length
    password_length = len(password_input)

    # Classify password strength
    if password_length < 8:
        password_strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        password_strength = "strong"
    else:
        password_strength = "medium"

    # Output
    print(f"Password strength: {password_strength}")



"""
Problem 6: Product Label Formatter

Description:
This program creates a fixed-width label for a product.
It combines the product name and its positive price.
The final label contains exactly 30 characters.
Short labels are padded with spaces and long labels are truncated.

Inputs:
- product_name: A string containing the product name.
- price_value: A value that can be converted to a positive number.

Outputs:
- "Label: <exactly 30 characters>"
- An error message if the product name or price is invalid.

Validations:
- Remove leading and trailing whitespace from product_name using strip().
- Reject an empty product name.
- Convert price_value to a number and verify that it is positive.
- Reject values that cannot be converted to a number.
- Ensure that the final label contains exactly 30 characters.

Test cases:
1) Normal: product_name = "Book", price_value = "19.99"
   -> Label: "Product: Book | Price: $19.99"
      followed by 2 spaces to reach 30 characters.
2) Border: product_name = "Notebook", price_value = "5"
   -> The label is padded or truncated to exactly 30 characters.
3) Error: product_name = "   ", price_value = "10"
   -> Error: invalid input
"""

print('\n---Problem 6: Product Label Formatter---')
# Input
product_name = input("Enter product name: ").strip()
price_value = input("Enter product price: ").strip()

# Initial validation
if not product_name:
    print("Error: invalid input")
else:
    # Validate the price
    try:
        price_number = float(price_value)

        if price_number <= 0:
            print("Error: invalid input")
        else:
            # Format the price
            price_text = str(price_number)

            # Build the label
            label = f"Product: {product_name} | Price: ${price_text}"

            # Adjust the label to exactly 30 characters
            label = label[:30]
            label = label.ljust(30)

            # Output
            print(f'Label: "{label}"')

    except ValueError:
        print("Error: invalid input")


'''
    CONCLUCIONES:
El manejo de cadenas de texto en Python permite procesar,
modificar y organizar información de manera eficiente.
Aprendí a utilizar métodos como strip(), lower(), split() y join(),
así como a validar entradas y dar formato a los textos. También comprendí
la importancia de la inmutabilidad y el uso de índices y slicing. 
Estos conocimientos ayudan a crear programas más claros, ordenados
y confiables.

    REFERENCIAS:
1)Python Software Foundation. Tutorial de Python:
Entrada y salida de datos.
https://docs.python.org/3/tutorial/inputoutput.html
2)Python Software Foundation. Documentación oficial de Python:
Tipos integrados: cadenas de texto (str).
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
3)Python Software Foundation. Métodos de cadenas de texto en Python.
https://docs.python.org/3/library/stdtypes.html#string-methods
4)Python Software Foundation. Tutorial de Python:
Errores y excepciones en la programación.
https://docs.python.org/3/tutorial/errors.html
5)Python Software Foundation. Funciones integradas de Python:
uso de funciones como len().
https://docs.python.org/3/library/functions.html
'''