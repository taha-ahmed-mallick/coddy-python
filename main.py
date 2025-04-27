lst = input().split(",")
# Write your code below
half = len(lst)//2
if len(lst)%2==0:
    print(lst[half-1:half+1])
else:
    print(lst[half-1:half+2])