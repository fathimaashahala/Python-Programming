
print("===== DICTIONARY AND SET OPERATIONS =====")
print("1. Sort a Dictionary")
print("2. Merge Two Dictionaries")
print("3. Count Character Frequency")
print("4. Find Common Elements in Sets")
print("5. Find Unique Elements in Sets")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    d = {'banana': 3, 'apple': 5, 'orange': 2}
    sorted_dict = dict(sorted(d.items()))
    print("Original Dictionary:", d)
    print("Sorted Dictionary:", sorted_dict)

elif choice == 2:
    d1 = {'a': 10, 'b': 20}
    d2 = {'c': 30, 'd': 40}
    merged = {**d1, **d2}
    print("First Dictionary:", d1)
    print("Second Dictionary:", d2)
    print("Merged Dictionary:", merged)

elif choice == 3:
    string = input("Enter a string: ")
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print("Character Frequency:", frequency)

elif choice == 4:
    set1 = set(map(int, input("Enter first set elements: ").split()))
    set2 = set(map(int, input("Enter second set elements: ").split()))

    common = set1 & set2
    print("Common Elements:", common)

elif choice == 5:
    set1 = set(map(int, input("Enter first set elements: ").split()))
    set2 = set(map(int, input("Enter second set elements: ").split()))

    unique = set1 ^ set2
    print("Unique Elements:", unique)

else:
    print("Invalid Choice!")
