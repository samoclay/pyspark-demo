import pyspark

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = str(input("Enter 'A' for Addition, 'S' for Subtraction, 'M' for Multiplication, 'D' for Division: "))

if c == "A":
    print("Addition is: ", a + b)
elif c == "S":
    print("Subtraction is: ", a - b)
elif c == "M":
    print("Multiplication is: ", a * b)
elif c == "D":
    if b != 0:
        print("Division is: ", a / b)
    else:
        print("Error: Division by zero is not allowed.")

else: 
    print("Invalid operation code.")

    