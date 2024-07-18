# Author: Wendy Y. Falcon Kuffel
# GitHub username: falcon-source
# Date: 7/16/2024
# Description: Recursive function that takes two positive integers as parameters
# and returns the product of those two numbers.

def multiply(x, y):
    """
    Recursively multiplies two integers x and y without using multiplication.

    Parameters:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The product of x and y.
    """
    # Base case: if y is 0, return 0 (since anything multiplied by 0 is 0)
    if y == 0:
        return 0
    # Base case: if y is 1, return x
    elif y == 1:
        return x
    # If y is positive, recursively add x
    elif y > 1:
        return x + multiply(x, y - 1)
    # If y is negative, convert to positive multiplication and then negate result
    else:
        return -multiply(x, -y)


# Example function calls with correct indentation:
result = multiply(7, 4)
print(result)  # Output: 28

result = multiply(7, -4)
print(result)  # Output: -28
