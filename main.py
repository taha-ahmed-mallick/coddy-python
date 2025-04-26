def prod(lst):
    # Write code here
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
    return product

lst = list(map(int, input().split(",")))
changed = prod(lst)
print(changed)
