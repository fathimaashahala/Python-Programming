
import re

# Function to validate email address
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print("Valid Email Address")
    else:
        print("Invalid Email Address")


# Function to validate phone number
def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'

    if re.match(pattern, phone):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")


# Function to extract transaction IDs
def extract_transaction_id(log):
    pattern = r'TXN\d+'

    ids = re.findall(pattern, log)

    if ids:
        print("Transaction IDs:", ids)
    else:
        print("No Transaction IDs Found")


# Main Program
print("===== INPUT VALIDATION SYSTEM =====")
print("1. Validate Email Address")
print("2. Validate Phone Number")
print("3. Extract Transaction IDs")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    email = input("Enter Email Address: ")
    validate_email(email)

elif choice == 2:
    phone = input("Enter Phone Number: ")
    validate_phone(phone)

elif choice == 3:
    log = input("Enter Log Message: ")
    extract_transaction_id(log)

else:
    print("Invalid Choice!")
