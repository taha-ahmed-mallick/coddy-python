def sigma(n):
    # Write your code below
    sumation = 0
    while n > 0:
        sumation+=n
        n-=1
    return sumation

n = int(input())
# Call the function below
result = sigma(n)
print(result)