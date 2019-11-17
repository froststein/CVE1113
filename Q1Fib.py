def fib(input):
    if (input == 1): 
        return 0
    # Second Fibonacci number is 1 
    elif (input == 2): 
        return 1
    else: 
        return fib(input - 1)+fib(input - 2) 

input = int(input("Number of fib numbers to geenrate: "))
result = fib(input)
print("Result: {}".format(result))
    