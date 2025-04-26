print("Welcome to FizzBuzz!")
def fizzbuzz(n):
    if n%21==0:
        return "FizzBuzz"
    else:
        if n%7==0:
            return "Buzz"
        elif n%3==0:
            return "Fizz"
        else:
            return f"{n}"

usr_n = int(input())
result = fizzbuzz(usr_n)
print(result)