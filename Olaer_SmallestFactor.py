# Get the smallest factor
def check_factor(n):
    # Check for divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i  # Found a factor
    return n  # If no factor is found, n is a prime number


# Get user input for the integer
def get_user_input():
    while True:
        try:
            num = int(input("Enter an integer greater than or equal to 2: "))
            if num >= 2:  # Check if the number is less than or greater than 2
                return num
            else:
                print("Invalid input. Enter a number greater than or equal to 2.\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


# Check if yes or no input only
def check_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in {'yes', 'no'}:
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.\n")


# Print the result and ask if another input is needed.
def main():
    while True:
        num = get_user_input()
        result = check_factor(num)
        print("The smallest factor of", str(num), "other than 1 is", str(result), "\n")

        next_input = check_input("Do you want to input another integer? (yes/no): ")
        if next_input == 'yes':
            print("")
            continue
        else:
            print("\n- - Exiting - -")
            break


main()
