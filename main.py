def print_pattern(rows, cols):
    # Write your code here
    for _ in range(rows):
        print("*" * cols)
    pass


# Get input for rows and columns
rows = int(input())
cols = int(input())

# Call the function
print_pattern(rows, cols)