def factorial(num):
    output = num
    
    for x in range(1, num):
        output *= x

    return output


print(factorial(5))