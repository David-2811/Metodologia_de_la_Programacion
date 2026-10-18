# Manejo de numeros y booleanos en Python

'''
    Nombre: Jaime David Sanchez Hernandez
    Matricula: 2630009
    Grupo: IM - 1
'''

"""
    Resumen ejecutivo:
El tipo de dato int representa números enteros, mientras que float permite representar números con decimales.
Los valores booleanos pueden ser True (verdadero) o False (falso).
Las comparaciones, como >=, < e ==, generan resultados booleanos.
Los operadores lógicos, como and y or, permiten combinar condiciones para tomar decisiones.
La validación de rangos ayuda a detectar valores no válidos antes de realizar los cálculos.
Es importante comprobar los datos antes de realizar divisiones para evitar la división entre cero.
Este documento presenta seis problemas que utilizan tipos de datos numéricos y booleanos en Python.
Cada problema incluye descripción, entradas, salidas, validaciones y tres casos de prueba.
Los programas realizan cálculos numéricos y utilizan condiciones booleanas para determinar resultados.
"""

"""
    Principios y buenas practicas:
- Usar tipos apropiados: int para contadores, float para cantidades con decimales.
- Evitar duplicar expresiones complejas: guardar resultados intermedios en variables.
- Validar datos antes de operar.
- Usar nombres de variables descriptivos y mensajes claros para el usuario.
- Documentar claramente cómo se interpretan los booleanos.
"""

"""
Problem 1: Temperature Converter and Range Flag

Description:
This program converts a temperature from Celsius to Fahrenheit
and Kelvin. It also determines whether the Celsius temperature
is considered high (greater than or equal to 30.0).

Inputs:
- temp_c: A temperature in Celsius that can be converted to float.

Outputs:
- Fahrenheit: The temperature in Fahrenheit.
- Kelvin: The temperature in Kelvin.
- High temperature: true if temp_c >= 30.0, false otherwise.

Validations:
- Verify that the input can be converted to float.
- Reject temperatures below absolute zero (-273.15 Celsius),
  because they produce a negative Kelvin temperature.
- Handle invalid numeric input.

Test cases:
1) Normal: 25.0 -> Fahrenheit: 77.0, Kelvin: 298.15,
   High temperature: false.
2) Border: 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15,
   High temperature: true.
3) Error: "abc" -> Error: invalid input.

Best Practices:
- Use float for temperatures with decimal values and bool
  for logical flags.
- Store intermediate results in descriptive variables.
- Validate input before performing calculations.
- Use descriptive variable names and clear output messages.
- The boolean is_high_temperature is true when temp_c >= 30.0
  and false when temp_c < 30.0.
"""

print('---Problem 1: Temperature Converter and Range Flag---')
ABSOLUTE_ZERO_C = -273.15
HIGH_TEMPERATURE_THRESHOLD = 30.0

temp_input = input("Enter temperature in Celsius: ")
temp_input = temp_input.replace(" ", "")

if temp_input.replace(".", "", 1).replace("-", "", 1).isdigit():
    temp_c = float(temp_input)

    if temp_c < ABSOLUTE_ZERO_C:
        print("Error: invalid temperature.")
        print("Fahrenheit: undefined")
        print("Kelvin: undefined")
        print("High temperature: undefined")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= HIGH_TEMPERATURE_THRESHOLD

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", str(is_high_temperature).lower())

else:
    print("Error: This is not a temperature.")
    print("Fahrenheit: undefined")
    print("Kelvin: undefined")
    print("High temperature: undefined")


"""
Problem 2: Work Hours and Overtime Payment

Description:
This program calculates an employee's weekly pay.
Regular hours are paid at the normal hourly rate.
Hours above 40 are paid at 150% of the normal rate.

Inputs:
- hours_worked: Total hours worked during the week.
- hourly_rate: Regular payment per hour.

Outputs:
- Regular pay: Payment for regular hours.
- Overtime pay: Payment for overtime hours.
- Total pay: Total weekly payment.
- Has overtime: true if hours_worked > 40, false otherwise.

Validations:
- hours_worked must be greater than or equal to 0.
- hourly_rate must be greater than 0.
- If either validation fails, display "Error: invalid input".

Test cases:
1) Normal: 35 hours, rate 20 -> Regular pay: 700.0,
   Overtime pay: 0.0, Total pay: 700.0, Has overtime: false.
2) Border: 40 hours, rate 20 -> Regular pay: 800.0,
   Overtime pay: 0.0, Total pay: 800.0, Has overtime: false.
3) Error: -5 hours, rate 20 -> Error: invalid input.
"""

