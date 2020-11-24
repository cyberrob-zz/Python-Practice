def double_char(txt):
    output = ''
    for char in txt:
        for i in [0, 1]:
            output += char
        
    return output


print(double_char('hello'))
