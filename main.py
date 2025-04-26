def change_element(lst, index, new_element):
    # Write code here
    lst[index] = new_element
    return lst

usr_lst = input().split(",")
index = int(input())
new_element = input()
changed = change_element(usr_lst, index, new_element)
print(changed)