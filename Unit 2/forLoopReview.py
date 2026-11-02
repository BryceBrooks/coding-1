# Function to multiply numbers from 1 to 15 by 3
def multiply_by_three():
    # Using range to generate numbers from 1 to 15
    for num in range(1, 16):
        result = num * 3
        print(f"{num} multiplied by 3 is {result}")

# Run the function
multiply_by_three()

def collect_numbers():
    """
    Collect exactly 5 numbers from the user and store them in a list.
    Once collected, print the list and stop.
    """
    numbers = []
    
    while len(numbers) < 5:
        try:
            # Prompt user for input
            user_input = input(f"Enter number {len(numbers) + 1} of 5: ")
            
            # Convert to float (supports integers and decimals)
            num = float(user_input)
            
            # Add to list
            numbers.append(num)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Print the final list
    print("\nYou entered the following numbers:")
    print(numbers)


# Run the function
if __name__ == "__main__":
    collect_numbers()