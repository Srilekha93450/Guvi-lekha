def is_anagram(str1, str2):
    # Remove spaces and convert strings to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If lengths are different, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Dictionary to store character frequencies of str1
    char_freq = {}

    # Count frequencies of characters in str1
    for char in str1:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Check if str2 has the same characters with the same frequencies
    for char in str2:
        if char in char_freq:
            char_freq[char] -= 1
            if char_freq[char] == 0:
                del char_freq[char]  # Remove the character if its frequency becomes zero
        else:
            return False  # If a character is not present in str1, they cannot be anagrams

    # If all characters in str2 were found and their frequencies are zero in char_freq, they are anagrams
    return not char_freq

# Example usage
str1 = "listen"
str2 = "silent"
print(is_anagram(str1, str2))  # Output: True
