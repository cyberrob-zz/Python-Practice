# Define a function that takes as parameter a list that contains decimal numbers as strings and returns the sum of those numbers. For example, I&nbsp;called your function with <code>foo(['1.2', '2.6', '3.3'])</code> it should return <code>7.1</code>. Note that the floats of the input list are string datatypes.

def convert_n_sum(list):
    new_list = [float(item) for item in list if type(item) == str]
    return sum(new_list)

print(convert_n_sum(['1.2', '2.6', '3.3']))