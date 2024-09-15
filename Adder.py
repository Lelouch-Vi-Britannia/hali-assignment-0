# Python script to add two numbers from command line input with sanity check

def get_number(prompt):
    while True:
        try:
            # Try to convert input to a float
            return float(input(prompt))
        except ValueError:
            # If conversion fails, prompt the user to try again
            print("Invalid input. Please enter a valid number.")

# Taking two numbers as input from the user with sanity check
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

# Adding the two numbers
sum = num1 + num2

# Printing the sum to the command line
print(f"The sum of {num1} and {num2} is {sum}")

