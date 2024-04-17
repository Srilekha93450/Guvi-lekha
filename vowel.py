def count_vowels(string):
    # Define a string containing all vowels
    vowels = 'AEIOU'
    
    # Create a dictionary to store the count of each individual vowel
    vowel_count = {}
    
    # Initialize a variable to store the total count of vowels
    total_vowels = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel (case-insensitive)
        if char.upper() in vowels:
            # Update the count of the current vowel in the dictionary
            # If the vowel is not already in the dictionary, initialize its count to 0
            # Then increment its count by 1
            vowel_count[char.upper()] = vowel_count.get(char.upper(), 0) + 1
            
            # Increment the total count of vowels
            total_vowels += 1

    # Return the total count of vowels and the dictionary containing the count of each individual vowel
    return total_vowels, vowel_count

# Example usage
input_string = "Guvi Geeks Network Private Limited"
total_vowels, individual_vowels_count = count_vowels(input_string)

print("Total number of vowels:", total_vowels)
print("Count of each individual vowel:")
for vowel, count in individual_vowels_count.items():
    print(vowel, ":", count)