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
            string = f"{n}"
            if "3" in string:
                return "Almost Fizz"
            else:
                return f"{n}"

usr_n = int(input())
for i in range(1, usr_n+1):
    result = fizzbuzz(i)
    print(result)