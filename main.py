def values(lst):
    # Write code here
    for i in range(len(lst)):
        print(lst[i])
    pass

usr_lst = input().split(",")
values(usr_lst)