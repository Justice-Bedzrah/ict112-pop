#A Calculator Progrm
print("WELCOME TO THE CALCULATOR PROGRAM")
print("=================================")
print()
number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))
print()
print("Addition")
print(number1,"+",number2,"=",number1 + number2)
print()
print("Subtraction")
print(number1,"-",number2,"=",number1 - number2)
print()
print("Multiplication")
print(number1,"*",number2,"=",number1 * number2)
print()
print("Divition")
print(number1,"/",number2,"=",number1 / number2)
print()
print("End of program. Thanks for using it")
print()

#A Circle Program
print("WELCOME TO THE CIRCLE PROGRAM")
print("=================================")
print()
PI = 3.14159
radius = float(input("Enter radius: "))
area = PI * radius * radius
print("The area of a circle with radius",radius,"is",round(area,2))
