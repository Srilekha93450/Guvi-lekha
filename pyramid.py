rows = 5  # Number of rows for the pattern
num = 1   # Starting number for the pattern

# Loop through each row
for i in range(1, rows + 1):
    # Print spaces before printing numbers to create a triangular pattern
    for j in range(1, rows - i + 1):
        print(" ", end="")
    
    # Print numbers for the current row
    for j in range(1, i + 1):
        print(num, end=" ")  # Print the current number followed by a space
        num += 1  # Increment the number for the next iteration

    print()  # Move to the next line after printing each row