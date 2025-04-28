def find_occurrences(text, pattern):
    # Write your code here
    was_found = False
    occurrence = 0
    indices = []
    for i, char in enumerate(text):
        if pattern[0] == char:
            pattern_found = True
            for j, char_ in enumerate(pattern):
                if i + j <= len(text) - 1:
                    if char_ != text[i + j]:
                        pattern_found = False
                        break
                else:
                    pattern_found = False
            if pattern_found:
                occurrence += 1
                indices.append(i)
    if occurrence:
        was_found = True
    return (was_found, occurrence, indices)


# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)
