lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
result = []
for i in lst1:
    add_ele = True
    for j in lst2:
        if i == j:
            add_ele = False
    if add_ele:
        result.append(i)

print(result)