print('\n---Problem 2: Work Hours and Overtime Payment---')
hours_input = input("Enter hours worked: ")
rate_input = input("Enter hourly rate: ")

hours_input = "".join(hours_input.split())
rate_input = "".join(rate_input.split())

if (hours_input.replace(".", "", 1).isdigit()
        and rate_input.replace(".", "", 1).isdigit()):

    hours_worked = float(hours_input)
    hourly_rate = float(rate_input)

    if hours_worked >= 0 and hourly_rate > 0:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", str(has_overtime).lower())
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")



"""
Problem 3: Discount Eligibility with Booleans

Description:
This program determines whether a customer qualifies for a discount.
Customers qualify if they are students, seniors, or spend at least 1000.0.
Eligible customers receive a 10% discount on their purchase.

Inputs:
- purchase_total: Total purchase amount.
- is_student_text: "YES" or "NO".
- is_senior_text: "YES" or "NO".

Outputs:
- Discount eligible: true or false.
- Final total: Final amount after applying the discount if eligible.

Validations:
- purchase_total must be greater than or equal to 0.0.
- Student and senior answers must be "YES" or "NO".
- Normalize answers to uppercase.
- Display "Error: invalid input" if any input is invalid.

Test cases:
1) Normal: 500.0, YES, NO -> Discount eligible: true,
   Final total: 450.0.
2) Border: 1000.0, NO, NO -> Discount eligible: true,
   Final total: 900.0.
3) Error: 500.0, MAYBE, NO -> Error: invalid input.
"""

print('\n---Problem 3: Discount Eligibility with Booleans---')
purchase_input = input("Enter purchase total: ")
is_student_text = input("Are you a student? (YES/NO): ")
is_senior_text = input("Are you a senior? (YES/NO): ")

purchase_input = "".join(purchase_input.split())
is_student_text = is_student_text.strip().upper()
is_senior_text = is_senior_text.strip().upper()

if purchase_input.replace(".", "", 1).isdigit():
    purchase_total = float(purchase_input)

    if purchase_total >= 0 and is_student_text in ("YES", "NO") and is_senior_text in ("YES", "NO"):
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", final_total)
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")



"""
Problem 4: Basic Statistics of Three Integers

Description:
This program reads three integers and calculates their sum,
average, maximum, and minimum values. It also determines
whether all three integers are even.

Inputs:
- n1: First integer.
- n2: Second integer.
- n3: Third integer.

Outputs:
- Sum: The sum of the three integers.
- Average: The arithmetic average as a float.
- Max: The largest integer.
- Min: The smallest integer.
- All even: true if all three integers are even, otherwise false.

Validations:
- Verify that all three inputs can be converted to integers.
- Negative and positive integers are allowed.
- Display "Error: invalid input" if any input is not an integer.

Test cases:
1) Normal: 2, 4, 6 ->
   Sum: 12
   Average: 4.0
   Max: 6
   Min: 2
   All even: true

2) Border: -3, 0, 3 ->
   Sum: 0
   Average: 0.0
   Max: 3
   Min: -3
   All even: false

3) Error: 2, abc, 6 ->
   Error: invalid input
"""

print('\n---Problem 4: Basic Statistics of Three Integers---')
n1_text = input("Enter the first integer: ").strip()
n2_text = input("Enter the second integer: ").strip()
n3_text = input("Enter the third integer: ").strip()

if (n1_text.lstrip("-").isdigit()
        and n2_text.lstrip("-").isdigit()
        and n3_text.lstrip("-").isdigit()):

    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (
        (n1 % 2 == 0)
        and (n2 % 2 == 0)
        and (n3 % 2 == 0)
    )

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

else:
    print("Error: invalid input")



