
numbers = input("Enter comma-separated numbers: ")

# Generate list and tuple
num_list = numbers.split(',')
num_tuple = tuple(num_list)

# Display list and tuple
print("List:", num_list)
print("Tuple:", num_tuple)

# Count total elements
print("Total number of elements:", len(num_list))

# Display first and last elements
print("First element:", num_list[0])
print("Last element:", num_list[-1])

# Display list in reverse order
print("List in reverse order:", num_list[::-1])
