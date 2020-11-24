# Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically. For example, if I&nbsp;called your function with <code>foo("snow", "glacier", "iceberg")</code> it should return <code>["GLACIER", "ICEBERG", "SNOW"]</code>.

def foo(*args):
    return [item.upper() for item in args]

def find_sum(**kwargs):
    # kwargs is dict
    return sum(kwargs.values())


# print(foo("snow", "glacier", "iceberg"))
print(find_sum(a=1,b=2,c=3,d=4,e=5))