def remove_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define a string containing all vowels
    
    # Use a generator expression to iterate over each character in the input string
    # Filter out characters that are vowels by checking if they are not in the vowels string
    # Join the remaining characters together to form the modified string without vowels
    return ''.join(char for char in input_string if char not in vowels)

# Example usage:
input_string = "Hello, how are you?"
result = remove_vowels(input_string)
print(result)  # Output: "Hll, hw r y?"

