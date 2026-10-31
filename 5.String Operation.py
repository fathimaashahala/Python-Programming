
print("===== STRING PROCESSING OPERATIONS =====")
print("1. Character Replacement")
print("2. String Reversal")
print("3. Palindrome Checking")
print("4. Character Frequency")
print("5. Word Frequency")

choice = int(input("Enter your choice (1-5): "))

string = input("Enter a string: ")

if choice == 1:
    old = input("Enter the character to replace: ")
    new = input("Enter the new character: ")
    result = string.replace(old, new)
    print("Modified String:", result)

elif choice == 2:
    reverse = string[::-1]
    print("Reversed String:", reverse)

elif choice == 3:
    reverse = string[::-1]
    if string.lower() == reverse.lower():
        print("The string is a Palindrome")
    else:
        print("The string is not a Palindrome")

elif choice == 4:
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print("Character Frequencies:")
    for char, count in frequency.items():
        print(char, ":", count)

elif choice == 5:
    words = string.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("Word Frequencies:")
    for word, count in frequency.items():
        print(word, ":", count)

else:
    print("Invalid Choice!")
