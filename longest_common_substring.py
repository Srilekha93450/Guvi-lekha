def longest_common_substring(str1, str2):
    m = len(str1)  # Length of the first string
    n = len(str2)  # Length of the second string

    # Create a table to store lengths of longest common suffixes
    # Initialize all values to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length of the longest common substring and its ending index
    max_length = 0  # Initialize the maximum length of the common substring to 0
    end_index = 0    # Initialize the ending index of the common substring to 0

    # Fill the dp table
    for i in range(1, m + 1):  # Iterate over the indices of the first string
        for j in range(1, n + 1):  # Iterate over the indices of the second string
            if str1[i - 1] == str2[j - 1]:  # If the characters at these indices are equal
                dp[i][j] = dp[i - 1][j - 1] + 1  # Update the length of the common substring
                if dp[i][j] > max_length:  # If the current common substring is longer than the previous longest
                    max_length = dp[i][j]  # Update the maximum length
                    end_index = i  # Update the ending index of the common substring
            else:
                dp[i][j] = 0  # If the characters are not equal, set the length to 0

    # Extract the longest common substring using the ending index and its length
    longest_substring = str1[end_index - max_length: end_index]  # Extract the substring from str1

    return longest_substring  # Return the longest common substring


# Example usage
str1 = "abcdef"
str2 = "bcde"
print("Longest common substring:", longest_common_substring(str1, str2))

