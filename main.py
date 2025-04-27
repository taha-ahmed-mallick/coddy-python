lst = list(map(int, input().split(",")))
# Write your code below
updated=[]
for index, num in enumerate(lst):
    if num < 50 or num%5==0:
        updated.append(index)

print(updated)