import random
def rollDices(num):
    arr = []
    d1arr = []
    d2arr = []
    total = 0
    for x in range(0,num):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        total = d1 + d2
        d1arr.append(d1)
        d2arr.append(d2)
        arr.append(total)
    print("Rolls for dice 1: {}".format(d1arr))
    print("Rolls for dice 2: {}".format(d2arr))
    return arr

num = int(input("Enter number of times to roll dice: "))
resultarr = rollDices(num)
print("The result of {} rolls are: {}".format(num,resultarr))