def sumMul(input):
    arr = []
    for i in range(3,input+1):
        if(i <= input and i % 3 ==0):
            arr.append(i)
        elif ( i <= input and i % 5 == 0):
            arr.append(i)
    print(arr)
    result = 0
    for x in arr:
        result+=x
    return result
    
    
input = int(input("Enter number: "))
result = sumMul(input)
print("Sum: {}".format(result))