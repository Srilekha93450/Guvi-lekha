def count_unique_characters(input_string):
    unique_chars = set(input_string)  # Create a set to store unique characters from the input string
    return len(unique_chars)  # Return the number of unique characters in the set

# Example usage:
input_string = "hello"
result = count_unique_characters(input_string)  # Call the function to count unique characters
print("Number of unique characters:", result)  # Print the result
