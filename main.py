lst = input().split(",")
# Write your code below
updated=[]
for items in lst:
    if len(items)>5:
        updated.append(items)

print(updated)