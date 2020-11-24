# Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros instead of strings. For example, I&nbsp;called your function with <code>foo([99, 'no data', 95, 94, 'no data'])</code> it should return <code>[99, 0, 95, 94, 0]</code>.

def zero_instead(list):
    return [item if type(item) != str else 0 for item in list]


print(zero_instead([99, 'no data', 95, 94, 'no data']))
