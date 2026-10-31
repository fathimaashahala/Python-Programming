
print("===== LIST OPERATIONS =====")
print("1. Create a List")
print("2. Search an Element")
print("3. Update an Element")
print("4. Filter Even Numbers")
print("5. Add an Element")
print("6. Remove an Element")
print("7. Sort the List")
print("8. Display the List")

lst = list(map(int, input("Enter list elements separated by spaces: ").split()))

choice = int(input("Enter your choice (1-8): "))

if choice == 1:
    print("Created List:", lst)

elif choice == 2:
    num = int(input("Enter element to search: "))
    if num in lst:
        print(num, "is found at index", lst.index(num))
    else:
        print(num, "is not found")

elif choice == 3:
    old = int(input("Enter element to update: "))
    if old in lst:
        new = int(input("Enter new value: "))
        index = lst.index(old)
        lst[index] = new
        print("Updated List:", lst)
    else:
        print("Element not found")

elif choice == 4:
    even = [x for x in lst if x % 2 == 0]
    print("Even Numbers:", even)

elif choice == 5:
    num = int(input("Enter element to add: "))
    lst.append(num)
    print("List after adding:", lst)

elif choice == 6:
    num = int(input("Enter element to remove: "))
    if num in lst:
        lst.remove(num)
        print("List after removing:", lst)
    else:
        print("Element not found")

elif choice == 7:
    lst.sort()
    print("Sorted List:", lst)

elif choice == 8:
    print("List Elements:", lst)

else:
    print("Invalid Choice!")
