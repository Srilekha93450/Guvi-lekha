def is_palindrome(input_string):
    # Convert the input string to lowercase to handle case-insensitivity
    input_string = input_string.lower()
    # Remove non-alphanumeric characters from the string
    input_string = ''.join(char for char in input_string if char.isalnum())
    # Check if the string is equal to its reverse (a palindrome)
    return input_string == input_string[::-1]

# Example usage:
input_string = "A man, a plan, a canal, Panama"
result = is_palindrome(input_string)  # Call the function to check if the input string is a palindrome
print(result)  # Print the result
