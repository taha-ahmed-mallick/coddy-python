iteration = int(input())

def repeat():
    sumation = 0
    for i in range(1, 10001):
        sumation+=i
    for i in range(iteration):
        print(sumation)
    pass

repeat()