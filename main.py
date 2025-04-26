iteration = int(input())

def repeat():
    sumation = 0
    for i in range(1, 1001):
        sumation+=i
    for i in range(iteration):
        print(sumation)
    pass

repeat()