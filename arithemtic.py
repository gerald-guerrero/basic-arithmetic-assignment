# The following two lines assigns the user input to two float type variables
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

add_result = num1 + num2 # Addition operation for the inputs
sub_result = num1 - num2 # Subtraction operation for the inputs
mul_result = num1 * num2 # Multiplication operation for the inputs
# Ternary operator checks if num2 is 0 to proceed with division or error message
div_result = num1 / num2 if num2 != 0 else "Error! Cannot divide by zero"

# The following lines print the relevant results as formatted strings
print(f"\nAddition result: {add_result:.2f}")
print(f"Subtraction result: {sub_result:.2f}")
print(f"Multiplcation result: {mul_result:.2f}")
# Ternary operator checks if div_result is a float to print either a float or error message
print("Division result: " + (f"{div_result:.2f}" if type(div_result) == float else f"{div_result}"))