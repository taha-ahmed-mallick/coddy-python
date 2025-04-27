text = input()
# Write your code below
text = text.lower()

count = 0
for char in text:
    if char == "p":
        count+=1

print(count)