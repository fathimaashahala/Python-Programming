
# Student Performance Analysis System

# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to find highest mark
def highest_mark(marks):
    return max(marks)

# Function to find lowest mark
def lowest_mark(marks):
    return min(marks)

# Function to determine grade
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# Main program
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = []
    for j in range(3):
        mark = float(input("Enter mark for subject " + str(j + 1) + ": "))
        marks.append(mark)

    total = calculate_total(marks)
    avg = calculate_average(marks)
    highest = highest_mark(marks)
    lowest = lowest_mark(marks)
    grade = calculate_grade(avg)

    students.append({
        'name': name,
        'total': total,
        'average': avg,
        'highest': highest,
        'lowest': lowest,
        'grade': grade
    })

# Display student performance
print("\n===== STUDENT PERFORMANCE REPORT =====")

for s in students:
    print("\nStudent Name:", s['name'])
    print("Total Marks:", s['total'])
    print("Average Marks:", round(s['average'], 2))
    print("Highest Mark:", s['highest'])
    print("Lowest Mark:", s['lowest'])
    print("Grade:", s['grade'])

# Sort students using lambda expression
students.sort(key=lambda x: x['total'], reverse=True)

print("\n===== STUDENTS SORTED BY TOTAL MARKS =====")

for s in students:
    print(s['name'], "-", s['total'])
