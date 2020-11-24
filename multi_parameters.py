# Define a function that takes an indefinite number of numbers as arguments and returns their average. If I&nbsp;called your function with foo(10, 20, 30, 40) it should return the 25, the average of those numbers.

def mean(*args):
    #return type(args)
    return sum(args) / len(args)

print(mean(10, 20, 30, 40))