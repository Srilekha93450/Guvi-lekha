def count_words(input_string):
    # Split the string into words using whitespace as delimiter
    words = input_string.split()
    
    # Return the number of words
    return len(words)

# Example usage
input_str = "Hello world, how are you?"
print("Number of words:", count_words(input_str))
