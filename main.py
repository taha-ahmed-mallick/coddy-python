def create_pattern(numbers, repeats):
    # Write your code here
    numbers = numbers*2
    numbers = numbers*repeats
    return numbers

numbers = input().split(", ")
repeat = int(input())
print(create_pattern(numbers, repeat))