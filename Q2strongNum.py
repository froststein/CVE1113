def findStrongNum(start,end):
    arr = []
    for num in range(start,end+1):
        if(num != 0):
            length = len(str(num))
            n1 = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                n1 += digit ** length  
                temp //= 10
            if(num == n1):
                arr.append(num)
    return arr

startRange = int(input("Start Range: "))
endRange = int(input("End Range: "))
resultArr = findStrongNum(startRange,endRange)
print("Armstrong numbers within {} to {} : {}".format(startRange,endRange,resultArr))