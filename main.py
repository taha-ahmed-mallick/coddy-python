lst = input().split(",")
# Write your code below
# list containing every 3rd element from index 1
print(lst[1::3])
# list containing every element from 6th to 1st in reverse order
print(lst[5-len(lst):-len(lst)-1:-1])
# list containing every second element starting from the middle of the list to the end
print(lst[len(lst)//2::2])