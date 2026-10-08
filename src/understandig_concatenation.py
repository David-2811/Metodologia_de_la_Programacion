#Combinación o concatenación de Strigns
first_name = "david"
last_name = "sanchez"
full_name = first_name + " " + last_name
print(full_name.title())
print("holi".upper(), first_name + " " + last_name)

#WhiteSpace
"""
Se refiere a cualquier caracter que no se imprime, es decir
un espacio ( ),
tabuladores (\t)y final de  linea (\n)
Se usan comúnmente para organizar salidas de texto a usuarios de tal manera
que sea amigable para el usuario de ver
"""
print("python")
print("\tPyhon")
print("\t\tPyhton")
print("Lenguajes:\n\tPython\nC\nJavaScript")

#f-strings
famous_person = "David Sanchez"
message = f' {famous_person.upper()} una vez dijo: Python is love'
print(message)

