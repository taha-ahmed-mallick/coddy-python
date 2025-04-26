def merge(lst1, lst2):
    # Write code here
    for i in range(len(lst2)):
        lst1.append(lst2[i])
    lst1.sort()
    return lst1

lst1 = list(map(int, input().split(",")))
lst2 = list(map(int, input().split(",")))
changed = merge(lst1, lst2)
print(changed)