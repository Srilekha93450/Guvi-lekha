def most_frequent_character(input_string):
    # Dictionary to store character frequencies
    char_freq = {}

    # Count frequencies of characters
    for char in input_string:
        if char in char_freq:  # If the character is already in the dictionary
            char_freq[char] += 1  # Increment its frequency
        else:
            char_freq[char] = 1  # Initialize its frequency to 1 if it's not in the dictionary

    # Find the character with the maximum frequency
    max_freq_char = max(char_freq, key=char_freq.get)  # Get the character with the maximum frequency using the max function

    return max_freq_char  # Return the character with the maximum frequency

# Example usage
input_str = "hello world"
print("Most frequent character:", most_frequent_character(input_str))

