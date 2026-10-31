
import math

print("===== BASIC COMPUTATIONAL PROBLEMS =====")
print("1. Find the Area of a Circle")
print("2. Check Whether a Year is a Leap Year")
print("3. Find the Largest of Three Numbers")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    print("Area of the circle =", round(area, 2))

elif choice == 2:
    year = int(input("Enter a year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")

elif choice == 3:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("The largest number is:", largest)

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