"""
Problem 5: Loan Eligibility (Income and Debt Ratio)

Description:
This program determines whether a person is eligible for a loan.
Eligibility depends on monthly income, the debt ratio, and
the credit score.

Inputs:
- monthly_income: Monthly income as a float.
- monthly_debt: Monthly debt payments as a float.
- credit_score: Credit score as an integer.

Outputs:
- Debt ratio: Monthly debt divided by monthly income.
- Eligible: true if all loan requirements are met, otherwise false.

Validations:
- monthly_income must be greater than 0.0.
- monthly_debt must be greater than or equal to 0.0.
- credit_score must be greater than or equal to 0.
- Inputs must have valid numeric formats.
- Display "Error: invalid input" if any input is invalid.

Test cases:
1) Normal: 10000.0, 2000.0, 700 ->
   Debt ratio: 0.2
   Eligible: true

2) Border: 8000.0, 3200.0, 650 ->
   Debt ratio: 0.4
   Eligible: true

3) Error: 0.0, 1000.0, 700 ->
   Error: invalid input
"""

print('\n---Problem 5: Loan Eligibility (Income and Debt Ratio)---')
income_text = "".join(input("Enter monthly income: ").split())
debt_text = "".join(input("Enter monthly debt: ").split())
credit_text = input("Enter credit score: ").strip()

if (income_text.replace(".", "", 1).isdigit()
        and debt_text.replace(".", "", 1).isdigit()
        and credit_text.isdigit()):

    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(credit_text)

    if (monthly_income > 0.0
            and monthly_debt >= 0.0
            and credit_score >= 0):

        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print("Debt ratio:", debt_ratio)
        print("Eligible:", str(eligible).lower())

    else:
        print("Error: invalid input")

else:
    print("Error: invalid input")



"""
Problem 6: Body Mass Index (BMI) and Category Flag

Description:
This program calculates a person's Body Mass Index (BMI)
using weight in kilograms and height in meters.
It determines whether the person is underweight, normal,
or overweight based on the calculated BMI.

Inputs:
- weight_kg: Weight in kilograms as a float.
- height_m: Height in meters as a float.

Outputs:
- BMI: The calculated BMI rounded to two decimal places.
- Underweight: true if BMI is less than 18.5.
- Normal: true if BMI is between 18.5 and 25.0, excluding 25.0.
- Overweight: true if BMI is greater than or equal to 25.0.

Validations:
- weight_kg must be greater than 0.0.
- height_m must be greater than 0.0.
- Inputs must have valid numeric formats.
- Display "Error: invalid input" if any input is invalid.

Test cases:
1) Normal: 70.0, 1.75 ->
   BMI: 22.86
   Underweight: false
   Normal: true
   Overweight: false

2) Border: 50.0, 1.70 ->
   BMI: 17.3
   Underweight: true
   Normal: false
   Overweight: false

3) Error: 70.0, 0.0 ->
   Error: invalid input
"""

print('\n---Problem 6: Body Mass Index (BMI) and Category Flag---')
weight_text = "".join(input("Enter weight in kilograms: ").split())
height_text = "".join(input("Enter height in meters: ").split())

if (weight_text.replace(".", "", 1).isdigit()
        and height_text.replace(".", "", 1).isdigit()):

    weight_kg = float(weight_text)
    height_m = float(height_text)

    if weight_kg > 0.0 and height_m > 0.0:

        bmi = weight_kg / (height_m * height_m)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())

    else:
        print("Error: invalid input")

else:
    print("Error: invalid input")


"""
    CONCLUCIONES:
Durante esta actividad aprendí a utilizar los tipos de datos int y float
para realizar cálculos, y los valores booleanos True y False para tomar
decisiones mediante condiciones. Comprendí la importancia de validar las
entradas y evitar divisiones entre cero. También practiqué el uso de los
operadores lógicos and, or y not para combinar condiciones. Finalmente,
reconocí que estos conocimientos se aplican en situaciones reales, como
el cálculo de nóminas, descuentos y préstamos.

    REFERENCIAS:
1)Python Software Foundation. Python Documentation - Boolean Type: bool.
https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
2)Python Software Foundation. Python Documentation - Built-in Functions.
https://docs.python.org/3/library/functions.html
3)Python Software Foundation. Python Tutorial - More Control Flow Tools.
https://docs.python.org/3/tutorial/controlflow.html
4)Python Software Foundation. Python Documentation - Expressions.
https://docs.python.org/3/reference/expressions.html
5)Python Software Foundation. Python Tutorial - More Control Flow Tools.
https://docs.python.org/3/tutorial/controlflow.html
"""