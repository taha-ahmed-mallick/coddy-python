def reverse(lst):
    # Write code here
    print(lst)
    rev = []
    for i in range(len(lst)):
        print(len(lst)-i-1)
        rev.append(lst[len(lst)-i-1])
    return rev

lst = list(map(int, input().split(",")))
changed = reverse(lst)
print(changed)
